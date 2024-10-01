import streamlit as st
import pandas as pd

adminpass = st.text_input('Enter admin password',type='password')
if adminpass == 'secretpassword2':
    st.write('You guessed the password')
    csvlink = pd.read_csv('church.csv')

name = st.text_input('Enter your name')
age = st.number_input('Enter your age',0)
gender = st.radio('What is your gender',['Male','Female'],horizontal=True)

if age <=12:
    st.write(name, 'will be in the Kids class in the church')#3-12

elif age <=19:
    st.write(name, 'will be in the Teens class in the church')#13-19

elif age <=35:
    st.write(name, 'will be in the Youth class in the church')#20-35

elif age <=64:
    st.write(name, 'will be in the Adult class in the church')#36-64

else:
    st.write(name, 'will be in the Elders class in the church')#65+

if st.button('Save Information'):
    churchdict = {'name':[name],'age':[age],'gender':[gender]}

    churchtable = pd.DataFrame(churchdict)
    tablesjoins = pd.concat([csvlink,churchtable],ignore_index=True)
    tablesjoins.to_csv('church.csv',index=False)