import streamlit as st

st.title("Weather forecast for the next few days")

place = st.text_input("enter the location")

days=st.slider("number of days",min_value=1,max_value=5,
               help="select the number of days from today to see forecast of")

options = st.selectbox("select a way to view data",("temperature","clouds"))

st.subheader(f"{options} forecast for the next {days} days in {place}")