pip install beautifulsoup4
import streamlit as st
import requests
from bs4 import BeautifulSoup


def obter_ingredientes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ingredientes = []
    for ingrediente in soup.find_all('li', class_='ingredient'):
        ingredientes.append(ingrediente.text.strip())
    return ingredientes


def gerar_lista_compras(receitas):
    lista_compras = []
    for receita in receitas:
        ingredientes = obter_ingredientes(receita)
        lista_compras.extend(ingredientes)
    return lista_compras


# Cabeçalho do aplicativo Streamlit
st.title("Gerador de Lista de Compras")
st.write("Selecione 7 receitas para a semana e gere a lista de compras de ingredientes.")

# Verifica se é o primeiro acesso à aplicação
if 'urls' not in st.session_state:
    st.session_state.urls = []
    st.session_state.urls = st.text_input("Insira a URL do site de receitas:", key='urls')
else:
    st.write("URLs salvas:")
    st.write(st.session_state.urls)
    if st.button("Editar URLs"):
        st.session_state.urls = st.text_input("Insira a URL do site de receitas:", st.session_state.urls, key='urls')

# Lista de seleção das receitas
receitas_selecionadas = st.multiselect("Selecione as receitas:", st.session_state.urls, default=st.session_state.urls[:7])

# Verifica se o usuário selecionou 7 receitas
if len(receitas_selecionadas) == 7:
    # Gera a lista de compras
    lista_compras_semana = gerar_lista_compras(receitas_selecionadas)

    # Imprime a lista de compras
    st.subheader("Lista de Compras:")
    for item in lista_compras_semana:
        st.write("- " + item)
else:
    st.warning("Por favor, selecione exatamente 7 receitas.")
