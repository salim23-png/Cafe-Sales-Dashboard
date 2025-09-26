import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.colors as pc

# set the page
st.set_page_config(layout="wide", page_title="Sales Dashboard")
# set the title page
st.title("Cafe Sales Dashboard")
# load dataset
df = pd.read_csv("cafe_sales_clean.csv")
# only show the head and tail
limited_df = pd.concat([df.head(5), df.tail(5)])
# interactive dataframe
st.dataframe(df.style.highlight_max(axis=0))
# pie chart
counts = df["Item"].value_counts().reset_index()
counts.columns = ["Item", "Count"]
pie_fig = px.pie(counts, values='Count', names='Item', hole=.3, color_discrete_map=pc.qualitative.Pastel)
st.plotly_chart(pie_fig)
# line chart
df['Transaction Date'] = pd.to_datetime(df['Transaction Date']) # make sure the type as datetime
daily_spent = df.groupby(df['Transaction Date'].dt.date)['Total Spent'].sum().reset_index()
daily_spent.columns = ['Transaction Date', 'Total Spent']
line_fig = px.line(daily_spent, x="Transaction Date", y="Total Spent")
st.plotly_chart(line_fig)

st.balloons()

