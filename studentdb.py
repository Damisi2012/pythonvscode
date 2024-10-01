import streamlit as st
import pandas as pd

csvfiles = pd.read_csv('scores.csv')


menu = st.sidebar.selectbox('Menu',['Submit scores','Database'])
if menu == 'Database':
    st.table(csvfiles)

if menu == ('Submit scores'):
    st.subheader('Students score')


    st.write('Submit Students Name:')
    name = st.text_input('')


    sc1,sc2 = st.columns(2)
    sc3,sc4 = st.columns(2)
    sc5,sc6 = st.columns(2)


    with sc1:
        math = st.number_input('Enter Students Math Score:',0,100)


    with sc2:
        eng = st.number_input('Enter Students English Score:',0,100)


    with sc3:
        science = st.number_input('Enter Students Science Score:',0,100)


    with sc4:
        history = st.number_input('Enter Students History Score:',0,100)


    with sc5:
        art = st.number_input('Enter Students Art Score:',0,100)


    with sc6:
        geo = st.number_input('Enter Students Geography Score:',0,100)


    total = math + eng + science + history + art + geo



    averaged = total / 6
    average = round(averaged,2)

    if average >= 90:
        grade = 'A+'

    elif average >= 80:
        grade = 'A'

    elif average >= 70:
        grade = 'B'
    
    elif average >= 60:
        grade = 'C'

    elif average >= 59:
        grade = 'D'

    elif average < 50:
        grade = 'F-'


    if st.button('Save Student score'):
            st.write(name,'got a',grade,'for school and their total score is',total)
            studentdict = {'Name':[name],'Math':[math],'English':[eng],'Science':[science],'History':[history],'Art':[art],'Geography':[geo]}
            studenttable = pd.DataFrame(studentdict)
            tablesjoin = pd.concat([csvfiles,studenttable],ignore_index=True)
            tablesjoin.to_csv('scores.csv',index=False)