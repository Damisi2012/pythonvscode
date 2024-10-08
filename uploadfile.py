import streamlit as st
import pandas as pd


st.set_page_config(page_title='Upload files',page_icon='📂')
menu = st.sidebar.selectbox('Choose an option',['Upload CSV','Upload image','Upload audio','Upload video'])

if menu == 'Upload CSV':
    st.subheader('Upload CSV and D')
    uploadcsv = st.file_uploader('Upload CSV File',type='csv')

    if uploadcsv:
        csvlink = pd.read_csv(uploadcsv)
        with st.expander('Open CSV table'):
            st.table(csvlink)



if menu == 'Upload image':
    uploadimage = st.file_uploader('Upload image file',type=['jpg','jpeg','png'])

    if uploadimage:
        st.image(uploadimage,use_column_width=True)



if menu == 'Upload audio':
    st.subheader('Upload Audio To Play')
    uploadaudio = st.file_uploader('Upload your audio file here',type=['mp3','wav'])
    if uploadaudio:
        st.audio(uploadaudio,format='audio/mp3')


if menu == 'Upload video':
    st.subheader('Upload YouTube Video link To Play')
    youtubelink = st.text_input('Paste your YouTube Video link here')
    if st.button('Play Youtube Video'):
        try:
            if youtubelink:
                st.video(youtubelink)
        except:
            st.write('Sorry I can not play this')