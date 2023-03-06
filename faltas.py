import pandas as pd
import plotly.graph_objects as go
from funcdetratamento import tratar_dataframe


def update_graph_anti_jogo(year, clubes):
    global x_values1
    time_f = clubes
    df = pd.read_csv('Data/campeonato-brasileiro-estatisticas-full.csv')

    if year == '2017':

        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 5746) & (df['partida_id'] < 6126)]
        dfr = tratar_dataframe(dfa)

        x_values1 = dfa['rodata']
    elif year == '2018':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 6126) & (df['partida_id'] < 6506)]
        dfr = tratar_dataframe(dfa)

        x_values1 = dfa['rodata']

    elif year == '2019':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 6506) & (df['partida_id'] < 6886)]
        dfr = tratar_dataframe(dfa)

        x_values1 = dfa['rodata']

    elif year == '2020':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 6886) & (df['partida_id'] < 7266)]
        dfr = tratar_dataframe(dfa)

        x_values1 = dfa['rodata']

    elif year == '2021':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 7266) & (df['partida_id'] < 7646)]
        dfr = tratar_dataframe(dfa)

        x_values1 = dfa['rodata']

    elif year == '2022':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 7646)]
        dfr = tratar_dataframe(dfa)

        x_values1 = dfa['rodata']

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=x_values1,
            y=dfr['faltas'],
            name='Faltas',
            text=dfa['faltas'],
            hovertemplate='Faltas: %{text}',
            marker=dict(color='blue')

        )
    )
    fig.add_trace(
        go.Bar(x=x_values1,
               y=dfr['cartao_amarelo'],
               name='Cartões Amarelo',
               text=dfa['cartao_amarelo'],
               hovertemplate='Cartões Amarelo: %{text}',
               marker=dict(color='yellow')),

    )

    fig.add_trace(
        go.Bar(x=x_values1,
               y=dfr['cartao_vermelho'],
               name='Cartões Vermelho',
               text=dfa['cartao_vermelho'],

               hovertemplate='Cartões Vermelho: %{text}',
               marker=dict(color='red')
               )
    )

    fig.update_layout(
        barmode='group',
        title='Faltas vs Cartões',

        template='plotly_dark', paper_bgcolor='rgba(0, 0, 0, 0)',

        # xaxis_title='Partidas',
        # yaxis_title='Quantidade',
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis=dict(
            title='Rodadas',
            tickmode='array',
            tickvals=x_values1,
            ticktext=[str(i) for i in x_values1]
        ),
        yaxis=dict(title='Quantidade')

    )

    return fig
