import streamlit as st
import pandas as pd
import time

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
st.sidebar.selectbox('Show Movies',['The Machinist', 'Memento', 'Shutter Island', 'Inception'])

col1, col2, col3 = st.columns(3)

with col1:
    st.image('beautiful-flowers-lily.webp')

with col2:
    st.video('LOREM IPSUM - AI Short Film.mp4')

with col3:
    st.image('beautiful-flowers-lily.webp')

progress_bar = st.progress(0, text='Processing')

for progress in range(100):
    time.sleep(0.01)
    progress_bar.progress(progress+1, text='Processing')

st.success('Success')
st.info('Info')
st.warning('Warning')
st.error('Error')

st.text_input('Enter text here')
st.number_input('Enter number here')
st.date_input('Enter date here')

st.button('Click here')
st.balloons()

st.file_uploader('Select file')