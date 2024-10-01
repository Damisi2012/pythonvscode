import streamlit as st

saved_amount = 200
st.write('You saved 200 dollars to spent')
movie_cost = st.number_input('Enter the movie cost here',0)
popcorn_cost = st.number_input('Enter the popcorn cost',0)
ice_cream_cost = st.number_input('Enter the ice cream cost',0)
transport_cost = st.number_input('Enter the transport cost',0)
lost_money = st.number_input('Enter the amount of dollars you lost',0)
total = movie_cost + popcorn_cost + ice_cream_cost + transport_cost + lost_money
remaining = saved_amount - total