import spacy

nlp = spacy.load("en_core_web_sm")

def parse_habit_input(habit_text):
    doc = nlp(habit_text)
    habit_name = []
    frequency = None

    for token in doc:
        if token.dep_ in ("ROOT", "dobj", "compound"):
            habit_name.append(token.text)
        elif token.ent_type_ == "DATE":
            frequency = token.text

    return {
        "habit_name": " ".join(habit_name),
        "frequency": frequency or "daily"
    }
