import streamlit as st

password = st.text_input('Login to your account',type='password')
if password == 'Socceristhebestsportevercreated':
    st.write('You are logged in')
ticket = st.radio('Season pass ticket',['Choose','Standard $200','Vip $500'],horizontal=True)
merchandise = st.radio('Team merchandise',['None','Jersey $60','Scarf $30','Hat $20'],horizontal=True)
snacks = st.radio('Snacks',['None','Popcorn $10','Hotdog $15','Soda $5'],horizontal=True)
subscription = st.radio('Sport subscription',['None','Monthly $20','Annual $200'],horizontal=True)