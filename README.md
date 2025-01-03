# HabitFlow: Habit-Building Platform

**HabitFlow** is a Streamlit-powered platform designed to help users build and track habits, achieve goals, and stay motivated. The platform includes personalized habit suggestions, natural language habit creation, and a user-friendly dashboard.

---

## **Features**

### 🗂️ **Dashboard**
- View and manage your habits.
- Mark habits as completed.
- Track progress with visual indicators.

### 💡 **Personalized Habit Suggestions**
- Get habit recommendations based on your focus areas (e.g., Health, Education).

### ✍️ **Natural Language Habit Creation**
- Create habits by describing them in plain English (e.g., "Walk 5,000 steps every day").

### 🔔 **Reminders**
- (Planned) Set reminders for habits and receive notifications.

### 📊 **Analytics**
- (Planned) Track streaks, completion rates, and weekly progress.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/habit-building-platform.git
   cd habit-building-platform
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## **Directory Structure**

```
habit-building-platform/
│
├── app.py                   # Main Streamlit entry point
├── data/
│   └── habits_data.json     # Stores habit data for persistence
│
├── components/
│   ├── __init__.py          # To make the folder a module
│   ├── personalized_suggestions.py  # For habit suggestions
│   ├── natural_language_creation.py # For NLP-based habit creation
│   └── habit_dashboard.py   # Dashboard-related logic
│
├── utils/
│   ├── __init__.py          # To make the folder a module
│   ├── data_handler.py      # For reading/writing habit data
│   ├── nlp_parser.py        # NLP parsing for habit creation
│   └── reminder_utils.py    # Reminder management
│
└── assets/
    └── logo.png             # Platform logo and other images
```

---

## **Requirements**

The following libraries are required to run HabitFlow:

```
streamlit
spacy
matplotlib
streamlit-echarts
```

Install them via:
```bash
pip install -r requirements.txt
```

---

## **Future Enhancements**
- Streak tracking and detailed analytics.
- Integration with voice assistants for hands-free habit tracking.
- AI-powered habit difficulty analysis and optimization.

---

## **Contributing**
Feel free to fork the repository and submit pull requests for improvements or bug fixes. Contributions are always welcome!

---

## **License**
This project is licensed under the MIT License.
