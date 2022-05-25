from itertools import product
import streamlit as st
import pandas as pd

st.write("""
# My first app
hello *world!!*
""")

df=pd.read_csv("product.csv")
st.line_chart(df)
