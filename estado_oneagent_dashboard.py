import pandas as pd
import streamlit as st
import plotly.express as px

# Título
st.set_page_config(page_title="Estado OneAgent", layout="wide")
st.title("📊 Dashboard de Estado de OneAgent por Host")

# Cargar datos
df = pd.read_excel("estado_oneagent_hosts.xlsx")

# Filtro de estado
estados = st.multiselect(
    "Filtrar por estado de versión:",
    options=df["estado_version"].unique(),
    default=df["estado_version"].unique()
)

df_filtrado = df[df["estado_version"].isin(estados)]

# Gráfico de barras
fig = px.bar(
    df_filtrado["estado_version"].value_counts().reset_index(),
    x="index", y="estado_version",
    labels={"index": "Estado", "estado_version": "Cantidad de Hosts"},
    color="index",
    title="Cantidad de Hosts por Estado de Versión"
)
fig.update_layout(xaxis_title="Estado", yaxis_title="Cantidad")

st.plotly_chart(fig, use_container_width=True)

# Mostrar tabla
st.subheader("📋 Detalle de Hosts")
st.dataframe(df_filtrado, use_container_width=True)