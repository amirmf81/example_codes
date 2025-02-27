import re


def validate_company_name_func(name):
    pattern = r"^[\u0600-\u06CC\s]+$"
    if re.match(pattern, name):
        return True
    return False
