import re


def validate_password_func(password):
    pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{6,}$"
    if re.match(pattern, password):
        return True
    return False
