import plotly.express as px

from dash import html, dcc
from dash.dependencies import Input, Output
import dash
import dash_bootstrap_components as dbc

from shots_ import *
from fouls_ import *
from goals_ import *


def create_app():
    my_app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG], assets_folder='assets')

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

            dcc.RadioItems(id='clubs',
                           options=[
                               {'label': 'Athletico-PR', 'value': 'Athletico-PR'},
                               {'label': 'Atletico-GO', 'value': 'Atletico-GO'},
                               {'label': 'Atletico-MG', 'value': 'Atletico-MG'},
                               {'label': 'Avai', 'value': 'Avai'},
                               {'label': 'Bahia', 'value': 'Bahia'},
                               {'label': 'Botafogo', 'value': 'Botafogo-RJ'},
                               {'label': 'Bragantino', 'value': 'Bragantino'},
                               {'label': 'Ceara', 'value': 'Ceara'},
                               {'label': 'Chapecoense', 'value': 'Chapecoense'},
                               {'label': 'Corinthians', 'value': 'Corinthians'},
                               {'label': 'Cruzeiro', 'value': 'Cruzeiro'},
                               {'label': 'Flamengo', 'value': 'Flamengo'},
                               {'label': 'Fluminense', 'value': 'Fluminense'},
                               {'label': 'Fortaleza', 'value': 'Fortaleza'},
                               {'label': 'Goias', 'value': 'Goias'},
                               {'label': 'Gremio', 'value': 'Gremio'},
                               {'label': 'Internacional', 'value': 'Internacional'},
                               {'label': 'Palmeiras', 'value': 'Palmeiras'},
                               {'label': 'Santos', 'value': 'Santos'},
                               {'label': 'Sao Paulo', 'value': 'Sao Paulo'},
                               {'label': 'Sport', 'value': 'Sport'},
                               {'label': 'Vasco', 'value': 'Vasco'}

                           ],
                           value='Flamengo', labelStyle={'display': 'flex', 'margin-right': '10px'},
                           inputStyle={'margin-right': '10px'}
                           )
        ], style=style_sidebar
    )

    my_app.layout = html.Div([
        dbc.Row([
            dbc.Col(layout_sidebar, md=2),
            dbc.Col([
                html.H5('Estatísticas dos últimos 5 anos da Séria A do Campeonato Brasileiro de Futebol'),
                html.Div('Escolha uma opção de ano:'),
                dcc.Dropdown(id='dropdown',
                             options=[{'label': 'Chute no Gol vs Chutes', 'value': 'shots'},
                                      {'label': 'Faltas vs Cartões', 'value': 'fouls'},
                                      {'label': 'Gols Feitos Vs Gols Tomados', 'value': 'goals'}
                                      ],
                             value='shots',
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
                                children=html.Img(
                                    src='https://live.staticflickr.com/65535/52731851812_b9a309d444_o.png',

                                    alt='linkedin',
                                    style={'margin-right': '10px'}
                                    ),
                                href='https://www.linkedin.com/in/jan%C3%ADson-pinheiro-b20a92237/',
                                target='_bank'),

                            html.A(
                                href='https://www.instagram.com/janisonpinheiro/',
                                target='_bank',
                                children=html.Img(
                                    src='https://live.staticflickr.com/65535/52731869012_3febae232d_o.png',

                                    alt='instagram',
                                    style={'margin-right': '10px'}
                                    ),
                            ),
                            html.A(
                                href='https://github.com/JanisonPinheiro/',
                                target='_bank',
                                children=html.Img(
                                    src='https://live.staticflickr.com/65535/52732785625_c4629a07b4_o.png',

                                    alt='git hub',
                                    style={'margin-right': '10px'}),
                            ),
                            # html.P('Informação 2', style={'text-align': 'center'})
                        ], style={'text-align': 'center'})
                    ], )
                )

            ], md=10),

        ])
    ])

    @my_app.callback(Output('grafico', 'figure'),
                     [Input('dropdown', 'value'),
                      Input('year', 'value'),
                      Input('clubs', 'value')
                      ])
    def update_figure(value, year, clubs):
        if value == 'shots':
            return update_graph(year, clubs)
        elif value == 'fouls':
            return update_graph_anti_jogo(year, clubs)
        elif value == 'goals':
            return update_graph_goals(year, clubs)

    my_app.scripts.config.serve_locally = True
    server = my_app.server
    if __name__ == '__main__':
        my_app.run_server(debug=True)

    return server


app = create_app()

