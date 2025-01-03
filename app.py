import streamlit as st
from components.personalized_suggestions import display_suggestions
from components.natural_language_creation import display_nlp_creation
from components.habit_dashboard import display_dashboard
from utils.data_handler import load_habits, save_habits

# Initialize session state
if "habits_data" not in st.session_state:
    st.session_state.habits_data = load_habits()

st.title("HabitFlow")
st.subheader("Build small habits, achieve big goals.")

# Navigation
menu = st.sidebar.selectbox("Menu", ["Dashboard", "Add Habits", "Suggestions"])

if menu == "Dashboard":
    display_dashboard(st.session_state.habits_data)
elif menu == "Add Habits":
    display_nlp_creation()
elif menu == "Suggestions":
    display_suggestions()

# Save data on app exit
save_habits(st.session_state.habits_data)
