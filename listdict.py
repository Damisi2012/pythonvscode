import streamlit as st

game = 'Roblox'#The most popular game

bestgames = ['Roblox', 'Fortnite','Minecraft','Rocket league']
st.write('My best games are',bestgames)

#Selectbox
selecthaircolor = st.selectbox ('Choose which hair color you have',['Black', 'Brown','Blonde','Gray','Bald','None of the above'])
st.write('Your hair color is',selecthaircolor)


#Radio
hemisphere = st.radio('Which hemisphere do you libe in',['North', 'South'])
st.write('You live in the', hemisphere,'hemisphere')


#Sidebar
Hobbies = st.sidebar.selectbox('Hobies',['Gaming','Music','Sports'])