import random, string

def passwd_validator_generator():
    while True:
        password_issue = input("Press 1 to generate a password or 2 to validate your password: ")

        if password_issue == "1":
            password_generator()
            break
        elif password_issue == "2":
            password_validator()
            break
        else:
            print("Wrong entry. Try again")

def password_generator():

    my_password = ''

    letter_upper = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    letter_lower = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    my_digits = ''.join(random.choice(string.digits) for i in range(3))
    my_punctuation = ''.join(random.choice(string.punctuation) for i in range(3))

    my_password = (letter_lower + letter_upper + my_digits + my_punctuation)
    password = list(my_password)
    random.shuffle(password)
    result = ''.join(password)
    print(result)


def password_validator():
    password_strenght = []
    password = input("Enter password? ")

    right_length = True if len(password) in range(8, 13) else False
    if right_length == True:
        password_strenght += "A"
            
    is_digit = any(char.isdigit() for char in password)
    if is_digit:
        password_strenght += "B"

    is_upper = any(char.isupper() for char in password)
    if is_upper:
        password_strenght += "C"

    is_lower = any(char.islower() for char in password)
    if is_lower:
        password_strenght += "D"

    special_character = any(char in string.punctuation for char in password)
    if special_character:
        password_strenght += "E"

    is_space = True if ' ' in password else False
    if not is_space:
        password_strenght += "F"

    if len(password_strenght) == 6:
        print("Password is very strong.")

    if len(password_strenght) == 5:
        print("Password is strong.")

    if len(password_strenght) == 4:
        print("Password is Fair.")

    if len(password_strenght) == 3:
        print("Password is weak.")

    if len(password_strenght) <= 2:
        print("Password is very weak.")

    if not right_length:
        print("Length of password must be between 8 & 12 characters")

    if not is_digit:
        print("password must contain at least 1 digit.")

    if not is_upper:
        print("Password must contain at least 1 uppercase letter.")

    if not is_lower:
        print("Password must contain at least 1 lowercase letter.")

    if not special_character:
        print("Password has to contain at least 1 special character.")

    if is_space:
        print("Password is not suppose to have a space.")
        print("Note: Password is not valid")



passwd_validator_generator()