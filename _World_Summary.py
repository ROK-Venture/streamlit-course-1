import streamlit as st
from utils import load_data

#load data 
ev_sales_df, ev_sales_share_df = load_data()

# page config
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="centered",
    page_icon="🚗",
    initial_sidebar_state="expanded"
)

# title
st.title("🚗🔌EV Adoption Tracker")

#header
st.header("🗺️World Summary🗺️")

#expander
with st.expander("Where does the date come from", expanded=False):
    st.write("The data for this app is sourced from ... .")
    st.write("The data set can be found - LInk.") 


#card metrics
col1, col2, col3 = st.columns(3)

card1 = col1.container(border=True)
card2 = col2.container(border=True)
card3 = col3.container(border=True)

card1.metric("Metric Name", "42%",2)
card2.metric("Metric Name", "42%",2)
card3.metric("Metric Name", "42%",2)


st.subheader("🚗🔌World Sales🔌🚗")
st.divider()

world_sales_df = ev_sales_df[ev_sales_df["region"] == "World"]

st.bar_chart(world_sales_df, x="year", y="value", color="powertrain")



# #display the data
# st.dataframe(ev_sales_df.head(10))
# st.dataframe(ev_sales_share_df)