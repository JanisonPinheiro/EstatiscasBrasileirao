import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.scripts.config.serve_locally = True
server = app.server

