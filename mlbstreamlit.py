import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/13Rxh8FddZGRlaDff2314Jwh2hM4cj5S-qaBU0aKdVWA/edit?usp=sharing"

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)


data = conn.read(spreadsheet=url)
st.dataframe(data)
