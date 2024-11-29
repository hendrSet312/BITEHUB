import streamlit as st
from pages.register import register
from pages.recipes import recipe

if "recipe" not in st.session_state:
    st.session_state.recipe = []

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "page" not in st.session_state:
    st.session_state.page = {
        'home': True,
        'register':[False, 0],
        'recipes':[False, 0]
    }

if "recipes" not in st.session_state:
    st.session_state.recipes = []

# Main menu
# menu = ["Home", "Articles and Tips", "Achievement", "Account" ]
# choice = st.sidebar.selectbox("Menu", menu)

# Home Page

def main():
    if st.session_state.page["home"]:
        st.title("BITEHUB")
        st.subheader("Eat healthy without no worries !")
            
        if st.button('Let\'s begin !'):
            st.session_state.page["home"] = False 
            st.session_state.page["register"][0] = True
            st.rerun()

    if st.session_state.page["register"][0]:
        register()
    
    if st.session_state.page["recipes"][0]:
        recipe()


main()
