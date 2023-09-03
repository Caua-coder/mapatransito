import streamlit as st
import folium
from streamlit_folium import st_folium

# Dados fictícios de operações policiais (latitude, longitude, descrição, tipo)
operacoes_policiais = [
    (-22.8979, -43.4897, "Operação em Senador Camará, linhas: 397, 746, 790SV, 855, 926", "Operações"),
    (-22.9898, -43.2485, "Operação em Rocinha, linhas: 309, 548, 553, 565", "Operações"),
    (-22.8899, -43.4198, "Operação em Jardim Novo, linhas: 383, 794, 801", "Operações"),
    (-22.7599, -43.2827, "Roubo de Carga: Duque de Caxias, Rua Cambuci", "Roubo de Carga"),
    (-22.8054, -43.3568, "Roubo em Coletivo: Pavuna, Rua Mércurio, linha: 734L", "Roubo em Coletivo"),
    (-22.8795, -43.4582, "Roubo de Carga: Bangu, Rua Francisco Real", "Roubo de Carga"),
    (-22.8059, -43.3883, "Roubo em Coletivo: Nova Iguaçu, Av. Tancredo Neves, linha: 749L", "Roubo em Coletivo"),
]

# Configuração da página do Streamlit
st.title('Mapa de Criminalidade: Transporte')
st.sidebar.header('Filtros')

# Opções do filtro
opcoes_filtro = ["Todos", "Operações", "Roubo de Carga", "Roubo em Coletivo"]

# Filtro para escolher o tipo de operação
tipo_operacao = st.sidebar.selectbox("Selecione o Tipo de delito", opcoes_filtro)

# Dicionário de cores por categoria
cores = {
    "Operações": "blue",
    "Roubo de Carga": "red",
    "Roubo em Coletivo": "green",
}

# Crie um mapa com Folium
m = folium.Map(location=[-22.9035, -43.2096], zoom_start=11)

# Filtra os dados com base no tipo de operação selecionado
operacoes_filtradas = []

if tipo_operacao == "Operações":
    operacoes_filtradas = [op for op in operacoes_policiais if op[3] == "Operações"]
elif tipo_operacao == "Roubo de Carga":
    operacoes_filtradas = [op for op in operacoes_policiais if op[3] == "Roubo de Carga"]
elif tipo_operacao == "Roubo em Coletivo":
    operacoes_filtradas = [op for op in operacoes_policiais if op[3] == "Roubo em Coletivo"]
elif tipo_operacao == "Todos":
    operacoes_filtradas = operacoes_policiais


# Adicione marcadores ao mapa para as operações filtradas com cores personalizadas
for lat, lon, descricao, categoria in operacoes_filtradas:
    folium.Marker(
        [lat, lon],
        popup=descricao,
        icon=folium.Icon(color=cores[categoria], icon="info-sign")
    ).add_to(m)

# Exiba o mapa no Streamlit
st_data = st_folium(m, width="100%")
