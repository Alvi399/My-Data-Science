import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.title("belajar Analisa data")
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
st.header("Pengembangan Dashboard")
st.subheader("pengembanagan Dashboard")
st.write(pd.DataFrame({
    'c1':[1,2,3,4,5],
    'c2':[12,20,30,40,50]
}))
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
st.caption("Copyright (r) Samboo")
#data display
st.dataframe(data=df,width=500,height=150)
st.table(data=df)
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
x = np.random.normal(15, 5, 250)
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)