MINIMUM_LENGTH = 4


def main():
    get_password()


def get_password():
    password_input = input("Password: ")
    password_length = len(password_input)
    print_asterisks(password_length)


def print_asterisks(password_length):
    if password_length < MINIMUM_LENGTH:
        password_input = input("Password: ")
    print(password_length * "*")


main()
