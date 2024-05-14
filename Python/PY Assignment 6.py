
import random
tries = 0
max_tries = 2
nums = [1, 2, 3, 4, 5, 6]
# I used a choice module to have it to pick a number in the list at random.

while tries < max_tries:
    user = int(input("Pick a number between 1 and 6"))
    dice_roll = random.choice(nums)
    tries += 1

    if user == dice_roll:
     print("You have successfully rolled:",dice_roll)
     break

else:
    print("Sorry, please roll again. If max tries, start again.")

if tries == max_tries:
    print("sorry, you've reached max tries:", max_tries)

    #I used conditonal statements to create the outcome if the player picked the right number, the wrong number, or went over a certain amount of tries.