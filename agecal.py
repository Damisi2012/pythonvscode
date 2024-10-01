import streamlit as st

st.header('Age Calculator App')

name = st.text_input('Enter your name here')
currentyear = st.number_input('Enter your current year here',0)
yob = st.number_input('Enter your year of birth here',0)
age = currentyear - yob

if st.button('Check My Age'):
    st.write('Your age is',age,'in',currentyear)