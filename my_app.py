import dash
import dash_bootstrap_components as dbc

my_app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

my_app.scripts.config.serve_locally = True
server = my_app.server

