import pandas as pd
import numpy as np
import streamlit as st

# set the page
st.set_page_config(layout="wide", page_title="Sales Dashboard")
# set the title page
st.title("Cafe Sales Dashboard")
# load dataset
df = pd.read_csv("cafe_sales_clean.csv")
# interactive dataframe
st.dataframe(df)

st.balloons()

