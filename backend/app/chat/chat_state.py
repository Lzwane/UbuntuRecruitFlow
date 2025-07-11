cv_data = {
    "name": None,
    "surname": None,
    "address": None,
    "email": None,
    "cell_number": None,
    "industry_interest": None,
    "interests": [],
    "skills": [],
    "projects": [],
    "experience": [],
    "education": []
}

conversation_state = {
    "started": False,
    "stage": "basic",
    "current_question_index": 0,
    "temp_entry": {},
    "awaiting_another_entry": False
}

#questions are stored in tuple
basic_questions = [
    ("name", "What is your first name?"),
    ("surname", "What is your surname?"),
    ("address", "What is your address?"),
    ("email", "What is your email address?"),
    ("cell_number", "What is your cell phone number?"),
    ("industry_interest", "Which industry are you interested in?"),
    ("interests", "List your personal interests (comma-separated):"),
    ("skills", "List your professional skills (comma-separated):"),
    ("projects", "List your projects (comma-separated):")
]
