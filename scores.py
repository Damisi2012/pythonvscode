import streamlit as st

st.header('ERP subject scores')
name = st.text_input('Stundent name here')
gym,math = st.columns(2)

with gym:
    gym = st.number_input('Enter your gym scores here',0)
with math:
    math = st.number_input('Enter your math scores here',0)

French,English = st.columns(2)

with French:
    French = st.number_input('Enter your french scores here',0)
with English:
    English = st.number_input('Enter your english scores here',0)

Makerfaire,music = st.columns(2)

with Makerfaire:
    Makerfaire = st.number_input('Enter your Makerfaire scores here',0)
with music:
    music = st.number_input('Enter your music scores here',0)

total_score = gym + math + French + English + Makerfaire + music
average = gym + math + French + English + Makerfaire + music / 6

if st.button('Check My Scores'):
    st.write(name,'total score is',total_score,'their average is:',average)