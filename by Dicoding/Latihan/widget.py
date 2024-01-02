import streamlit as st
import pandas as pd

nama = st.text_input(label="Masukan Nama anda: ",value='')
st.write("Nama anda adalah ",nama)

feedback_message =st.text_area(label="Masukan feedbck anda")
st.write(feedback_message)

date = st.date_input(label="Masukan tanggal lahir")
st.write("tanggal lahir anda ",date)

datarame = st.file_uploader("Msukan dataset anda")
if datarame:
    df = pd.read_csv(datarame)
    st.dataframe(df)

picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)

if st.button('Say hello'):
    st.write('Hello there')

agree = st.checkbox('I agree') 
if agree:
    st.write('Welcome to MyApp')


genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)