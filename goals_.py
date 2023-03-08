import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def update_graph_goals(year, clubs):

    home_goals = 0
    away_goals = 0
    away_goals_conceded = 0
    home_goals_conceded = 0

    df_goals = pd.read_csv('Data/campeonato-brasileiro-full.csv')

    if year == '2017':
        df_filtered_by_year = df_goals.loc[
            ((df_goals['mandante'] == clubs) | (df_goals['visitante'] == clubs)) & (df_goals['ID'] >= 5746) & (
                    df_goals['ID'] < 6126)]

        # 'Gols pró' refers to the number of goals scored by the team. If the team is the home team, the 'gols pró'
        # can be found in the 'placar_Mandante' column. If the team is the away team, the 'gols pró' can be found in
        # the 'placar_Visitante' column. The opposite of that is the number of goals that the team conceded.
        home_games = df_filtered_by_year[df_filtered_by_year['mandante'] == clubs]
        home_goals += home_games['mandante_Placar'].sum()
        home_goals_conceded += home_games['visitante_Placar'].sum()
        away_games = df_filtered_by_year[df_filtered_by_year['visitante'] == clubs]
        away_goals += away_games['visitante_Placar'].sum()
        away_goals_conceded += away_games['mandante_Placar'].sum()
    elif year == '2018':

        df_filtered_by_year = df_goals.loc[
            ((df_goals['mandante'] == clubs) | (df_goals['visitante'] == clubs)) & (df_goals['ID'] >= 6126) & (
                    df_goals['ID'] < 6506)]
        home_games = df_filtered_by_year[df_filtered_by_year['mandante'] == clubs]
        home_goals += home_games['mandante_Placar'].sum()
        home_goals_conceded += home_games['visitante_Placar'].sum()
        away_games = df_filtered_by_year[df_filtered_by_year['visitante'] == clubs]
        away_goals += away_games['visitante_Placar'].sum()
        away_goals_conceded += away_games['mandante_Placar'].sum()

    elif year == '2019':
        df_filtered_by_year = df_goals.loc[
            ((df_goals['mandante'] == clubs) | (df_goals['visitante'] == clubs)) & (df_goals['ID'] >= 6506) & (
                    df_goals['ID'] < 6886)]

        home_games = df_filtered_by_year[df_filtered_by_year['mandante'] == clubs]
        home_goals += home_games['mandante_Placar'].sum()
        home_goals_conceded += home_games['visitante_Placar'].sum()

        away_games = df_filtered_by_year[df_filtered_by_year['visitante'] == clubs]
        away_goals += away_games['visitante_Placar'].sum()
        away_goals_conceded += away_games['mandante_Placar'].sum()

    elif year == '2020':
        df_filtered_by_year = df_goals.loc[
            ((df_goals['mandante'] == clubs) | (df_goals['visitante'] == clubs)) & (df_goals['ID'] >= 6886) &
            (df_goals['ID'] < 7266)]

        home_games = df_filtered_by_year[df_filtered_by_year['mandante'] == clubs]
        home_goals += home_games['mandante_Placar'].sum()
        home_goals_conceded += home_games['visitante_Placar'].sum()
        away_games = df_filtered_by_year[df_filtered_by_year['visitante'] == clubs]
        away_goals += away_games['visitante_Placar'].sum()
        away_goals_conceded += away_games['mandante_Placar'].sum()

    elif year == '2021':

        df_filtered_by_year = df_goals.loc[
            ((df_goals['mandante'] == clubs) | (df_goals['visitante'] == clubs)) &
            (df_goals['ID'] >= 7266) & (df_goals['ID'] < 7646)]
        home_games = df_filtered_by_year[df_filtered_by_year['mandante'] == clubs]
        home_goals += home_games['mandante_Placar'].sum()
        home_goals_conceded += home_games['visitante_Placar'].sum()
        away_games = df_filtered_by_year[df_filtered_by_year['visitante'] == clubs]
        away_goals += away_games['visitante_Placar'].sum()
        away_goals_conceded += away_games['mandante_Placar'].sum()

    elif year == '2022':
        df_filtered_by_year = df_goals.loc[
            ((df_goals['mandante'] == clubs) | (df_goals['visitante'] == clubs)) & (df_goals['ID'] >= 7646)]

        home_games = df_filtered_by_year[df_filtered_by_year['mandante'] == clubs]
        home_goals += home_games['mandante_Placar'].sum()
        home_goals_conceded += home_games['visitante_Placar'].sum()
        away_games = df_filtered_by_year[df_filtered_by_year['visitante'] == clubs]
        away_goals += away_games['visitante_Placar'].sum()
        away_goals_conceded += away_games['mandante_Placar'].sum()

    values_ = [home_goals, away_goals]
    values_1 = [home_goals_conceded, away_goals_conceded]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'pie'}, {'type': 'pie'}]])

    fig.add_trace(go.Pie(labels=['Gols como Mandante', 'Gols como Visitante'], values=values_, name=''),
                  row=1, col=1
                  )
    fig.add_trace(go.Pie(labels=['Gols Tomados como Mandante', 'Gols tomados como Visitante'], values=values_1,
                         name=''), row=1, col=2)

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(17, 17, 17)',
        title='Gols Feitos vs Gols Tomados',
        grid=dict(rows=1, columns=2),
        annotations=[
            dict(text='Gols Pró', x=0.20, y=0.5, font_size=16, showarrow=False, ),
            dict(text='Gols Contra', x=0.80, y=0.5, font_size=16, showarrow=False, )
        ]

    )
    fig.update_traces(textfont=dict(color='black'),
                      hoverlabel=dict(font=dict(color='white')))

    return fig
