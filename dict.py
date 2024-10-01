import streamlit as st

#Data collection used when you want to save multiple items in a variable

#List by the square brackets
bestgames = ['Roblox','Fortnite','EAFC24','Rocket leaugue']

#Dictionary:
#can help you save items in different categories {}

# a list is good when you want to group items and choose one from items
#but a dictionary is good when you want to put items inside categories and also create a table
robloxname = ['Damdemjj_1',99,59,100]

st.write(robloxname)


studentdict  = {'Roblox name':'Damdemjj_1','Teamwork':99,'luck':59,'Skill':100}

st.write(studentdict)

st.table(studentdict)