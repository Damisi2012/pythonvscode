import streamlit as st

st.set_page_config(page_title='Season shop',page_icon='')
password = st.text_input('Login to your account',type='password')
if password == 'Socceristhebestsportevercreated':
    st.write('You are logged in')
ticket = st.radio('Season pass ticket',['Choose','Standard $200','Vip $500'],horizontal=True)
if ticket == 'Choose':
    st.write('You have to choose a option to watch a match')

elif ticket == 'Standard $200':
    st.write('You bought a standard ticket for $200')

else:
    st.write('You bought a VIP ticket for $500')

merchandise = st.radio('Team merchandise',['None','Jersey $60','Scarf $30','Hat $20'],horizontal=True)
if merchandise == 'None':
    st.write('You bought nothing')

elif merchandise == 'Jersey $60':
    st.write('You bought a Jersey for $60')

elif merchandise == 'Scarf $30':
    st.write('You bought a scarf for $30')

else:
    st.write('You bought a Hat for $20')
snacks = st.radio('Snacks',['None','Popcorn $10','Hotdog $15','Soda $5'],horizontal=True)

if snacks == 'None':
    st.write('You bought nothing')

elif snacks == 'Popcorn $10':
    st.write('You bought popcorn for $10')

elif snacks == 'Hotdog $15':
    st.write('You bought a hotdog for $15')

else:
    st.write('You bought a soda for $5')
subscription = st.radio('Sport subscription',['None','Monthly $20','Annual $200'],horizontal=True)

if subscription == 'None':
    st.write('You have no sport subscription')

elif subscription == 'Monthly $20':
    st.write('You have a monthly subscription')

else:
    st.write('You have a annual subsciption')