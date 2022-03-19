from email import charset
import random
from ssl import _PasswordType
# imports random module

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!@#$%&*";
# characters given will import

print("PASSGEN 1.0 ver 1.1.0.0");
# Describes programs

while 1:
    password_len = int(input("What length would you like your password be?"))
    # Ask users length of passwords
    password_count = int(input("How many passwords do you like to generate"))
    # Ask users how many passwords would the user want to generate
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password       = password + password_char
            # Generates password
        print("Here is your password, " , password)

