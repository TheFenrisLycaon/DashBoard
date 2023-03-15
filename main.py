from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layouts import create_layout
from src.data.data_loader import load_transactions

PATH = "./Data/transactions.csv"


def main() -> None:
    """Main Function"""
    data = load_transactions(PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
