# Rock, paper, scissors game


# import the random module
import random

# store the player's choice
choices = ("rock", "paper", "scissors")

run = True


# creating the while loop for the player's choices and the rules of the game.

while run:
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

            # setting the rules of the game.
    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    # If the player wants to continue playing or not.
    play_again = input("Play again? (yes/no): ").lower()
    if not play_again == "yes":
        run = False

print("Thanks for playing!")
