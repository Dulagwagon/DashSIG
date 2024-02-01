import streamlit as st
import psycopg2
import pandas as pd
from streamlit.connections import SQLConnection

conn = st.connection("postgresql", type=SQLConnection)



st.sidebar.title("SIG-Escola")

diretoria = st.sidebar.selectbox(
    "DRE",
    ('BT', 'CS', 'CL', 'IP', 'IT', 'MP', 'SA', 'SM'))

periodo = st.sidebar.selectbox(
    'Período',
    (2021.1, 2021.2, 2021.3))

st.write('Você selecionou o período', periodo)
st.write('e a DRE', diretoria)
df = conn.query('SELECT nome from core_unidade;')