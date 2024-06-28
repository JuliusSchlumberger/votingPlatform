from dash import dcc, Input, Output, State, callback_context
from dashapp import app
import dash_bootstrap_components as dbc
import pandas as pd
from assets.static_inputs import RESTRICTED_IDS_STEMMING_ONLY, RESTRICTED_IDS_PEILING_ONLY

# Callback to handle user ID submission
# Combined callback to handle user ID submission and modal close
# Combined callback to handle user ID submission and modal close
@app.callback(
    [Output('url', 'pathname'),  # Update the pathname to navigate to a new page
     Output('invalid_userid-modal', 'is_open'),
     Output('stored-user-id', 'data')],
    [Input('submit_userid-button', 'n_clicks'),
     Input('close-invalid_userid-modal', 'n_clicks')],
    [State('user-id', 'value'),
     State('url', 'pathname'),
     ]
)
def handle_user_id_and_modal(submit_n_clicks, close_modal_n_clicks, user_id, current_path):
    ctx = callback_context

    if ctx.triggered:
        prop_id = ctx.triggered[0]['prop_id']

        # Handle modal close action
        if prop_id == 'close-invalid-modal.n_clicks':
            return '/', False, {'id': ''}

        # Handle user ID submission
        if prop_id == 'submit_userid-button.n_clicks' and submit_n_clicks > 0:
            if user_id in RESTRICTED_IDS_STEMMING_ONLY:
                return '/stemming', False, {'id': user_id}  # Replace '/page1' with the actual path for LIST_1 users
            elif user_id in RESTRICTED_IDS_PEILING_ONLY:
                return '/peiling',False, {'id': user_id}  # Replace '/page2' with the actual path for LIST_2 users
            else:
                return '/', True, {'id': ''}  # Show the modal if user ID is not valid

    return '/', False, {'id': ''}