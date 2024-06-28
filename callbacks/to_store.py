import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app


# # Callback to store data
# @app.callback(Output('storage-alternative_pathways', 'data'),
#               [Input('risk_owner_hazard', 'value'),
#                 Input('url', 'pathname'),
#
#                ],
#               State('storage-alternative_pathways', 'data')
#               )
# def store_choices_alternatives(risk_owner_hazard,pathname, stored_data):
#     ctx = callback_context
#     if not ctx.triggered:
#         stored_data['risk_owner_hazard'] = risk_owner_hazard if risk_owner_hazard is not None else stored_data.get('risk_owner_hazard', '')  # Use a specific key or dynamic based on another input
#     return stored_data

# # Callback to store data
# @app.callback(Output('storage-pathways_performance', 'data'),
#               [
#                Input('timehorizon', 'value'),
#                Input('scenarios', 'value'),
#                Input('performance_metric', 'value'),
#                Input('options', 'value'),
#                 Input('url', 'pathname'),
#                ],
#               State('storage-pathways_performance', 'data')
#               )
# def store_choices_performance(timehorizon, scenarios, performance_metric, plot_type,pathname, stored_data):
#     ctx = callback_context
#     if not ctx.triggered:
#         stored_data['timehorizon'] = timehorizon if timehorizon is not None else stored_data.get(
#             'timehorizon', '')  # Use a specific key or dynamic based on another input
#         stored_data['scenarios'] = scenarios if scenarios is not None else stored_data.get(
#             'scenarios', '')  # Use a specific key or dynamic based on another input
#         stored_data['performance_metric'] = performance_metric if performance_metric is not None else stored_data.get(
#             'performance_metric', '')  # Use a specific key or dynamic based on another input
#         stored_data['plot_type'] = plot_type if plot_type is not None else stored_data.get(
#             'plot_type', '')  # Use a specific key or dynamic based on another input
#     return stored_data
#
#
# # Callback to store data
# @app.callback(Output('storage-interactions', 'data'),
#               [
#                Input('multi_sectoral_interactions', 'value'),
#                Input('interaction_plot_options', 'value'),
# Input('url', 'pathname'),
#                ],
#               State('storage-interactions', 'data')
#               )
# def store_choices_interactions(interactions_of_interest, interaction_plot,pathname, stored_data):
#     ctx = callback_context
#     print(ctx)
#     if not ctx.triggered:
#         stored_data['interactions_of_interest'] = interactions_of_interest if interactions_of_interest is not None else stored_data.get(
#             'interactions_of_interest', '')  # Use a specific key or dynamic based on another input
#         stored_data['interaction_plot'] = interaction_plot if interaction_plot is not None else stored_data.get(
#             'plot_type', '')  # Use a specific key or dynamic based on another input
#     return stored_data
