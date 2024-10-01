import streamlit as st

st.subheader('Docter Appointment Form')

st.write('Name')
half1,half2 = st.columns(2)

with half1:
    firstname = st.text_input('First')

with half2:
    lastname = st.text_input('Last')

st.write('Phone')
phone = st.number_input('Phone number here',0)

st.write('Date of Birth')
DOB = st.date_input('YYYY-MM-DD')

st.write('Address')
street = st.text_input('Street name')

st.write('City and Region')
half3,half4 = st.columns(2)

with half3:
    City = st.text_input('City')

with half4:
    region = st.text_input('region')

st.write('Postal/zip code and country')
half5,half6 = st.columns(2)

with half5:
    postalcode = st.text_input('Postal/zip code')

with half6:
    country = st.text_input('Country')

st.write('Email')
email = st.text_input('Email')