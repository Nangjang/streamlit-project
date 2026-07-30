import streamlit as st
import pandas as pd

st.title('Title')
st.header('Header')
st.subheader('Subheader')

st.write('Normal text')

st.markdown('''
## Name of Favourite Movies:
- The Machinist
- Memento
- Shutter Island
- Inception
''')

st.code('''
def add(a, b):
    return a + b

print(add(10, 20))
''')

st.latex('''
(a+b)^2=a^2+2ab+b^2
''')

ipl_df = pd.read_csv('ipl_deliveries.csv')
st.dataframe(ipl_df)

st.json({'name': 'Santosh', 'age': 30, 'gender': 'male'})

st.metric(label='Temperature', value='70 °F', delta='1.5 °F')

st.image('beautiful-flowers-lily.webp')
st.video('LOREM IPSUM - AI Short Film.mp4')

st.sidebar.title('Sidebar')
st.sidebar.radio('Movie', ['The Machinist', 'Memento', 'Shutter Island', 'Inception'])

col1, col2, col3 = st.columns(3)

with col1:
    st.image('beautiful-flowers-lily.webp')

with col2:
    st.video('LOREM IPSUM - AI Short Film.mp4')

with col3:
    st.image('beautiful-flowers-lily.webp')

