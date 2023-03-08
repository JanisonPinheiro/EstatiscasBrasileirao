# Handle it so that when the value is 0, the chart displays a column instead of leaving blank columns
def handle_dataframe(df_received):
    df_t = df_received.copy()
    df_t.loc[df_t['chutes'] == 0, 'chutes'] = 0.1
    df_t.loc[df_t['chutes_no_alvo'] == 0, 'chutes_no_alvo'] = 0.1

    df_t.loc[df_t['cartao_amarelo'] == 0, 'cartao_amarelo'] = 0.1
    df_t.loc[df_t['cartao_vermelho'] == 0, 'cartao_vermelho'] = 0.1
    return df_t
