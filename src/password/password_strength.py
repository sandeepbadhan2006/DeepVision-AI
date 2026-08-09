import re

def check_password(password):

    score = 0

    breakdown = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "number": False,
        "special": False,
        "repeat": True
    }

    # Minimum Length
    if len(password) >= 8:
        breakdown["length"] = True
        score += 20

    # Uppercase
    if re.search(r"[A-Z]", password):
        breakdown["uppercase"] = True
        score += 20

    # Lowercase
    if re.search(r"[a-z]", password):
        breakdown["lowercase"] = True
        score += 20

    # Number
    if re.search(r"\d", password):
        breakdown["number"] = True
        score += 20

    # Special Character
    if re.search(r"[!@#$%^&*()_\-+=<>?/{}\[\]|\\:;.,~`]", password):
        breakdown["special"] = True
        score += 20

    # Repeated Characters (aaa, 111, $$$ etc.)
    if re.search(r"(.)\1{2,}", password):
        breakdown["repeat"] = False

    # Final Prediction
    if score <= 40:
        prediction = "Weak"

    elif score <= 80:
        prediction = "Medium"

    else:
        prediction = "Strong"

    return prediction, score, breakdown