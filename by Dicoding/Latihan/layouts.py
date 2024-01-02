import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title('Belajar Analisis Data') 
#sidebar
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)
#colums
col1,col2,col3 = st.columns([1,1,1])
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")
#tab
tab1,tab2,tab3 = st.tabs(['tab 1', 'tab 2','tab 3'])
with tab1:
    st.header('Tab 1')
    st.image("https://static.streamlit.io/examples/cat.jpg")
with tab2:
    st.header('Tab 2')
    st.image("https://static.streamlit.io/examples/dog.jpg")
with tab3:
    st.header('Tab 3')
    st.image("https://static.streamlit.io/examples/owl.jpg")
#container
with st.container():
    st.write("Ini Contoh Container")
    x = np.random.normal(15,5,250)
    fig,ax = plt.subplots()
    ax.hist(x= x, bins = 15)
    st.pyplot(fig)
st.write('outside counteiner')
with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )