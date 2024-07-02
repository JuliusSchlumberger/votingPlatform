import dash_bootstrap_components as dbc
from dash import dcc, html
from components import content, header

from callbacks import update_dropdowns_stemming, update_dropdowns_peiling, verify_user_id, submit_responses_peiling, submit_responses_stemming

from dashapp import app

server = app.server
# Define the layout of the app with four sections
app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='stored-user-id', storage_type='session', data={}),  # Using session storage
    header.header,
    content.content,
    html.Div(id='unique-id', style={'display': 'none'}),


], fluid=True, style={'max-height': '100vh', 'overflow': 'scroll'})


if __name__ == '__main__':
    app.run_server(debug=True)