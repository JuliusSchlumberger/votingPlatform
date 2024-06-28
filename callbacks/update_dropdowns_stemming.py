from dash import  Input, Output, State, callback_context
from dashapp import app

from assets.static_inputs import CANDIDATES

@app.callback(
    [Output(f'dropdown_stemming-{i}', 'options') for i in range(len(CANDIDATES))],
    [Input(f'dropdown_stemming-{i}', 'value') for i in range(len(CANDIDATES))],
    [State(f'dropdown_stemming-{i}', 'value') for i in range(len(CANDIDATES))]
)
def update_dropdown_stemming_options(*values):
    selected_values = values[:len(CANDIDATES)]
    ctx = callback_context
    if not ctx.triggered:
        return [[{'label': candidate, 'value': candidate} for candidate in CANDIDATES] for _ in range(len(CANDIDATES))]

    available_options = [candidate for candidate in CANDIDATES if candidate not in selected_values]

    updated_options = []
    for i in range(len(CANDIDATES)):
        if selected_values[i] is None:
            updated_options.append([{'label': candidate, 'value': candidate} for candidate in available_options])
        else:
            updated_options.append([{'label': selected_values[i], 'value': selected_values[i]}] + [{'label': candidate, 'value': candidate} for candidate in available_options])
    return updated_options

