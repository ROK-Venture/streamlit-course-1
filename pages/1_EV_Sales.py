import streamlit as st
from utils import load_data, create_sales_pie_chart, top10_sales_by_country
import plotly

#load data
ev_sales_df, ev_sales_share_df = load_data()

#page config
st.set_page_config(
    page_title="EV Sales",
    page_icon="🚗",
)

#title
st.title("🚗🔌EV Sales🔌🚗")

st.divider()

st.subheader("🚗🔌EV Sales by Region🔌🚗")

region = st.selectbox("Select a region", ev_sales_df["region"].unique())

filtered_df = ev_sales_df[ev_sales_df["region"] == region]

st.bar_chart(filtered_df, x="year", y="value", color="powertrain")

st.divider()

st.subheader("🚗🔌Top Sales by Country 2023🔌🚗")

top_sales_by_country_df = top10_sales_by_country(ev_sales_df)
st.divider()


# Use the function instead of inline configuration
st.subheader("Top 10 Countries by EV Sales - Pie Chart")
fig = create_sales_pie_chart(top_sales_by_country_df)

#create two columns
col1, col2 = st.columns([1.8, 1]) 

col2.dataframe(top_sales_by_country_df)

#show the pie chart in the first column
col1.plotly_chart(fig)

# ev sales by conuntry comparison
st.subheader("🚗🔌EV Sales by Country Comparison🔌🚗")

st.divider()

countries = st.multiselect("Select a country", ev_sales_df["region"].unique(), default=["Germany", "France", "Spain"])

sales_comparison_df = ev_sales_df.copy()

sales_comparison_df = sales_comparison_df[sales_comparison_df["region"].isin(countries)]

st.divider()

powertrain = st.selectbox("Select a powertrain", ev_sales_df["powertrain"].unique())

sales_comparison_df = sales_comparison_df[sales_comparison_df["powertrain"] == powertrain]

#create a linechart
st.line_chart(sales_comparison_df, x="year", y="value", color="region")



