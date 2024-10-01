import streamlit as st

savings = 250
st.write('You saved up 250 dolars to spend')
theme_park_cost = st.number_input('Enter the theme park cost here',0)
movies_cost = st.number_input('Enter the movie cost here',0)
snacks_cost = st.number_input('Enter the snack cost here',0)
bikes_cost = st.number_input('Enter the bike renting here',0)
beach_cost = st.number_input('Enter the beach cost here',0)
total_spent = theme_park_cost + movies_cost + snacks_cost + bikes_cost + beach_cost
remaining = savings - total_spent
if remaining > 0:
    st.write('You have',remaining,'dollars left')

else:
    st.write('You are now',remaining,'in debt')