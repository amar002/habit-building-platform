import streamlit as st

habit_suggestions = {
    "Health": ["Drink 2L water daily", "Walk 10,000 steps", "Stretch for 5 minutes"],
    "Education": ["Read 15 pages daily", "Review one chapter", "Learn 5 new words"]
}

def get_personalized_habits(focus_areas):
    suggestions = []
    for area in focus_areas:
        suggestions.extend(habit_suggestions.get(area, []))
    return suggestions

def display_suggestions():
    st.write("### Personalized Habit Suggestions")
    focus_areas = ["Health", "Education"]  # Replace with dynamic user focus areas
    suggested_habits = get_personalized_habits(focus_areas)
    for habit in suggested_habits:
        st.write(f"✅ {habit}")
        if st.button(f"Add '{habit}' to My Habits", key=habit):
            st.session_state.habits_data.append({"name": habit, "due": "Today", "status": "Pending"})
            st.success(f"Habit '{habit}' added successfully!")
