MINIMUM_LENGTH = 4

password_input = input("Password: ")
password_length = len(password_input)
if password_length < MINIMUM_LENGTH:
    password_input = input("Password: ")
print(password_length * "*")
