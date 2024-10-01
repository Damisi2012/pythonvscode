import streamlit as st
import pandas as pd

csvlink = pd.read_csv('donor.csv')
menu = st.sidebar.selectbox('menu',['Registration','Donation Database'])
if menu == 'Donation Database':
    st.table(csvlink)

if menu == 'Registration':
    st.subheader('Donation')
    name = st.text_input('Name')
    contact = st.text_input('Contact')
    blood = st.radio('Blood group',['A','B','AB','O'])
    illness = st.radio('Select Illness',['Disease','Infection','None'])

    if st.button('Submit Donor Details'):
        donordict = {'name':[name],'contact':[contact],'blood':[blood],'illness':[illness]}

        donortable = pd.DataFrame(donordict)
        tablesjoin = pd.concat([csvlink,donortable],ignore_index=True)
        tablesjoin.to_csv('donor.csv',index=False)