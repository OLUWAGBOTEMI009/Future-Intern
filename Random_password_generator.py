# A Simple Random Password Generator.

# import the module
import random

# set the types of password options available
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*._"






length = int(input("Enter the length of the password "))


string = upper + numbers +  symbols +  lower

password = "".join(random.sample(string, length))


print("Your new passowrd is:", password)
