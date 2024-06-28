import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from assets.static_inputs import CANDIDATES, INTRODUCTION


dash.register_page(__name__, path='/stemming')

# List of candidates
candidates = CANDIDATES

# Function to determine the appropriate suffix for the choice number
def get_choice_suffix(index):
    if 11 <= index <= 13:
        return 'th'
    elif index % 10 == 1:
        return 'st'
    elif index % 10 == 2:
        return 'nd'
    elif index % 10 == 3:
        return 'rd'
    else:
        return 'th'


layout = dbc.Container([
# Introduction section
    # Introduction section
    dbc.Row(dbc.Col(html.H3("Stemming", className="text-success"), width=12), className="mt-3"),
    dbc.Row(dbc.Col(INTRODUCTION,
                    width=12), className="mb-3 "),

    # Question 1 section

    # Question 3 section with dropdowns
    html.Div(id="stemming-1", children=[
        dbc.Row(dbc.Col(html.H4("Welke methoden vindt je het meest geschikt voor de Nieuwelaan?", className="text-success"), width=12),
                className="mt-3"),
        dbc.Row(
            dbc.Col(html.P("Please rank all methods according to your preference."),
                    width=12)),

        *[dbc.Row(dbc.Col(dcc.Dropdown(
            id=f'dropdown_stemming-{i}',
            options=[{'label': candidate, 'value': candidate} for candidate in candidates],
            placeholder=f'Choose your {i + 1}{get_choice_suffix(i + 1)} choice'
        ), width=12), className="mb-3") for i in range(len(CANDIDATES))],
# Modals for pop-up messages
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Incomplete Submission")),
            dbc.ModalBody("Please fill in all the ranks before submitting."),
        ],
        id="incomplete_stemming-modal",
        is_open=False,
    ),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Submission Successful")),
            dbc.ModalBody("Your vote has been successfully submitted. Thanks for taking part in the vote. "
                          "If you made a mistake, you can just correct it and re-submit your vote."),
        ],
        id="success_stemming-modal",
        is_open=False,
    ),

    dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Invalid User ID")),
                dbc.ModalBody("The user ID you entered is not correct for the Stemming. Please go back to Home and fill in your user ID again."),
            ],
            id="wrong-userid_stemming-modal",
            is_open=False,
        )
        ]),

    # Submit button
    dbc.Row(dbc.Col(dbc.Button('Submit', id='submit_stemming-button', n_clicks=0, color='primary', className="mt-3"), width=12))],

)


