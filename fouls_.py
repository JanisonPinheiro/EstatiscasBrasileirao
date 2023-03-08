import pandas as pd
import plotly.graph_objects as go
from handling_function import handle_dataframe


def update_graph_anti_jogo(year, clubs):
    global x_values1

    df = pd.read_csv('Data/campeonato-brasileiro-estatisticas-full.csv')

    if year == '2017':

        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 5746) & (df['partida_id'] < 6126)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values1 = df_filtered_by_year['rodata']
    elif year == '2018':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 6126) & (df['partida_id'] < 6506)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values1 = df_filtered_by_year['rodata']

    elif year == '2019':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 6506) & (df['partida_id'] < 6886)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values1 = df_filtered_by_year['rodata']

    elif year == '2020':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 6886) & (df['partida_id'] < 7266)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values1 = df_filtered_by_year['rodata']

    elif year == '2021':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 7266) & (df['partida_id'] < 7646)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values1 = df_filtered_by_year['rodata']

    elif year == '2022':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 7646)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values1 = df_filtered_by_year['rodata']

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=x_values1,
            y=df_filtered_by_year_t['faltas'],
            name='Faltas',
            text=df_filtered_by_year['faltas'],
            hovertemplate='Faltas: %{text}',
            marker=dict(color='blue')

        )
    )
    fig.add_trace(
        go.Bar(x=x_values1,
               y=df_filtered_by_year_t['cartao_amarelo'],
               name='Cartões Amarelo',
               text=df_filtered_by_year['cartao_amarelo'],
               hovertemplate='Cartões Amarelo: %{text}',
               marker=dict(color='yellow')),

    )

    fig.add_trace(
        go.Bar(x=x_values1,
               y=df_filtered_by_year_t['cartao_vermelho'],
               name='Cartões Vermelho',
               text=df_filtered_by_year['cartao_vermelho'],

               hovertemplate='Cartões Vermelho: %{text}',
               marker=dict(color='red')
               )
    )

    fig.update_layout(
        barmode='group',
        title='Faltas vs Cartões',

        template='plotly_dark', paper_bgcolor='rgba(0, 0, 0, 0)',

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
