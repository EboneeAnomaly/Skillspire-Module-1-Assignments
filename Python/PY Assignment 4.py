num_input = int(input("Pick a number between 1 & 10!: "))
# I assigned my string to 'num_input' and told it to convert the input string to an integer.
if num_input == 8:
    # I set my correct number to 8 and told it that the number is equal to 8, it's correct
    print("You have successfully guessed the number, congrats!")
elif num_input > 8:
    # Here I tell it that if a number is bigger than 8, it's too big and is incorrect.
    print("The number is too big guess again.")
else:
    print("The number is too small guess again.")
    # Finally, I tell that anything else (which would be numbers smaller than 8, is too small and thus incorrect.)