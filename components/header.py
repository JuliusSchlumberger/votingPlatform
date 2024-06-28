from dash import dcc, html
import dash_bootstrap_components as dbc


# Define the header with an additional modal for the glossary
header = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Bepalen methode voor betaalbaarheid op de Nieuwelaan", className="ms-2"),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
                ],
                className="ms-auto",
                navbar=True
            ),
            id="navbar-collapse",
            navbar=True,
        ),
    ]),
    color="primary",
    dark=True,
    className="mb-4"
)
