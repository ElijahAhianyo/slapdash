"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances.
"""

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from .components import make_brand, make_navbar


def main_layout_header():
    """Dash layout with a top-header"""
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(make_brand(), width="auto"),
                    dbc.Col(make_navbar(vertical=False), width="auto"),
                ],
                id="header",
                className="bg-dark justify-content-between align-items-center",
            ),
            dbc.Container(dbc.Row(dbc.Col(dash.page_container)), fluid=True),
        ]
    )


def main_layout_sidebar():
    """Dash layout with a sidebar"""
    return html.Div(
        [
            dbc.Container(
                fluid=True,
                children=dbc.Row(
                    [
                        dbc.Col(
                            [make_brand(), make_navbar(vertical=True)],
                            width=2,
                            className="px-0 bg-dark",
                            style={"height": "100vh"},
                            id="sidebar",
                        ),
                        dbc.Col(dash.page_container, width=10),
                    ]
                ),
            ),
        ]
    )
