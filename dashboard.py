import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("sample_mpan_data_tile7 (1).csv")

st.set_page_config(layout="wide")
st.title("Interactive Energy Dashboard (MPANs)")

# Sidebar Filters
with st.sidebar:
    st.header("Filters")
    area_codes = st.multiselect("Select Area Code", options=sorted(df["Area Code"].dropna().unique()), default=df["Area Code"].dropna().unique())
    categories = st.multiselect("Select Category", options=sorted(df["Category"].dropna().unique()), default=df["Category"].dropna().unique())
    read_flags = st.multiselect("Select Is Read Ignored", options=sorted(df["Is Read Ignored"].dropna().unique()), default=df["Is Read Ignored"].dropna().unique())

# Apply filters
filtered_df = df[
    df["Area Code"].isin(area_codes) &
    df["Category"].isin(categories) &
    df["Is Read Ignored"].isin(read_flags)
]

# Donut Chart: Count of MPANs by Area Code
area_code_counts = filtered_df["Area Code"].value_counts().reset_index()
area_code_counts.columns = ["Area Code", "Count"]
fig1 = px.pie(area_code_counts, values='Count', names='Area Code', hole=0.5,
              title="Count of MPANs by Area Code")

# Bar Chart: Count of MPANs by Is Read Ignored and Category
fig2 = px.histogram(filtered_df, x="Is Read Ignored", color="Category",
                    barmode='group', title="Count of MPANs by Is Read Ignored and Category")

# Display Charts
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
