import langchain_logic as lch
import streamlit as st

st.sidebar.image('.\images\sprink_logo.jpg', width= 240) 
st.title("Sprink Quote Generator")
st.date_input("Todays date")
st.slider('Slide me', min_value=0, max_value=10)