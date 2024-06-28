import json
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dash
from dash.dependencies import Input, Output, State
from dashapp import app

# Replace with your actual Heroku Postgres connection URL
DATABASE_URL = "postgresql://u5s15stvo89j49:p2095dee64da9073d0b5a81bff8f603ddc5c38cee18ffe9be010c065b0d79593e@ccaml3dimis7eh.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d5hi0d744nm4al"

# Set up SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class SurveyResponse(Base):
    __tablename__ = 'survey_responses'
    id = Column(Integer, primary_key=True)
    session_id = Column(String)
    page = Column(String)
    data = Column(Text)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_response_to_db(session_id, page, data):
    session = Session()
    response = session.query(SurveyResponse).filter_by(session_id=session_id, page=page).first()
    if response:
        response.data = json.dumps(data)
    else:
        response = SurveyResponse(session_id=session_id, page=page, data=json.dumps(data))
        session.add(response)
    session.commit()
    session.close()
#
# @app.callback(
#     Output('introduction-container', 'children'),
#     Input('submit-survey-introduction', 'n_clicks'),
#     [State('age-input', 'value'),
# State('work-input', 'value'),
# State('use_frequency-input', 'value'),
# State('viztype-input', 'value'),]
# )
# def save_answers_introduction(n_clicks, age, work,use_frequency,viztype, session_id):
#     if n_clicks > 0:
#         data = {"age": age,
#                 "work": work,
#                 "use_frequency": use_frequency,
#                 "viztype": viztype}
#         save_response_to_db(session_id['existing_id'], "introduction", data)
#         return f'Your response has been saved ({n_clicks}).'
#     else:
#         return 'Please submit your response.'
#
# @app.callback(
#     Output('alternative_pathways-container', 'children'),
#     Input('submit-survey-alternative_pathways', 'n_clicks'),
#     [State('pathway_number-input', 'value'), State('f_resilient_crops-input', 'value'),
#      State('long_term-input', 'value'), State('flexibility-level', 'value'), State('storage-general', 'data')]
# )
# def save_answers_alternatives(n_clicks, pathway_number, f_resilient_crops, long_term, flexibility, session_id):
#     if n_clicks > 0:
#         data = {
#             "pathway_number": pathway_number,
#             "f_resilient_crops": f_resilient_crops,
#             "long_term": long_term,
#             "flexibility": flexibility
#         }
#         save_response_to_db(session_id['existing_id'], "alternatives", data)
#         return f'Your response has been saved ({n_clicks}).'
#     else:
#         return 'Please submit your response.'
#
# @app.callback(
#     Output('pathways_performance-container', 'children'),
#     Input('submit-survey-pathways_performance', 'n_clicks'),
#     [State('color-input', 'value'), State('crop_loss-input', 'value'), State('performance-input', 'value'),
#      State('tradeoff-input', 'value'), State('storage-general', 'data')]
# )
# def save_answers_performance(n_clicks, color, crop_loss, performance, tradeoff, session_id):
#     if n_clicks > 0:
#         data = {
#             "color": color,
#             "crop_loss": crop_loss,
#             "performance": performance,
#             "tradeoff": tradeoff,
#         }
#         save_response_to_db(session_id['existing_id'], "pathways_performance", data)
#         return f'Your response has been saved ({n_clicks}).'
#     else:
#         return 'Please submit your response.'
#
# @app.callback(
#     Output('interaction_effects-container', 'children'),
#     Input('submit-survey-interaction_effects', 'n_clicks'),
#     [State('measure_shift-input', 'value'), State('performance_change-input', 'value'),
#      State('strong_tradeoffs-input', 'value'), State('strong_synergy-input', 'value'), State('storage-general', 'data')]
# )
# def save_answers_interactions(n_clicks, measure_shift, performance_change, strong_tradeoffs, strong_synergy, session_id):
#     if n_clicks > 0:
#         data = {
#             "measure_shift": measure_shift,
#             "performance_change": performance_change,
#             "strong_tradeoffs": strong_tradeoffs,
#             "strong_synergy": strong_synergy,
#         }
#         save_response_to_db(session_id['existing_id'], "interaction_effects", data)
#         return f'Your response has been saved ({n_clicks}).'
#     else:
#         return 'Please submit your response.'

# Callback for the introduction section
@app.callback(
    Output('introduction-container', 'children'),
    Output('modal-introduction', 'is_open'),
    Output('modal-body-introduction', 'children'),
    Input('submit-survey-introduction', 'n_clicks'),
    [State('age-input', 'value'), State('work-input', 'value'),
     State('use_frequency-input', 'value'), State('viztype-input', 'value'), State('storage-general', 'data')],
    State("modal-introduction", "is_open")
)
def save_answers_introduction(n_clicks, age, work, use_frequency, viztype, session_id, is_open):
    if n_clicks > 0:
        missing_fields = []
        if age is None:
            missing_fields.append("Age")
        if work is None:
            missing_fields.append("Work")
        if use_frequency is None:
            missing_fields.append("Use Frequency")
        if viztype is None:
            missing_fields.append("Visualization Type")

        if missing_fields:
            missing_fields_str = ", ".join(missing_fields)
            return 'Please complete all required fields before submitting.', True, f"The following fields are missing: {missing_fields_str}"
        else:
            data = {"age": age, "work": work, "use_frequency": use_frequency, "viztype": viztype}
            save_response_to_db(session_id['existing_id'], "introduction", data)
            return f'Your response has been saved ({n_clicks}).', False, ""
    return 'Please submit your response.', is_open, ""

# Callback for the alternative pathways section
@app.callback(
    Output('alternative_pathways-container', 'children'),
    Output('modal-alternatives', 'is_open'),
    Output('modal-body-alternatives', 'children'),
    Input('submit-survey-alternative_pathways', 'n_clicks'),
    [State('pathway_number-input', 'value'), State('f_resilient_crops-input', 'value'),
     State('long_term-input', 'value'), State('flexibility-level', 'value'), State('storage-general', 'data')],
    State("modal-alternatives", "is_open")
)
def save_answers_alternatives(n_clicks, pathway_number, f_resilient_crops, long_term, flexibility, session_id, is_open):
    if n_clicks > 0:
        missing_fields = []
        if pathway_number is None:
            missing_fields.append("Pathway Number")
        if f_resilient_crops is None:
            missing_fields.append("Resilient Crops")
        if long_term is None:
            missing_fields.append("Long Term")
        if flexibility is None:
            missing_fields.append("Flexibility Level")

        if missing_fields:
            missing_fields_str = ", ".join(missing_fields)
            return 'Please complete all required fields before submitting.', True, f"The following fields are missing: {missing_fields_str}"
        else:
            data = {"pathway_number": pathway_number, "f_resilient_crops": f_resilient_crops, "long_term": long_term, "flexibility": flexibility}
            save_response_to_db(session_id['existing_id'], "alternatives", data)
            return f'Your response has been saved ({n_clicks}).', False, ""
    return 'Please submit your response.', is_open, ""

# Callback for the pathways performance section
@app.callback(
    Output('pathways_performance-container', 'children'),
    Output('modal-performance', 'is_open'),
    Output('modal-body-performance', 'children'),
    Input('submit-survey-pathways_performance', 'n_clicks'),
    [State('color-input', 'value'), State('crop_loss-input', 'value'), State('performance-input', 'value'),
     State('tradeoff-input', 'value'), State('storage-general', 'data')],
    State("modal-performance", "is_open")
)
def save_answers_performance(n_clicks, color, crop_loss, performance, tradeoff, session_id, is_open):
    if n_clicks > 0:
        missing_fields = []
        if color is None:
            missing_fields.append("Color")
        if crop_loss is None:
            missing_fields.append("Crop Loss")
        if performance is None:
            missing_fields.append("Performance")
        if tradeoff is None:
            missing_fields.append("Tradeoff")

        if missing_fields:
            missing_fields_str = ", ".join(missing_fields)
            return 'Please complete all required fields before submitting.', True, f"The following fields are missing: {missing_fields_str}"
        else:
            data = {"color": color, "crop_loss": crop_loss, "performance": performance, "tradeoff": tradeoff}
            save_response_to_db(session_id['existing_id'], "pathways_performance", data)
            return f'Your response has been saved ({n_clicks}).', False, ""
    return 'Please submit your response.', is_open, ""

# Callback for the interaction effects section
@app.callback(
    Output('interaction_effects-container', 'children'),
    Output('modal-interactions', 'is_open'),
    Output('modal-body-interactions', 'children'),
    Input('submit-survey-interaction_effects', 'n_clicks'),
    [State('measure_shift-input', 'value'), State('performance_change-input', 'value'),
     State('strong_tradeoffs-input', 'value'), State('strong_synergy-input', 'value'), State('storage-general', 'data')],
    State("modal-interactions", "is_open")
)
def save_answers_interactions(n_clicks, measure_shift, performance_change, strong_tradeoffs, strong_synergy, session_id, is_open):
    if n_clicks > 0:
        missing_fields = []
        if measure_shift is None:
            missing_fields.append("Measure Shift")
        if performance_change is None:
            missing_fields.append("Performance Change")
        if strong_tradeoffs is None:
            missing_fields.append("Strong Tradeoffs")
        if strong_synergy is None:
            missing_fields.append("Strong Synergy")

        if missing_fields:
            missing_fields_str = ", ".join(missing_fields)
            return 'Please complete all required fields before submitting.', True, f"The following fields are missing: {missing_fields_str}"
        else:
            data = {"measure_shift": measure_shift, "performance_change": performance_change, "strong_tradeoffs": strong_tradeoffs, "strong_synergy": strong_synergy}
            save_response_to_db(session_id['existing_id'], "interaction_effects", data)
            return f'Your response has been saved ({n_clicks}).', False, ""
    return 'Please submit your response.', is_open, ""

# Close modal callback
@app.callback(
    Output("modal", "is_open"),
    [Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open


