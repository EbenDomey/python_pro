import string
import random as rd


def password_generator(d):
    """this function creates a password containing numbers,letters and strings with a randomizing algorithm

    Args:
        d (number): sets the length of the password

    Returns:
        string: a string representation of a password with numbers, strings and symbols
    """
    letters_list = string.ascii_lowercase
    number_list = string.digits
    characters_list = string.punctuation
    passTemplate = letters_list + letters_list.upper() + number_list + characters_list

    passList = rd.choices(passTemplate, k=d)
    password = "".join(str(e) for e in passList)
    return password


passLength = int(input("Enter the desired length for your password: "))
print("Your password is: " + password_generator(passLength))
