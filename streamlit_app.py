from itertools import product
import streamlit as st
import pandas as pd

st.write("""
# My first app
hello *world!!*
""")
url='https://raw.githubusercontent.com/kwaii00/product1/main/product.csv'
df=pd.read_csv(url)
st.line_chart(df)
