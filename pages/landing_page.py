import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

# Define the modal for invalid user IDs
invalid_user_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Invalid User ID")),
        dbc.ModalBody("The user ID you entered is not correct. Please try again."),
        dbc.ModalFooter(
            dbc.Button("Close", id="close-invalid_userid-modal", className="ms-auto", n_clicks=0)
        ),
    ],
    id="invalid_userid-modal",
    is_open=False,
)

visualization = dbc.Container([
    dbc.Row([
        dbc.Col(html.Img(id='introduction-image', src='assets/NWL_foto.jpeg', className='mx-auto'), width=3),
        dbc.Col([
            html.P("De statuten van onze woonvereniging De Oude Nieuwelaan bepalen dat we om de 15 jaar vast moeten "
                   "stellen in welke mate ieder lid en oud lid gerechtigd is in het totale opgebouwde vermogen van de "
                   "vereniging en of de leden en oudleden een uitkering kunnen krijgen uit dit opgebouwd vermogen. "
                   "Hierbij dient in acht te worden genomen dat de betaalbaarheid van het wonen gewaarborgd blijft. "
                   "Het uitkeringsbedrag bestaat uit het geld in de "
                   "algemene reserve, vermeerderd met een extra lening (artikel 8 lid 5). In feite bepaalt de hoogte van een (nog) "
                   "betaalbare contributie dus hoeveel we kunnen herfinancieren en daarmee ook hoeveel van ons "
                   "vermogen we uit kunnen keren (hoe meer contributie we betalen, hoe meer we kunnen besteden aan een nieuwe lening)."),
            html.P("Het begrip betaalbaarheid wordt in de statuten niet verder gespecificeerd, wat ons nu voor de taak "
                   "stelt om duidelijke criteria en methodes te ontwikkelen voor het bepalen van wat als betaalbaar "
                   "wonen geldt. Echter, er is geen expliciete richtlijn over hoe we de hoogte van de contributie moeten handhaven dat het "
                   "betaalbaarheid blijvt, wat ons de ruimte en verplichting geeft om een methode te vinden die wij "
                   "objectief en eerlijk vinden."),
        ], width=9)
    ]),
    dbc.Row([
        dbc.Col(html.Div([
            html.P("Het lijkt ons dat een methode aan de volgende criteria "
                   "zou moeten voldoen:"),
            html.Ul([
                html.Li([html.B("Eenduidig. "),
                         "Wij bedoelen daarmee dat de uitkomst voor iedereen hetzelfde is en er geen discussie over de "
                         "toepassing van de methode en de uitkomst daarvan kan ontstaan."]),
                html.Li([html.B("Controleerbaar. "),
                         "De gebruikte data moet traceerbaar zijn. Data moet ook het liefst makkelijk verkrijgbaar zijn, "
                         "ook als je bijvoorbeeld een paar jaar later nog wilt controleren."]),
                html.Li([html.B("Algemeen aanvaard.")]),
                html.Li([html.B("Toekomstbestendig. "),
                         "Zeker weten doe je het nooit, maar we vinden dat er een methode gekozen moet worden waarvan "
                         "verwacht mag worden dat je deze over 15 en 30 jaar opnieuw toe kunt passen."])
            ]),
            html.P(
                "Met deze pagina gaan we een peiling doen voor oud-leden en aspirant-leden om hun inschatting als extra context mee te nemen in de stemming. "
                "Huidige leden stemmen met deze pagina op 18 juli 2024 over welke methode wij willen gebruiken om betaalbaarheid op de Nieuwelaan te bepalen."),
            html.B(html.P(
                "Vul je unieke code in die je per e-mail is toegestuurd om toegang te krijgen tot de peiling (oud-leden en aspirant-leden) of de stemming (leden).")),
            dbc.Input(id='user-id', placeholder='Enter your user ID', type='text', className='mb-3'),
        ]), width=12),]),
    # Submit button
    dbc.Row([
        dbc.Col([], width=2),
        dbc.Col(dbc.Button('Start', id='submit_userid-button', n_clicks=0, color='primary', className="mt-3"), width=12),
        dbc.Col([], width=2)],
        ),
    invalid_user_modal

        ])


layout = dbc.Container([
    dcc.Location(id='url', refresh=True),  # This component tracks the URL
    # html.Div(id='stored-user-id', style={'display': 'none'}),

    # Introduction section
    visualization
], fluid=False)

