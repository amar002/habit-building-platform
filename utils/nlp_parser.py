def parse_habit_input(habit_text):
    words = habit_text.split()
    habit_name = " ".join(words[:-2]) if len(words) > 2 else habit_text
    frequency = "daily" if "every" in words else "one-time"
    return {
        "habit_name": habit_name,
        "frequency": frequency
    }
