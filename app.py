import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.colors as pc

# --- Page configuration ---
st.set_page_config(layout="wide", page_title="Sales Dashboard")

# --- Title ---
st.title("Cafe Sales Dashboard")

# --- Load dataset ---
# Read the CSV file and convert the Transaction Date column to datetime once.
df = pd.read_csv("cafe_sales_clean.csv")
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# --- Sidebar filters ---
# Allow users to filter by Payment Method and Location.
ith st.sidebar:
    # Add logo
    st.image("logo.png", use_container_width=True)

    # filters in sidebar
    payment_options = st.multiselect(
        "Choose Payment Method",
        options=df["Payment Method"].unique(),
        default=df["Payment Method"].unique()
    )
    location_options = st.multiselect(
        "Choose Location",
        options=df["Location"].unique(),
        default=df["Location"].unique()
    )
# --- Apply filters to the dataframe ---
filtered_df = df[
    (df["Payment Method"].isin(payment_options)) &
    (df["Location"].isin(location_options))
].copy()  # .copy() avoids SettingWithCopy warnings

# --- Create two columns for side-by-side charts ---
col1, col2 = st.columns(2)

# --- Pie chart: distribution of items sold ---
with col1:
    counts = filtered_df["Item"].value_counts().reset_index()
    counts.columns = ["Item", "Count"]
    pie_fig = px.pie(
        counts,
        values='Count',
        names='Item',
        hole=.3,
        color_discrete_sequence=pc.qualitative.Pastel  # use pastel color palette
    )
    st.plotly_chart(pie_fig, use_container_width=True)

# --- Line chart: total spending per day ---
with col2:
    daily_spent = (
        filtered_df
        .groupby(filtered_df['Transaction Date'].dt.date)['Total Spent']
        .sum()
        .reset_index()
    )
    daily_spent.columns = ['Transaction Date', 'Total Spent']
    line_fig = px.line(
        daily_spent,
        x="Transaction Date",
        y="Total Spent",
        markers=True  # optional: add markers to highlight each point
    )
    st.plotly_chart(line_fig, use_container_width=True)

# --- Show the filtered dataframe below the charts ---
st.dataframe(filtered_df)

# --- Celebration animation ---
st.balloons()
