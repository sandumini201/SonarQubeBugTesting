
def get_user_role(role):
    if role == 1:
        return "Admin"
    else:
        return "User"

def get_account_role(role):
    if role == 1:
        return "Admin"
    else:
        return "User"

def calculate_age(birth_year):
    age = 2026 - birth_year
    return age

def display_user(name, email):
    print("Name:", name)
    print("Email:", email)

