import pandas as pd
import plotly_express as px
import streamlit as st


car_ad_data = pd.read_csv('vehicles_us.csv')

st.header('created a table grouping model and year and geting the average price')
a = car_ad_data.groupby
(['model', 'model_year'])['price'].mean().reset_index()
fig = px.scatter(a, x="model_year", y="price", color="model")

st.write(a)
st.plotly_chart(fig, use_container_width=True)
