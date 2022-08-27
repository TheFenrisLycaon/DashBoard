from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash) -> html.Div:
    all_years: list[str] = ["2020", "2021", "2022", "2023"]
    unique_years: list[str] = sorted(set(all_years), key=int)

    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
    )
    def select_all_years(_: int) -> list[str]:
        return all_years

    return html.Div(
        children=[
            html.H6("Select Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in all_years],
                value=all_years,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_YEARS_BUTTON,
            ),
        ]
    )
