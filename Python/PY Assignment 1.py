name = "Ebonee Singleteary"
# Here I put my first name and surname into a string and assigned them the variable
# 'name'
surname = name.endswith("Singleteary")
# I then assigned the variable surname to the result of the .endswith function, which
# allows me to check if what's in the quotes is in the 'name' string. It returns a 
# boolean and in this case it's 'true' because my last name is provided in the string.
print(surname)
# Then I print it to the terminal

# ---- Part Two:

userName = "Eb94"

uNameCheck = userName.isalnum()
# I used the .isalnum function, because it checks to see if there are both letters and numbers
# and returns a boolean based on that. It returns true, because my 'username' contains both letters and numbers.
print(uNameCheck)



