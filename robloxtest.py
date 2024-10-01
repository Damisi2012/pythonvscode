import streamlit as st

name = st.text_input('Your name')

Roblox = 150
username = st.text_input('Your Roblox username')
password = st.text_input('Roblox password',type='password' )
if password == 'password':
    st.write('You are logged in')

gamepass = st.radio('Which gamepass do you want',['Choose','VIP $50','Premium $120'],horizontal=True)
pet = st.radio('Do you want to buy a pet for gameplay',['Choose','Yes $40','No $0'],horizontal=True)
robux = st.radio('You have extra money to buy robux',['Choose','800 $10','2000 $25','4500 $50'],horizontal=True)
if gamepass == 'Choose':
    st.write('You should choose a option')

elif gamepass == 'VIP $50':
    st.write('You spent 50 dollars on this gamepass')

else:
    st.write('You spent 120 dollars on this gamepass')

if pet == 'Choose':
    st.write('You should choose a option')

elif pet == 'Yes $40':
    st.write('You spent 40 dollars on this pet')

else:
    st.write('You did not buy a pet')

if robux == 'Choose':
    st.write('You should choose a option')

elif robux == '800 $10':
    st.write('You spent 10 dollars on robux')

elif robux == '2000 $25':
    st.write('You spent 25 dollars on robux')

else:
    st.write('You spent 50 dollars on robux')

st.write('You also spent 150 dollars to get Roblox')