import pandas as pd
import streamlit as st
import plotly.express as px

# Título
st.set_page_config(page_title="Estado OneAgent", layout="wide")
st.title("📊 Dashboard de Estado de OneAgent por Host")

# Cargar datos
df = pd.read_excel("estado_oneagent_2025_actualizado.xlsx")

# Filtro de estado
estados = st.multiselect(
    "Filtrar por estado de versión:",
    options=df["estado_version"].unique(),
    default=df["estado_version"].unique()
)

df_filtrado = df[df["estado_version"].isin(estados)]

# Preparar datos para gráfico
conteo_estados = df_filtrado["estado_version"].value_counts().reset_index()
conteo_estados.columns = ["estado", "cantidad"]

# Gráfico de barras
fig = px.bar(
    conteo_estados,
    x="estado", y="cantidad",
    labels={"estado": "Estado", "cantidad": "Cantidad de Hosts"},
    color="estado",
    title="Cantidad de Hosts por Estado de Versión"
)

fig.update_layout(xaxis_title="Estado", yaxis_title="Cantidad")

st.plotly_chart(fig, use_container_width=True)

# Mostrar tabla
st.subheader("📋 Detalle de Hosts")
st.dataframe(df_filtrado, use_container_width=True)
