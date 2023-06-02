import streamlit as st
from bs4 import BeautifulSoup
import requests

def get_recipe_data(url):
    # Realiza a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)
    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extrai os ingredientes da página
    ingredientes = []
    # Lógica para extrair os ingredientes da página utilizando Beautiful Soup
    
    return ingredientes

def main():
    st.title("Gerador de Lista de Compras Semanal")
    
    # Campo de entrada de URL na barra lateral
    url = st.sidebar.text_input("Insira a URL do site de receitas", value="", key='urls')
    
    # Verifica se o campo de URL não está vazio
    if url:
        st.write("URL inserida:", url)
        
        # Botão para editar a URL
        if st.sidebar.button("Editar URL"):
            url = st.sidebar.text_input("Insira a URL do site de receitas", value=url, key='urls')
        
        # Lógica para processar a URL e gerar a lista de compras
        lista_compras = get_recipe_data(url)
        
        st.subheader("Lista de Compras:")
        for item in lista_compras:
            st.write(item)

if __name__ == '__main__':
    main()
