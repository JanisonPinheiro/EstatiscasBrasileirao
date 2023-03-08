import pandas as pd
import plotly.graph_objects as go

from handling_function import handle_dataframe


def update_graph(year, clubs):
    global x_values # Responsible for ensuring that the correct value is assigned to each match, as not all matches
    # occur in the correct numerical order, and there may be postponements and rescheduling. Therefore, for example,
    # round 3 may occur before round 2. With this treatment, even if round 2 occurred after round 3, the chart will
    # be rearranged so that the data for each round is in the correct index

    df = pd.read_csv('Data/campeonato-brasileiro-estatisticas-full.csv')

    if year == '2017':

        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 5746) & (df['partida_id'] < 6126)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values = df_filtered_by_year['rodata']
    elif year == '2018':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 6126) & (df['partida_id'] < 6506)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values = df_filtered_by_year['rodata']

    elif year == '2019':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 6506) & (df['partida_id'] < 6886)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values = df_filtered_by_year['rodata']

    elif year == '2020':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 6886) & (df['partida_id'] < 7266)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values = df_filtered_by_year['rodata']

    elif year == '2021':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 7266) & (df['partida_id'] < 7646)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values = df_filtered_by_year['rodata']

    elif year == '2022':
        df_filtered_by_year = df.loc[(df['clube'] == clubs) & (df['partida_id'] >= 7646)]
        df_filtered_by_year_t = handle_dataframe(df_filtered_by_year)

        x_values = df_filtered_by_year['rodata']

    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=x_values,
               y=df_filtered_by_year_t['chutes_no_alvo'],
               name='Chutes no Alvo',
               text=df_filtered_by_year['chutes_no_alvo'],

               hovertemplate='Chutes no Alvo: %{text}',
               marker=dict(color='blue')
               )
    )

    fig.add_trace(
        go.Bar(x=x_values,
               y=df_filtered_by_year_t['chutes'],
               name='Chutes',
               text=df_filtered_by_year['chutes'],
               hovertemplate='Chutes: %{text}',
               hoverlabel=dict(font=dict(color='white')),
               marker=dict(color='red'))
    )

    fig.update_layout(
        barmode='group',
        title='Chutes no Alvo vs Chutes',

        template='plotly_dark', paper_bgcolor='rgba(0, 0, 0, 0)',


        margin=dict(l=50, r=50, t=50, b=50),
        xaxis=dict(
            title='Rodadas',
            tickmode='array',  # Specifies that the tick values have been manually defined
            tickvals=x_values,  # Tick values for the x-axis
            ticktext=[str(i) for i in x_values]  # Text for the ticks on the x-axis
        ),
        yaxis=dict(title='Quantidade de Chutes')

    )

    return fig
