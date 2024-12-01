import streamlit as st

def go_next():
    st.session_state.page['register'][1] += 1
    st.rerun()

def go_back():
    st.session_state.page['register'][1] -= 1
    st.rerun()

def go_edit():
    st.session_state.page['register'][1] = 0
    st.rerun()

def go_recipes():
    st.session_state.page['register'] = [False,0]
    st.session_state.page['recipes'] = [True,0]
    st.rerun()

def pages_1():
    st.title("Step 1: Basic Information")

    with st.container():
        st.write("Provide details about your basic information")
        st.session_state.user_data["age"] = st.number_input("Age", min_value=18, max_value=100, step=1)
        st.session_state.user_data["weight"] = st.number_input("Weight (kg)", min_value=0, step=1)
        st.session_state.user_data["height"] = st.number_input("Height (cm)", min_value=0, step=1)

def pages_2():
    with st.container():
        st.write("Provide details about your lifestyle, goals, budget !")

        st.session_state.user_data["lifestyle"] = st.selectbox(
            "Health Lifestyle", 
            ["Sedentary (little or no exercise)", 
            "Lightly Active (light exercise)", 
            "Moderately Active (moderate exercise)", 
            "Very Active (hard exercise)"]
        )
        st.session_state.user_data["goals"] = st.selectbox(
            "Health Goals", 
            ["Lose Weight", "Maintain Weight", "Gain Muscle", "Improve Fitness"]
        )

        st.session_state.user_data["budget"] = st.selectbox("Budget options",[
            "Low Budget (e.g., $5-$15 per meal, groceries for $100/week)",
            "Medium Budget (e.g., $15-$30 per meal, groceries for $150-$300/week)",
            "High Budget (e.g., $30+ per meal, groceries for $300+/week)",
        ])

        st.session_state.user_data["Restrictions"] = st.multiselect("Diet Restrictions (optional)",[
            "Vegetarian", "Vegan" , "Halal", "Kosher", "Glutten free", "Diary Free", "Pescatarian"
        ])
        
    


def pages_3():
    st.title("Summary and Confirmation")
    st.write("Here is the information you provided:")
    for key, value in st.session_state.user_data.items():
        st.write(f"**{key.capitalize()}**: {value}")
    

def register():
    page_func = [pages_1,pages_2,pages_3]

    page_func[st.session_state.page['register'][1]]()

    if st.session_state.page['register'][1] == 0:
        if st.button("Next"):
            go_next()
            
    elif st.session_state.page['register'][1] == 2 : 
        if st.button("edit"):
            go_edit()
        if st.button("Confirm"):
            st.success("Your information has been successfully submitted!")
            go_recipes()
            
    else : 
        col1, col2 = st.columns(2)
        if st.button("Back"):
            go_back()

        if st.button("Next"):
            go_next()

