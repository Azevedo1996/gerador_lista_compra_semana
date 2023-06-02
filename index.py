import streamlit as st
import requests
from bs4 import BeautifulSoup

def extrair_ingredientes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    ingredientes = []
    
    # Extrair ingredientes da página da receita
    lista_ingredientes = soup.find_all('li', class_='ingredient')
    for ingrediente in lista_ingredientes:
        ingredientes.append(ingrediente.text.strip())
    
    return ingredientes

def main():
    st.title("Gerador de Lista de Compras")
    
    # Obtendo as URLs das receitas
    urls_receitas = []
    num_receitas = st.number_input("Quantas receitas você deseja adicionar à lista de compras?", min_value=1, value=1, step=1)

    for i in range(num_receitas):
        url = st.text_input(f"Insira a URL da receita {i+1}:")
        urls_receitas.append(url)

    # Gerando a lista de compras
    lista_compras = []
    for url in urls_receitas:
        ingredientes = extrair_ingredientes(url)
        lista_compras.extend(ingredientes)

    # Exibindo a lista de compras
    st.header("Lista de Compras:")
    if lista_compras:
        for item in lista_compras:
            st.write("- " + item)
    else:
        st.write("Nenhuma receita adicionada.")

if __name__ == "__main__":
    main()
