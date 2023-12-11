# Por: VICTOR GABRIEL DE JESUS MOURA
# SENAI CAMAÇARI - CURSO TECNICO DE DESENVOLVIMENTO DE SISTEMAS
# DEZEMBRO DE 2023

import pandas as pd


dados = {
    "Mês": ["Janeiro", "Fevereiro", "Março","Janeiro", "Fevereiro", "Março"],
    "Produto": ["Camisa", "Bermuda", "Calça","Camisa", "Bermuda", "Calça" ],
    "Vendas": [9, 14, 18, 24, 11, 0],
}

df = pd.DataFrame(dados)
df_janeiro = df.query('Mês == "Janeiro"')
print(df_janeiro)

