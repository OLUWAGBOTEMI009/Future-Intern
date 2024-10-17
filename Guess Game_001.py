# Number Guessing Game

# importing the module "Random"

import random

# creating the random number from 1 to 100
Guess_Number = random.randint(1,101)


# SET THE INITIAL NUMBER OF GUESS TO BE 1
number_guess = 1
# prompt the user to enter the number they guess
guess = int(input("Enter a guess "))

# writing the code for implementing if the number guessed is right or wrong

while (guess != Guess_Number):
    if (guess > Guess_Number):
        print("The number is less than" , str(guess))
    else:
        print("The number is greater than" , str(guess))
    number_guess += 1
    guess = int(input("Enter a guess "))


# print the congratulatory message
print("Right!, the number is" , str(Guess_Number))

# print the number of times the user guess the number correctly

print(" You guess the number correctly" , "at the " , str(number_guess) + "th", "times")


