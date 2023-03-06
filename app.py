#import dash
#import dash_bootstrap_components as dbc

#app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

#app.scripts.config.serve_locally = True
server = app.server

import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output


from chutes import *
from faltas import *
from gols_pro_contra import *
import dash

import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.scripts.config.serve_locally = True
server = app.server

px.defaults.template = 'plotly_dark'

fig = go.Figure()

style_sidebar = style = {
    'margin-left': '0',
    'margin': '0',
    'padding': '10px',
    'height': '100vh', }

layout_sidebar = dbc.Card(
    [
        html.H2('Clubes', style={'font-family': 'Voltaire', 'font-size': '20px', 'textAlign': 'center'}),
        html.Hr(),

        dcc.RadioItems(id='clubes',
                       options=[
                           {'label': 'Flamengo', 'value': 'Flamengo'},
                           {'label': 'Santos', 'value': 'Santos'},
                           {'label': 'Palmeiras', 'value': 'Palmeiras'},
                           {'label': 'Cruzeiro', 'value': 'Cruzeiro'},
                           {'label': 'Athletico-PR	', 'value': 'Athletico-PR'},

                           {'label': 'Sport', 'value': 'Sport'},
                           {'label': 'Avai', 'value': 'Avai'},
                           {'label': 'Atletico-MG', 'value': 'Atletico-MG'},
                           {'label': 'Goias', 'value': 'Goias'},
                           {'label': 'Sao Paulo', 'value': 'Sao Paulo'},
                           {'label': 'Vasco', 'value': 'Vasco'},
                           {'label': 'Chapecoense', 'value': 'Chapecoense'},
                           {'label': 'Atletico-GO', 'value': 'Atletico-GO'},
                           {'label': 'Internacional', 'value': 'Internacional'},
                           {'label': 'Gremio', 'value': 'Gremio'},
                           {'label': 'Bragantino', 'value': 'Bragantino'},
                           {'label': 'Bahia', 'value': 'Bahia'},
                           {'label': 'Ceara', 'value': 'Ceara'},
                           {'label': 'Botafogo', 'value': 'Botafogo-RJ'},
                           {'label': 'Fortaleza', 'value': 'Fortaleza'},
                           {'label': 'Corinthians', 'value': 'Corinthians'},
                           {'label': 'Fluminense', 'value': 'Fluminense'},

                       ],
                       value='Flamengo', labelStyle={'display': 'flex', 'margin-right': '10px'},
                       inputStyle={'margin-right': '10px'}
                       )
    ], style=style_sidebar
)

app.layout = html.Div([
    dbc.Row([
        dbc.Col(layout_sidebar, md=2),
        dbc.Col([
            html.H5('Estatísticas dos últimos 5 anos da Séria A do Campeonato Brasileiro de Futebol'),
            html.Div('Escolha uma opção de ano:'),
            dcc.Dropdown(id='dropdown',
                         options=[{'label': 'Chute no Gol vs Chutes', 'value': 'chutegol_fora'},
                                  {'label': 'Faltas vs Cartões', 'value': 'faltas_cartoes'},
                                  {'label': 'Gols Feitos Vs Gols Tomados', 'value': 'gols'}
                                  ],
                         value='chutegol_fora',
                         style={'float': 'right',
                                'width': '50%',
                                'margin-right': '10px',

                                },
                         className='bg-darkbg-dark text-light'
                         ),

            dcc.RadioItems(id='year',
                           options=[{'label': '2017', 'value': '2017'},
                                    {'label': '2018', 'value': '2018'},
                                    {'label': '2019', 'value': '2019'},
                                    {'label': '2020', 'value': '2020'},
                                    {'label': '2021', 'value': '2021'},
                                    {'label': '2022', 'value': '2022'}

                                    ], value='2017', labelStyle={'display': 'inline-block', 'margin-right': '20px'},
                           inputStyle={'margin-right': '5px'},

                           style={'display': 'flex', 'justify-content': 'flex-start'}),
            html.Hr(),  # cria um espaço
            dcc.Graph(
                id='grafico',
                figure=fig,

            ),
            html.Hr(),
            dbc.Col(

                html.Footer([

                    html.Div([
                        html.P('Produzido por Janíson Pinheiro'),
                        html.A(
                            href='https://www.linkedin.com/in/jan%C3%ADson-pinheiro-b20a92237/',
                            target='_bank',
                            children=html.Img(src='/assets/linkedin.png',

                                              alt='Janíson Pinheiro',
                                              style={'margin-right': '10px'}
                                              )

                        ),

                        html.A(
                            href='https://www.instagram.com/janisonpinheiro/',
                            target='_bank',
                            children=html.Img(src='/assets/instagram.svg',

                                              alt='Janíson Pinheiro',
                                              style={'margin-right': '10px'}
                                              ),
                        ),
                        html.A(
                            href='https://github.com/JanisonPinheiro/',
                            target='_bank',
                            children=html.Img(src='/assets/git.jpg',

                                              alt='Janíson Pinheiro',
                                              style={'margin-right': '10px'}),
                        ),
                        # html.P('Informação 2', style={'text-align': 'center'})
                    ], style={'text-align': 'center'})
                ], )
            )

        ], md=10),

    ])
])


@app.callback(Output('grafico', 'figure'),
              [Input('dropdown', 'value'),
               Input('year', 'value'),
               Input('clubes', 'value')
               ])
def update_figure(value, year, clubes):
    if value == 'chutegol_fora':
        return update_graph(year, clubes)
    elif value == 'faltas_cartoes':
        return update_graph_anti_jogo(year, clubes)
    elif value == 'gols':
        return update_graph_gols(year, clubes)


if __name__ == "__main__":
    app.run_server(port=8050, debug=False)

