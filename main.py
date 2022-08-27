from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layouts import create_layout


def main() -> None:
    """Main Function"""
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()
