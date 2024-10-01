import streamlit as st

name = st.text_input('Enter your name')
salary = st.number_input('Enter your salary',0)

if salary <= 30000:
    st.write('You can buy a used car')

elif salary <= 60000:
    st.write('You can buy an economy car')

elif salary <= 100000:
    st.write('You can buy a mid range car')

elif salary <= 200000:
    st.write('You can buy a luxury car')

else:
    st.write('You can buy a very expensive car like a lamboghini')

st.button('Checkout')