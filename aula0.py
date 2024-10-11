import json
import streamlit as st
import requests
import pandas as pd
import plotly.express as px


def formatar_valor(valor):
    if valor >= 1000000:
        return f"{valor/1000000:.2f} milhões"
    else :
        return f"{valor / 1000:.2f} mil"
    
        
st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos"

response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())
if st.button("todos"):
    receita = df['Preço'].sum()
    st.metric("Receita",formatar_valor(receita))
    linhas = df.shape[0]
    st.metric("Quantidade de vendas (linhas)",formatar_valor(linhas))
    st.dataframe(df)
    st.balloons()
    st.snow()
    
else:
    st.write("Clique no botão todos")
    
    
"""    
def formata_numero(valor,prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'
"""