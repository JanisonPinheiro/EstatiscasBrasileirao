# TRATAR PARA QUANDO O VALOR SEJA 0 O GRÁFICO EXIBA UMA COLUNA, NÃO DEIXANDO O GRAFICO COM COLUNAAS EM BRANCO,
# MESMO COM O VALOR 0
def tratar_dataframe(dftest):
    df_t = dftest.copy()
    df_t.loc[df_t['chutes'] == 0, 'chutes'] = 0.1
    df_t.loc[df_t['chutes_no_alvo'] == 0, 'chutes_no_alvo'] = 0.1

    df_t.loc[df_t['cartao_amarelo'] == 0, 'cartao_amarelo'] = 0.1
    df_t.loc[df_t['cartao_vermelho'] == 0, 'cartao_vermelho'] = 0.1
    return df_t
