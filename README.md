# Statistics of the last 5 years of the Brazilian Football Championship Series A

Application running ---> https://estatisticasbrasileirao.up.railway.app/

The web application is composed of a column "Clubes", where it is possible to choose the club that you want to see the statistics through a radioItems. In the main column, there is the application title, a radioItems for years and a dropdown, in addition to the chart that returns the data from the dataframe.

Through the radioItems for years, it is possible to choose the year to view the data. In the dropdown, the desired chart is selected, and it is possible to choose between charts containing data about "Chute no Gol vs Chutes", "Faltas vs Cartões" and, finally, "Gols Feitos vs Gols Tomados". The chart is returned with the data according to the user's choice.

In the graph named "Chutes no alvo Vs Chutes", the data is shown by rounds. In the blue column, the numbers of shots that were aimed at the goal are displayed, while in the red column, the number of shots that went out of bounds are shown.

In the "Faltas vs Cartões" graph, the data is shown by rounds. The blue column shows the number of fouls committed by the team, the yellow column shows the number of yellow cards the team received, and the red column shows the number of red cards the team received.

Lastly, in the "Gols feitos vs Gols tomados" graph, in the "Gols pró" pie chart, the relationship is shown by year of the number of goals the team scores at home and the number of goals they score playing as visitors. Next to it, in another pie chart named "Gols Contra", the relationship is shown by year of the number of goals the team concedes at home versus the number of goals they concede away from home.

Used  Datasets ---> https://www.kaggle.com/datasets/adaoduque/campeonato-brasileiro-de-futebol?select=campeonato-brasileiro-cartoes.csv
