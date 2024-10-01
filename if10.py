import streamlit as st

savings = 150
st.write('You saved up',savings,"dollars")
book_cost = 10
st.write("You got a book for",book_cost,"dollars")
snacks_cost = 9
st.write("You got snacks for",snacks_cost,"dollars")
toy_cost = 12
st.write("You got toys for",toy_cost,"dollars")
taxi_cost = 20
st.write("You got a taxi ride for",taxi_cost,"dollars")
game_cost = 30
st.write("You got a game for",game_cost,"dollars")
total = book_cost + snacks_cost + toy_cost + taxi_cost + game_cost
st.write("You spent",total,"dollars")
remaining = savings - total
if remaining > 0:
    st.write("You still have some money left")
else:
    st.write("You are now in debt")