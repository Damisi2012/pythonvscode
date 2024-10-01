import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox('Choose an option',['Upload CSV','Upload image'])

if menu == 'Upload CSV':
    uploadcsv = st.file_uploader('Upload CSV File',type='csv')

    if uploadcsv:
        csvlink = pd.read_csv(uploadcsv)
        with st.expander('Open CSV table'):
            st.table(csvlink)



if menu == 'Upload image':
    uploadimage = st.file_uploader('Upload image file',type=['jpg','jpeg','png'])

    if uploadimage:
        st.image(uploadimage,use_column_width=True)