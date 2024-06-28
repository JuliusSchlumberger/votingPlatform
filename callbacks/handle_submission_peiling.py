from dash import  Input, Output, State, callback_context
from dashapp import app
import pandas as pd

from assets.static_inputs import RESTRICTED_IDS_PEILING_ONLY, RESTRICTED_IDS_STEMMING_ONLY


@app.callback(
    [Output('incomplete-modal_peiling', 'is_open'), Output('success-modal_peiling', 'is_open'),
     Output('wrong-userid-modal_peiling', 'is_open')],
    [Input('submit-button_peiling', 'n_clicks'),
     ],
    [State('stored-user-id', 'data'), State('url', 'pathname'), State('peiling-q1', 'value'),
     State('peiling-q2', 'value')] +
    [State(f'dropdown_peiling-{i}', 'value') for i in range(5)]
)
def handle_submission(submit_n_clicks,
                      stored_user_id, pathname, q1_value, q2_value, *dropdown_values):
    user_data = {}
    user_id = stored_user_id['id']
    print('user_id', user_id)

    if submit_n_clicks > 0:
        # Check if the user ID and URL combination is valid
        if not stored_user_id or 'id' not in stored_user_id or \
                (pathname == '/peiling' and user_id not in RESTRICTED_IDS_PEILING_ONLY) or \
                (pathname == '/stemming' and user_id not in RESTRICTED_IDS_STEMMING_ONLY):
            return False, False, True  # Show the wrong user ID modal if the combination is not valid

        filled_dropdowns = [v for v in dropdown_values if v is not None]
        if 0 < len(filled_dropdowns) < 5:
            return True, False, False

        user_data[user_id] = {
            'q1': q1_value,
            'q2': q2_value,
            'rankings': dropdown_values
        }

        df = pd.DataFrame.from_dict(user_data, orient='index')
        df.to_csv(f'peiling_user_votes_{user_id}.csv')

        return False, True, False

    return False, False, False