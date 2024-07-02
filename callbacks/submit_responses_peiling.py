from dash import Input, Output, State, callback_context
from dashapp import app
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

from assets.static_inputs import RESTRICTED_IDS_PEILING_ONLY, RESTRICTED_IDS_STEMMING_ONLY, CANDIDATES

# Replace with your actual PostgreSQL connection URL
DATABASE_URL = "postgresql://u3504p7koghd0t:p1137c9e21197f7bb29c4d2c5c709b856e3418e904cdf4652e37aa6f7efb05576@cjpee40i0fqgl.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d1p2f4i9n451f8"

# Set up SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class SurveyResponse(Base):
    __tablename__ = 'peiling_responses'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    page = Column(String)
    data = Column(Text)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_response_to_db(user_id, page, data):
    session = Session()
    response = session.query(SurveyResponse).filter_by(user_id=user_id, page=page).first()
    if response:
        response.data = json.dumps(data)
    else:
        response = SurveyResponse(user_id=user_id, page=page, data=json.dumps(data))
        session.add(response)
    session.commit()
    session.close()

@app.callback(
    [Output('incomplete-modal_peiling', 'is_open'), Output('success-modal_peiling', 'is_open'),
     Output('wrong-userid-modal_peiling', 'is_open')],
    [Input('submit-button_peiling', 'n_clicks'),
     ],
    [State('stored-user-id', 'data'), State('url', 'pathname'),
     State('peiling-q2', 'value')] +
    [State(f'dropdown_peiling-{i}', 'value') for i in range(5)]
)
def handle_submission(submit_n_clicks, stored_user_id, pathname, vrije_vraag, *dropdown_values):
    user_data = {}
    if not stored_user_id or 'id' not in stored_user_id:
        return False, False, True

    user_id = stored_user_id['id']
    print('user_id', user_id)
    if submit_n_clicks > 0:

        # Check if the user ID and URL combination is valid
        if not stored_user_id or 'id' not in stored_user_id or \
                (pathname == '/peiling' and user_id not in RESTRICTED_IDS_PEILING_ONLY):
            return False, False, True  # Show the wrong user ID modal if the combination is not valid

        filled_dropdowns = [v for v in dropdown_values if v is not None]
        if 0 < len(filled_dropdowns) < 5:
            return True, False, False

        user_data[user_id] = {
            'rankings': '>>'.join(dropdown_values),
            'comment': vrije_vraag
        }

        # Store data in PostgreSQL
        try:
            save_response_to_db(user_id, pathname, user_data[user_id])
        except Exception as e:
            print(f"Error storing data: {e}")
            return False, False, True

        return False, True, False

    return False, False, False
