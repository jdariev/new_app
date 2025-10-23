import streamlit as st
import appdirs as ad
ad.user_cache_dir=lambda *args: "/tmp"
st.title("Welcome to IUJ.")
st.write('The best University')

# Add a calendar (date input)
st.date_input("Select a date")
