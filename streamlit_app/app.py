import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

st.title("Dashboard Mobilité - Ligne 5")

def load_data():
    conn = psycopg2.connect(
        host="db_mobilite", database="mobilite", user="admin", password="admin123"
    )
    df = pd.read_sql("SELECT * FROM eco_compteurs", conn)
    conn.close()
    return df

df = load_data()
fig = px.bar(df, x='nom_lieu', y='valeur', title="Flux piétons/vélos par lieu")
st.plotly_chart(fig)
