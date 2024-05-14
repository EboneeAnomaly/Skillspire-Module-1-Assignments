print("Welcome to Rock, Paper, Scissors!")
# I made a small declaration message that lets the user know what they're playing.

options = ['rock', 'paper', 'scissors']
# I then provided the options for the 'com player' to go through.

import random

while True:
    com = options[random.randint(0, 2)]
    user = input("Please choose: Rock, Paper, or Scissors? Type exit to quit.").lower()
    # I used a randint module to randomize between the range given 0-3.

    if user == "exit":
        print("Thanks for playing, try again sometime!")
        break
    if user not in options:
        print("Not a valid choice. Please try again.")

    if user == com:
        print("It's a tie!")
    elif user == "rock":
        if com == "paper":
            print("Sorry, you lose Paper covers rock.")
        else:
            print("You win! Rock smashes Scissors!")
    elif user == "paper":
        if com == "scissors":
            print("Sorry, you lose. Scissors cut Paper.")
        else:
            print("You win! Paper covers Rock!")
    elif user == "scissors":
        if com == "rock":
            print("Sorry, you lose. Rock smashes Scissors.")
        else:
            print("You win! Scissors cut paper!")

        # I used conditional statements to provide the win/lose conditions.

# I was able to get this to work in my the terminal outside of VSCode, but for some reason it wouldn't work here.
