import streamlit as st
from restaurant_generator import generate_restaurant_name_and_items

st.title("Restaurant Name & Menu Generator")

cuisine = st.text_input("Enter a cuisine type (e.g., Italian, Chinese, Mexican):")

if st.button("Generate"):
    if cuisine:
        response = generate_restaurant_name_and_items(cuisine)
        st.subheader("🍽️ Restaurant Name")
        st.write(response["restaurant_name"])
        st.subheader("📋 Menu")
        st.write(response["menu_items"])
    else:
        st.warning("Please enter a cuisine type.")
