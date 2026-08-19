import streamlit as st
import pandas as pd
from database import create_connection

st.set_page_config(page_title="Expense Tracker Dashboard", layout="wide")

st.title("💰 Personal Expense Tracker Dashboard")

# Load data
conn = create_connection()
df = pd.read_sql_query("SELECT * FROM expenses", conn)
conn.close()
df['date'] = pd.to_datetime(df['date'])

# --- Sidebar Filters ---
st.sidebar.header("Filters")

# Category filter
all_categories = sorted(df['category'].unique())
selected_categories = st.sidebar.multiselect(
    "Select Category", options=all_categories, default=all_categories
)

# Date range filter
min_date = df['date'].min()
max_date = df['date'].max()
date_range = st.sidebar.date_input(
    "Select Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date
)

# Apply filters
filtered_df = df[df['category'].isin(selected_categories)]

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df['date'] >= pd.to_datetime(start_date)) &
        (filtered_df['date'] <= pd.to_datetime(end_date))
    ]

# --- Top metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Expenses", len(filtered_df))
col2.metric("Total Spent", f"₹{filtered_df['amount'].sum():,.2f}")
col3.metric("Avg per Expense", f"₹{filtered_df['amount'].mean():,.2f}" if len(filtered_df) > 0 else "₹0")

st.divider()

# Category-wise chart
st.subheader("Spending by Category")
category_totals = filtered_df.groupby('category')['amount'].sum().sort_values(ascending=False)
st.bar_chart(category_totals)

# Daily trend chart
st.subheader("Daily Spending Trend")
daily_totals = filtered_df.groupby('date')['amount'].sum()
st.line_chart(daily_totals)

# Payment mode breakdown
st.subheader("Payment Mode Breakdown")
payment_totals = filtered_df.groupby('payment_mode')['amount'].sum()
st.bar_chart(payment_totals)

st.divider()

# Raw data table
st.subheader("Filtered Expenses")
st.dataframe(filtered_df.sort_values('date', ascending=False), use_container_width=True)