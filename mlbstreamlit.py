# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/13Rxh8FddZGRlaDff2314Jwh2hM4cj5S-qaBU0aKdVWA/edit#gid=0"

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)


data = conn.read(spreadsheet=url, usecols=[0,1])
st.dataframe(data)
