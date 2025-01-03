import streamlit as st
from utils.nlp_parser import parse_habit_input

def display_nlp_creation():
    st.write("### Create Habit from Natural Language")
    habit_input = st.text_input("Describe your habit:")
    if st.button("Create Habit"):
        if habit_input.strip():
            parsed_habit = parse_habit_input(habit_input)
            st.session_state.habits_data.append({
                "name": parsed_habit["habit_name"],
                "due": parsed_habit["frequency"],
                "status": "Pending"
            })
            st.success(f"Habit '{parsed_habit['habit_name']}' added successfully!")
        else:
            st.error("Please enter a valid habit description.")
