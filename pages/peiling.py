import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from assets.static_inputs import CANDIDATES, INTRODUCTION


dash.register_page(__name__, path='/peiling')

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
    dbc.Row(dbc.Col(html.H3("Introduction", className="text-success"), width=12), className="mt-3"),
    dbc.Row(dbc.Col(INTRODUCTION,
                    width=12), className="mb-3 "),

    # Question 1 section
    html.Div(id="peiling-1", children=[
        dbc.Row(dbc.Col(html.H3("When did you start living at the Nieuwelaan?", className="text-success"),
                        width=12), className="mt-3"),
        dbc.Row(dbc.Col(dcc.Dropdown(
            id='peiling-q1',
            options=[
                {'label': 'before 01/01/2012', 'value': 'before 01/01/2012'},
                {'label': 'between 01/01/2012 and 01/01/2019', 'value': 'between 01/01/2012 and 01/01/2019'},
                {'label': 'after 01/01/2019', 'value': 'after 01/01/2019'}
            ],
            placeholder='Select an option',
            className="mb-3"
        ), width=12)),
    ]),


    # Question 3 section with dropdowns
    html.Div(id="peiling-3", children=[
        dbc.Row(dbc.Col(html.H3("Which method do you find most appropriate for the Nieuwelaan?", className="text-success"), width=12),
                className="mt-3"),
        dbc.Row(
            dbc.Col(html.P("Please give the top 5 methods you find most appropriate for the Nieuwelaan. Rank them in order of your preference. "),
                    width=12)),

        *[dbc.Row(dbc.Col(dcc.Dropdown(
            id=f'dropdown_peiling-{i}',
            options=[{'label': candidate, 'value': candidate} for candidate in candidates],
            placeholder=f'Choose your {i + 1}{get_choice_suffix(i + 1)} choice'
        ), width=12), className="mb-3") for i in range(5)],
# Modals for pop-up messages
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Incomplete Submission")),
            dbc.ModalBody("Please fill in all the ranks for Question 3 before submitting."),
            # dbc.ModalFooter(
            #     dbc.Button("Close", id="close-incomplete_peiling", className="ms-auto", n_clicks=0)
            # ),
        ],
        id="incomplete-modal_peiling",
        is_open=False,
    ),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Submission Successful")),
            dbc.ModalBody("Your vote has been successfully submitted."),
            # dbc.ModalFooter(
            #     dbc.Button("Close", id="close-success_peiling", className="ms-auto", n_clicks=0)
            # ),
        ],
        id="success-modal_peiling",
        is_open=False,
    ),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Invalid User ID")),
            dbc.ModalBody("The user ID you entered is not correct for this section. Please go back to Home and fill in your userid again."),
            # dbc.ModalFooter(
            #     dbc.Button("Close", id="close-wrong-userid-modal_peiling", className="ms-auto", n_clicks=0)
            # ),
        ],
        id="wrong-userid-modal_peiling",
        is_open=False,
    )
    ]),

# Question 2 section
    html.Div(id="peiling-2", children=[
        dbc.Row(dbc.Col(html.H2("Question 2", className="text-success"), width=12), className="mt-3"),
        dbc.Row(dbc.Col(dcc.Textarea(
            id='peiling-q2',
            placeholder='Is there anything you want to give us on the road for the decision on affordability at the Nieuwelaan?'
                        ' Are there any methods of that that you would strongly advise against?',
            style={'width': '100%', 'height': '100px'},
            className="mb-3 form-control"
        ), width=12)),
    ]),

    # Submit button
    dbc.Row(dbc.Col(dbc.Button('Submit', id='submit-button_peiling', n_clicks=0, color='primary', className="mt-3"), width=12)),

    # Output state
    dbc.Row(dbc.Col(html.Div(id='output-state', className="mt-3 text-info"), width=12))]

)


