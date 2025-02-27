import re


def validate_username_func(username):
    pattern = r"^[a-zA-Z0-9 ]+$"
    if re.match(pattern, username):
        return True
    return False
