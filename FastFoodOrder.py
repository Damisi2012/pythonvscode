import streamlit as st

st.header("Damisi fast food resturant")
st.image('https://th.bing.com/th/id/OIP.73RlpZugfJfz5GaQdpVgBgHaC_?w=313&h=141&c=7&r=0&o=5&dpr=1.3&pid=1.7')

st.subheader('MEALS')
meal1,meal2,meal3,meal4,meal5,meal6 = st.columns(6)
with meal1:
    if st.checkbox("Double hamburger: $15"):
        st.write('Ok, anything else')

with meal2:
    if st.checkbox("Sirloin and fries: $20"):
        st.write("Ok, anything else")

with meal3:
    if st.checkbox('Medium size pizza: $15'):
        st.write('Ok, anything else')

with meal4:
    if st.checkbox('Small size pizza: $10'):
        st.write('anything else')

with meal5:
    if st.checkbox('Large size pizza: $20'):
        st.write("anything else")

with meal6:
    if st.checkbox('Extra large size pizza: $25'):
        st.write('Any drinks?')

st.subheader("DRINKS")
drink1,drink2,drink3,drink4,drink5,drink6 = st.columns(6)
with drink1:
    if st.checkbox("Lemonade: $8"):
        st.write('anymore drinks?')

with drink2:
    if st.checkbox("Iced tea: $8"):
        st.write('anymore drinks?')

with drink3:
    if st.checkbox('Root beer: $8'):
        st.write('anymore drinks?')

with drink4:
    if st.checkbox("Orange Crush: $8"):
        st.write('any more drinks?')

with drink5:
    if st.checkbox("Grape Crush: $8"):
        st.write('anymore drinks?')

with drink6:
    if st.checkbox('CreamSoda Crush: $8'):
        st.write('Want any healthy fruits?')

st.subheader('FRUITS')
fruit1,fruit2,fruit3,fruit4,fruit5,fruit6 = st.columns(6)
with fruit1:
    if st.checkbox('Orange: $3'):
        st.write('anymore fruits?')

with fruit2:
    if st.checkbox('Grapes: $3'):
        st.write('anymore fruits?')

with fruit3:
    if st.checkbox('Apple: $3'):
        st.write('anymore fruits?')

with fruit4:
    if st.checkbox('banana: $3'):
        st.write('anymore fruits?')

with fruit5:
    if st.checkbox('Pear: $3'):
        st.write('anymore fruits?')

with fruit6:
    if st.checkbox('Strawberry: $3'):
        st.write('any appetizer?')

st.subheader('APPETIZERS')
appetizer1,appetizer2,appetizer3,appetizer4,appetizer5,appetizer6 = st.columns(6)
with appetizer1:
    if st.checkbox('Ice cream: $8'):
        st.write('anymore appetizer?')

with appetizer2:
    if st.checkbox('Quater of cake: $7'):
        st.write('anymore appetizer?')

with appetizer3:
    if st.checkbox('2 cookies: $3'):
        st.write('anymore appetizer?')

with appetizer4:
    if st.checkbox('Donut: $4'):
        st.write('anymore appetizer?')

