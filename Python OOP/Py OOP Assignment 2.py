class Boxer:
    #Above is my class and below is my constructor
    def __init__(self, Size, Strength, Wins, Losses):
        self.Size = Size
        self.Strength = Strength
        self.Wins = Wins
        self.Losses = Losses
# The constructor function above gives a value to our constructor properties
Boxer_1 = Boxer("6'0 | Light-Heavy Weight,", "Str: 5,", "W: 22,", "L: 0" )
Boxer_2 = Boxer("5'11 | Middle Weight,", "Str: 5,", "W: 33,", "L: 3")
#Above are my objects with the constructor properties applied

print("Boxer 1's stats:", Boxer_1.Size, Boxer_1.Strength, Boxer_1.Wins, Boxer_1.Losses)
print("Boxer 2's stats:", Boxer_2.Size, Boxer_2.Strength, Boxer_2.Wins, Boxer_2.Losses)
# Here I tell the machine to print my objects and the respective information associated with them that I want

userChoice = input("Please Choose Winning Fighter | Type - Boxer_1 or Boxer_2").strip().lower()
# here is where I give the input rules that they user can choose from, and I used two functions at the end
# .strip = ignores spaces ad .lower = ignores case. Just make sure that you make your choice lowercase in the
# if / else statement for it to be recognized
if userChoice == "boxer_1":
    print("Congratulations, you've won your bet!")
else:
    print("Sorry, you've lost your bet.")
#This if / else statement tells the machine that if the user types in
#'boxer_1', to tell them they've won the bet and if they type in boxer_2 they've lost
