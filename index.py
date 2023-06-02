import streamlit as st

def main():
    st.title("Gerador de Lista de Compras Semanal")
    
    # Campo de entrada de URL na barra lateral
    url = st.sidebar.text_input("Insira a URL do site de receitas", value="", key='urls')
    
    # Verifica se o campo de URL não está vazio
    if url:
        st.write("URL inserida:", url)
        # Lógica para processar a URL e gerar a lista de compras
        # ...
        # Exemplo de geração da lista de compras
        lista_compras = ["Ingredientes A", "Ingredientes B", "Ingredientes C"]
        
        st.subheader("Lista de Compras:")
        for item in lista_compras:
            st.write(item)
    

if __name__ == '__main__':
    main()
