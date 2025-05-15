import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("sample_mpan_data_tile7 (1).csv")

st.title("Interactive Energy Dashboard (MPANs)")

# Sidebar Filters
area_codes = st.sidebar.multiselect("Select Area Code", options=df["Area Code"].unique(), default=df["Area Code"].unique())
categories = st.sidebar.multiselect("Select Category", options=df["Category"].unique(), default=df["Category"].unique())
read_flags = st.sidebar.multiselect("Select Is Read Ignored", options=df["Is Read Ignored"].unique(), default=df["Is Read Ignored"].unique())

# Apply filters
filtered_df = df[
    (df["Area Code"].isin(area_codes)) &
    (df["Category"].isin(categories)) &
    (df["Is Read Ignored"].isin(read_flags))
]

# Donut chart: Count of MPANs by Area Code
area_code_counts = filtered_df["Area Code"].value_counts().reset_index()
area_code_counts.columns = ["Area Code", "Count"]

fig1 = px.pie(area_code_counts, values='Count', names='Area Code', hole=0.5,
              title="Count of MPANs by Area Code")

# Bar chart: Count of MPANs by Is Read Ignored and Category
fig2 = px.histogram(filtered_df, x="Is Read Ignored", color="Category",
                    barmode='group', title="Count of MPANs by Is Read Ignored and Category")

# Display charts
st.plotly_chart(fig1)
st.plotly_chart(fig2)
