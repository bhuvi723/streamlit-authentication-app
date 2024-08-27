import streamlit as st
from streamlit import query_params, rerun

query_params = st.query_params()

if query_params.get("page") == ["newsapp"]:
    st.title(":red[_TAAZA KHABHAR NEWS APP!_]")
