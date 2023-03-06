import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def update_graph_gols(year, clubes):
    time_f = clubes
    golsfeitosmandante = 0
    golsfeitovisitante = 0
    golstomadov = 0
    golstomadom = 0

    df_gols = pd.read_csv('Data/campeonato-brasileiro-full.csv')

    if year == '2017':
        dfa = df_gols.loc[
            ((df_gols['mandante'] == time_f) | (df_gols['visitante'] == time_f)) & (df_gols['ID'] >= 5746) & (
                    df_gols['ID'] < 6126)]

        # Gols pró, caso o time seja o mandanate os gols pró é os da coluna 'placar_Mandante', caso o mesmo time seja o
        # Visitante os gols pró está na coluna 'placar_Visitante', o oposto disso é os gols contra
        jogos_mandante = dfa[dfa['mandante'] == time_f]
        golsfeitosmandante += jogos_mandante['mandante_Placar'].sum()
        golstomadom += jogos_mandante['visitante_Placar'].sum()
        jogos_visitante = dfa[dfa['visitante'] == time_f]
        golsfeitovisitante += jogos_visitante['visitante_Placar'].sum()
        golstomadov += jogos_visitante['mandante_Placar'].sum()
    elif year == '2018':

        dfa = df_gols.loc[
            ((df_gols['mandante'] == time_f) | (df_gols['visitante'] == time_f)) & (df_gols['ID'] >= 6126) & (
                    df_gols['ID'] < 6506)]
        jogos_mandante = dfa[dfa['mandante'] == time_f]
        golsfeitosmandante += jogos_mandante['mandante_Placar'].sum()
        golstomadom += jogos_mandante['visitante_Placar'].sum()
        jogos_visitante = dfa[dfa['visitante'] == time_f]
        golsfeitovisitante += jogos_visitante['visitante_Placar'].sum()
        golstomadov += jogos_visitante['mandante_Placar'].sum()

    elif year == '2019':
        dfa = df_gols.loc[
            ((df_gols['mandante'] == time_f) | (df_gols['visitante'] == time_f)) & (df_gols['ID'] >= 6506) & (
                    df_gols['ID'] < 6886)]

        jogos_mandante = dfa[dfa['mandante'] == time_f]
        golsfeitosmandante += jogos_mandante['mandante_Placar'].sum()
        golstomadom += jogos_mandante['visitante_Placar'].sum()

        jogos_visitante = dfa[dfa['visitante'] == time_f]
        golsfeitovisitante += jogos_visitante['visitante_Placar'].sum()
        golstomadov += jogos_visitante['mandante_Placar'].sum()

    elif year == '2020':
        dfa = df_gols.loc[
            ((df_gols['mandante'] == time_f) | (df_gols['visitante'] == time_f)) & (df_gols['ID'] >= 6886) &
            (df_gols['ID'] < 7266)]

        jogos_mandante = dfa[dfa['mandante'] == time_f]
        golsfeitosmandante += jogos_mandante['mandante_Placar'].sum()
        golstomadom += jogos_mandante['visitante_Placar'].sum()
        jogos_visitante = dfa[dfa['visitante'] == time_f]
        golsfeitovisitante += jogos_visitante['visitante_Placar'].sum()
        golstomadov += jogos_visitante['mandante_Placar'].sum()

    elif year == '2021':

        dfa = df_gols.loc[
            ((df_gols['mandante'] == time_f) | (df_gols['visitante'] == time_f)) &
            (df_gols['ID'] >= 7266) & (df_gols['ID'] < 7646)]
        jogos_mandante = dfa[dfa['mandante'] == time_f]
        golsfeitosmandante += jogos_mandante['mandante_Placar'].sum()
        golstomadom += jogos_mandante['visitante_Placar'].sum()
        jogos_visitante = dfa[dfa['visitante'] == time_f]
        golsfeitovisitante += jogos_visitante['visitante_Placar'].sum()
        golstomadov += jogos_visitante['mandante_Placar'].sum()

    elif year == '2022':
        dfa = df_gols.loc[
            ((df_gols['mandante'] == time_f) | (df_gols['visitante'] == time_f)) & (df_gols['ID'] >= 7646)]

        jogos_mandante = dfa[dfa['mandante'] == time_f]
        golsfeitosmandante += jogos_mandante['mandante_Placar'].sum()
        golstomadom += jogos_mandante['visitante_Placar'].sum()
        jogos_visitante = dfa[dfa['visitante'] == time_f]
        golsfeitovisitante += jogos_visitante['visitante_Placar'].sum()
        golstomadov += jogos_visitante['mandante_Placar'].sum()

    valores = [golsfeitosmandante, golsfeitovisitante]
    valores1 = [golstomadom, golstomadov]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'pie'}, {'type': 'pie'}]])

    fig.add_trace(go.Pie(labels=['Gols como Mandante', 'Gols como Visitante'], values=valores, name=''),
                  row=1, col=1
                  )
    fig.add_trace(go.Pie(labels=['Gols Tomados como Mandante', 'Gols tomados como Visitante'], values=valores1,
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
