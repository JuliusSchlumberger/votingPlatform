from dash import  Input, Output, State, callback_context
from dashapp import app

from assets.static_inputs import CANDIDATES

@app.callback(
    [Output(f'dropdown_peiling-{i}', 'options') for i in range(5)],
    [Input(f'dropdown_peiling-{i}', 'value') for i in range(5)],
    [State(f'dropdown_peiling-{i}', 'value') for i in range(5)]
)
def update_dropdown_peiling_options(*values):
    selected_values = values[:5]
    ctx = callback_context

    available_options = [candidate for candidate in CANDIDATES if candidate not in selected_values]

    updated_options = []
    for i in range(5):
        if selected_values[i] is None:
            updated_options.append([{'label': candidate, 'value': candidate} for candidate in available_options])
        else:
            updated_options.append(
                [{'label': selected_values[i], 'value': selected_values[i]}] +
                [{'label': candidate, 'value': candidate} for candidate in available_options]
            )
    return updated_options