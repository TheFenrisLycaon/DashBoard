from dash import Dash, html


def create_layout(app: Dash) -> html.Div:

    return html.Div(
        className="app-div",
        children=[
            html.H1("Finances"),
            html.Hr(),
        ],
    )
