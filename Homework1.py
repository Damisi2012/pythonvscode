import streamlit as st

st.header('Damisi Soccer shop')
st.image('https://www.bing.com/th?id=OPHS.o%2bIR%2bxE5rRpHVg474C474&o=5&pid=21.1&w=160&h=160&qlt=100&dpr=1.3&c=8&pcl=f5f5f5')

st.subheader('Man City')
socks,shorts,shirt = st.columns(3)
with socks:
    if st.checkbox('Man city socks €20'):
        st.write('Want any Man city shorts?')

with shorts:
    if st.checkbox('Man city shorts €35'):
        st.write('Want any Man city shirts?')

with shirt:
    if st.checkbox('Man city shirt €60'):
        st.write('Want any Arsenal cloths?')

st.subheader('Arsenal')
socks,shorts,shirt = st.columns(3)
with socks:
    if st.checkbox('Arsenal socks $30'):
        st.write('Want any Arsenal shorts?')

with shorts:
    if st.checkbox('Arsenal shorts $55'):
        st.write('Want any Arsenal shirt?')

with shirt:
    if st.checkbox('Arsenal shirt $105'):
        st.write('Want any Chealsea cloths')

st.subheader('Chelsea')
socks,shorts,shirt = st.columns(3)
with socks:
    if st.checkbox('Chelsea socks £20'):
        st.write('Want any Chelsea shorts?')

with shorts:
    if st.checkbox('Chelsea shorts £31'):
        st.write('Want any Chelsea shirt')

with shirt:
    if st.checkbox('Chelsea shirt £64'):
        st.write('That all for my soccer shop')