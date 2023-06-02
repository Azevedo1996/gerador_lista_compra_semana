import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extrair_ingredientes(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        ingredientes = []

        # Extrair ingredientes da página da receita
        lista_ingredientes = soup.find_all('li', class_='ingredient')
        for ingrediente in lista_ingredientes:
            ingredientes.append(ingrediente.text.strip())

        return ingredientes
    except requests.exceptions.RequestException as e:
        st.warning(f"Ocorreu um erro ao obter os ingredientes da receita: {str(e)}")
        return []

def is_url_valid(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc)

def main():
    st.title("Gerador de Lista de Compras")

    # Obtendo as URLs das receitas
    urls_receitas = []
    num_receitas = st.number_input("Quantas receitas você deseja adicionar à lista de compras?", min_value=1, value=1, step=1)

    for i in range(num_receitas):
        url = st.text_input(f"Insira a URL da receita {i+1}:")
        urls_receitas.append(url)

    # Verificar se o botão de envio foi pressionado
    if st.button("Gerar Lista de Compras"):
        # Gerar a lista de compras
        lista_compras = []
        for url in urls_receitas:
            if is_url_valid(url):
                ingredientes = extrair_ingredientes(url)
                lista_compras.extend(ingredientes)
            else:
                st.warning(f"A URL '{url}' é inválida. Verifique e tente novamente.")

        # Exibindo a lista de compras
        if lista_compras:
            st.header("Lista de Compras:")
            for item in lista_compras:
                st.write("- " + item)
        else:
            st.warning("Nenhuma receita adicionada ou nenhum ingrediente encontrado.")

if __name__ == "__main__":
    main()
