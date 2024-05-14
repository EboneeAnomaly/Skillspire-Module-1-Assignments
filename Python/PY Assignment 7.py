units_sold = int(input('Please enter number of units sold:'))

# I assigned the variable 'units_sold' to the input so that whatever the user input would be calculated by the values below.
#I also told it to convert strong to integer.

if units_sold >= 10 and units_sold <=19:
    discount = 0.2
elif units_sold >= 20 and units_sold <=49:
    discount = 0.3
elif units_sold >= 50 and units_sold <=99:
    discount = 0.4
elif units_sold >= 100:
    discount = 0.5
else:
    discount = 0
# I used conditional statements to decide what discount should be applied to the given value

price_per_unit = 99
total_price = units_sold * price_per_unit * (1 - discount)
# I set the unit price, and gave it the equation to run for the total

print("Total price for",units_sold,"is",total_price)
# I told it print the total along with this string.