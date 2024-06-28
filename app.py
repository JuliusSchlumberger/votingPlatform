
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, ClientsideFunction, callback_context
from components import content, header
# # from callbacks import toggle_tabs
# import dash
from callbacks import update_dropdowns_stemming, update_dropdowns_peiling, handle_submission_peiling, handle_submission_stemming, verify_user_id

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



# app.clientside_callback(
#     """
#     function(data) {
#         return data;
#     }
#     """,
#     Output('output-component', 'children'),  # Change this to your target output
#     Input('viewport-size', 'data')
# )
#
#
#
# @app.callback(
#     Output('dummy-div', 'children'),  # Dummy output, not used
#     Input('viewport-size', 'data')
# )
# def print_viewport_sizes(data):
#     if data is not None:
#         vh_in_pixels = data['vh']
#         vw_in_pixels = data['vw']
#         print(f"Viewport Height: {vh_in_pixels} pixels, Viewport Width: {vw_in_pixels} pixels")
#     else:
#         print("called but empty")
#     return None  # Dummy return, as the output is not visible or used
#

# # Clientside function to capture viewport size
# clientside_callback(
#     """
#     function(trigger) {
#         return JSON.stringify({
#             width: window.innerWidth,
#             height: window.innerHeight
#         });
#     }
#     """,
#     Output('viewport-size', 'data'),
#     Input('viewport-size', 'n_intervals')
# )
#
# @app.callback(
#     Output('dynamic-figure', 'figure'),
#     Input('viewport-size', 'data')
# )
# def update_figure(viewport_data):
#     if viewport_data:
#         size = json.loads(viewport_data)
#         width, height = size['width'], size['height']
#         # Adjust figure dimensions based on the viewport size
#         fig = go.Figure(data=[go.Bar(x=["A", "B", "C"], y=[1, 3, 2])])
#         fig.update_layout(width=width*0.8, height=height*0.8)  # Example scaling
#         return fig
#     return go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)