import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from assets.static_inputs import CANDIDATES, INTRODUCTION_PEILING


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
    dbc.Row(dbc.Col(html.H3("Peiling", className="text-success"), width=12), className="mt-3"),
    dbc.Row(dbc.Col(INTRODUCTION_PEILING,
                    width=12), className="mb-3 "),

    # # Question 1 section
    # html.Div(id="peiling-1", children=[
    #     dbc.Row(dbc.Col(html.H4("Wanneer ben je op de Nieuwelaan gaan wonen?", className="text-success"),
    #                     width=12), className="mt-3"),
    #     dbc.Row(dbc.Col(dcc.Dropdown(
    #         id='peiling-q1',
    #         options=[
    #             {'label': 'vóór 01/01/2012', 'value': 'vóór 01/01/2012'},
    #             {'label': 'tussen 01/01/2012 en 20/10/2019', 'value': 'tussen 01/01/2012 en 20/10/2019'},
    #             {'label': 'after 01/01/2019', 'value': 'na 01/01/2019'}
    #         ],
    #         placeholder='Kiez een periode',
    #         className="mb-3"
    #     ), width=12)),
    # ]),


    # Question 3 section with dropdowns
    html.Div(id="peiling-3", children=[
        dbc.Row(dbc.Col(html.H4("Welke methoden vindt je het meest geschikt voor de Nieuwelaan?", className="text-success"), width=12),
                className="mt-3"),
        dbc.Row(
            dbc.Col(html.Div(["Geef de top 5 van methoden die je het meest geschikt vindt om de betaalbaarheid voor de Nieuwelaan te bepalen.",
                              html.B(" Rangschik ze wel in volgorde van je voorkeur!"),]
                    ),width=12)),

        *[dbc.Row(dbc.Col(dcc.Dropdown(
            id=f'dropdown_peiling-{i}',
            options=[{'label': candidate, 'value': candidate} for candidate in candidates],
            placeholder=f'Choose your {i + 1}{get_choice_suffix(i + 1)} preference'
        ), width=12), className="mb-3") for i in range(5)],
# Modals for pop-up messages
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Incomplete Submission")),
            dbc.ModalBody("Geef een lijst van 5 methoden (in volgorde van voorkeur voordat je ze indient). Als je geen voorkeur wilt opgeven, houd dan alle drop-downs leeg."),
        ],
        id="incomplete-modal_peiling",
        is_open=False,
    ),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Submission Successful")),
            dbc.ModalBody("Je mening is succesvol ingediend. Bedankt voor het delen van je perspectieven, je kunt dit venster nu sluiten."
                          " Je kunt je invoer aanpassen voor het geval "
                          "je een fout hebt gemaakt en gewoon opnieuw indienen."),
        ],
        id="success-modal_peiling",
        is_open=False,
    ),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Invalid User ID")),
            dbc.ModalBody("De user-ID die je hebt ingevoerd is niet correct voor deze sectie. Ga terug naar Home "
                          "en vul uw gebruikers-ID (die je per e-mail hebt ontvangen) opnieuw in."),
        ],
        id="wrong-userid-modal_peiling",
        is_open=False,
    )
    ]),

# Question 2 section
    html.Div(id="peiling-2", children=[
        dbc.Row(dbc.Col(html.H4("Wat je ons nog mee wilt geven", className="text-success"), width=12), className="mt-3"),
        dbc.Row(dbc.Col(dcc.Textarea(
            id='peiling-q2',
            placeholder='Is er iets dat u ons mee wilt geven op weg naar het besluit over de betaalbaarheid aan de '
                        'Nieuwelaan? Zijn er bijvoorbeeld methodes die je sterk afraadt?',
            style={'width': '100%', 'height': '100px'},
            className="mb-3 form-control"
        ), width=12)),
    ]),

    # Submit button
    dbc.Row(dbc.Col(dbc.Button('Submit', id='submit-button_peiling', n_clicks=0, color='primary', className="mt-3"), width=12)),

    # Output state
    dbc.Row(dbc.Col(html.Div(id='output-state', className="mt-3 text-info"), width=12))]

)


