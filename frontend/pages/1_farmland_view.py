import streamlit as st
import requests
import json
import pandas as pd


st.set_page_config(
    page_title="Farmland List View"
)

st.markdown("# Farmland List View")

farmlands = requests.get(
    'http://localhost:8000/csm/farmland/list'
)

df = pd.DataFrame(json.loads(farmlands.content))

st.dataframe(df)

