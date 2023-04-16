import string as s
import random

def generate_func():
    characters = list(s.ascii_letters+s.digits+"!@#$%^&*")

    password_length = int(input("Enter the how long password do want? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(characters)

    password = "".join(password)

    print(password)
option = input("If You Want Password (Yes/No)? ")
if option == "Yes":
    generate_func()
elif option == "No":
    print("byee")
    quit()
else:
    print("Input is invalid")

