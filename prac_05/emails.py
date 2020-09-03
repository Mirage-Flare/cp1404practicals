"""
CP1404/CP5632 Practical
Finding and storing name the name from a email address in a dictionary
"""


def main():
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        name = get_name_from_email(user_email)
        confirmation = input("Is your name {}? (Y/N) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[user_email] = name
        user_email = input("Email: ")
    for user_email, name in email_to_name.items():
        print("{} ({})".format(name, user_email))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
