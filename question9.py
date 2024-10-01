import streamlit as st

lemon_cost = 10
sugar_cost = 8
cup_cost = 5
selling_cost = 2
total = lemon_cost + sugar_cost + cup_cost
revenue = cup_cost * selling_cost
profit = total - revenue
st.write("Hello Sarah you made a profit of",profit, "dollars")