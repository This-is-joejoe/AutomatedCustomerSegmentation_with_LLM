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
if selected == "Upload":
    st.header("Easy Segementation Tool")

        
    uploaded_files = st.file_uploader("Choose a file",accept_multiple_files=True)

    if uploaded_files is None:
        st.stop()

    @st.cache_data
    def load_data(files):
        dfs = {}
        for file in files:
            dfs[file.name] = pd.read_csv(file)
        print('load file')
        return dfs

    names = list()
    dfs = load_data(uploaded_files)

    for uploaded_file in uploaded_files:
        names.append(uploaded_file.name)
        print(str(uploaded_file.name))

    sheet_selects = st.multiselect('Tables', names)
    if len(sheet_selects) ==0:
        st.stop()


    tabs = st.tabs(sheet_selects)
    for tab,name in zip(tabs,sheet_selects):
        with tab:
            df = dfs[name]
            st.dataframe(df.head())
