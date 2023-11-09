import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Upload","Preproces","Feature Engineering","Analysis"],
    icons = ["cloud-arrow-up","database-check","gear-fill","graph-up"],

    menu_icon = "cast",
    default_index = 0,

  )
uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
    #if uploaded_file.type == 'text/csv':