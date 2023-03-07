import pandas as pd
import plotly.graph_objects as go

from funcdetratamento import tratar_dataframe


def update_graph(year, clubes):
    global x_values # Responsável para que possa colocar o valor correto em cada partida, já que nem todas partidas
    # são na ordem númerica correta

    time_f = clubes
    df = pd.read_csv('Data/campeonato-brasileiro-estatisticas-full.csv')

    if year == '2017':

        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 5746) & (df['partida_id'] < 6126)]
        dfr = tratar_dataframe(dfa)

        x_values = dfa['rodata']
    elif year == '2018':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 6126) & (df['partida_id'] < 6506)]
        dfr = tratar_dataframe(dfa)

        x_values = dfa['rodata']

    elif year == '2019':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 6506) & (df['partida_id'] < 6886)]
        dfr = tratar_dataframe(dfa)

        x_values = dfa['rodata']

    elif year == '2020':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 6886) & (df['partida_id'] < 7266)]
        dfr = tratar_dataframe(dfa)

        x_values = dfa['rodata']

    elif year == '2021':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 7266) & (df['partida_id'] < 7646)]
        dfr = tratar_dataframe(dfa)

        x_values = dfa['rodata']

    elif year == '2022':
        dfa = df.loc[(df['clube'] == time_f) & (df['partida_id'] >= 7646) ]
        dfr = tratar_dataframe(dfa)

        x_values = dfa['rodata']

    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=x_values,
               y=dfr['chutes_no_alvo'],
               name='Chutes no Alvo',
               text=dfa['chutes_no_alvo'],

               hovertemplate='Chutes no Alvo: %{text}',
               marker=dict(color='blue')
               )
    )

    fig.add_trace(
        go.Bar(x=x_values,
               y=dfr['chutes'],
               name='Chutes',
               text=dfa['chutes'],
               hovertemplate='Chutes: %{text}',
               hoverlabel=dict(font=dict(color='white')),
               marker=dict(color='red'))
    )

    fig.update_layout(
        barmode='group',
        title='Chutes no Alvo vs Chutes',

        template='plotly_dark', paper_bgcolor='rgba(0, 0, 0, 0)',

        # xaxis_title='Partidas',
        # yaxis_title='Quantidade',
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis=dict(
            title='Rodadas',
            tickmode='array',  # especifica que  os valores dos ticks foi definido manualmente
            tickvals=x_values,  # valores dos ticks para o eixo x
            ticktext=[str(i) for i in x_values]  # texto dos ticks para o eixo x
        ),
        yaxis=dict(title='Quantidade de Chutes')

    )

    return fig
