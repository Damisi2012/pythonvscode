import streamlit as st
import pandas as pd #this will read csv files and convert them to tables

st.set_page_config(page_title='Book A Docter',page_icon='🚑')
menu = st.sidebar.selectbox('Menu',['Book Appointment','Database']) #this is the menu to switch pages
csvlink = pd.read_csv('appointment.csv') #this will read any csv files
if menu == 'Database':
    st.table(csvlink) #this will display the csv files as a table

if menu == 'Book Appointment':
    adminpass = st.sidebar._text_input('Enter admin password',type='password')
    if adminpass == 'Robloxisagoodgame':
        st.table(csvlink)

    

    st.subheader('Docter Appointment')
    st.write('Fill the form below and we will get back soon to you for more updates and plan your appointment')

    left,right = st.columns(2)

    with left:
        firstname = st.text_input('First name')

    with right:
        lastname = st.text_input('Last name')


    with left:
        birthday = st.date_input("Choose your birthday",)

    with right:
        occupation = st.text_input('Enter your occupation')

    with left:
        st.write("")
        gender = st.radio('Choose your gender',['Male','Female'],horizontal=True)

    with right:
        phone = st.text_input('Phone number')

    street1 = st.text_input('Street address 1')

    street2 = st.text_input('Street address 2')
    left2,right2 = st.columns(2)

    with left2:
        city = st.text_input('City')

    with right2:
        st.text_input('State/Province')

    if st.button('Book an appointment'):
            docterdict = {'firstname':[firstname],'lastname':[lastname],'gender':[gender],'birthday':[birthday],'occupation':[occupation],
                          'phone':[phone],'street1':[street1],'street2':[street2],'city':[city]}
            doctertable = pd.DataFrame(docterdict)
            #st.write(docterdict)
            #st.table(doctertable)
            tablesjoin = pd.concat([csvlink,doctertable],ignore_index=True) #joins two tables
            tablesjoin.to_csv('appointment.csv',index=False) #saves to csv
            st.success('Submisson Completed')