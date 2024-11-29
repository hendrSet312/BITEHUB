import streamlit as st
import datetime

def recipe():
    st.header('Recipes')
    st.write("Fill out the details below to add a new recipe.")

    flavour_preferences = st.multiselect("Cuisine preferences", placeholder=[
        "Chinese", "French", "Mexican", "Korean","American","European","African"
    ])

    cooking_time = st.selectbox(
            "Cooking time", 
            ["Quick (15 minutes)", "Regular (15-30 minutes)", "Leisure (> 30 minutes)"]
    )

    weather = st.selectbox(
            "Weather today", 
            ["Cold", "Rainy", "Humid", "Windy", "Hot"]
    )

    # if st.button("Add Recipes"):


    ## keluar resepnya dibawah 



