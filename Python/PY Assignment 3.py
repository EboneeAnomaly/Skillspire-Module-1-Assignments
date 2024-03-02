sum = 0
for index in range(1,16):
    # the range function won't include the last value, so here I put 16
# so that it would count 15.
    sum += index

    print(sum)
    

    
#------ Part Two:
    

evenOdd = range(1, 101)   
# I gave it a range of numbers, I went up to 101 so that 100 would be counted
for i in evenOdd:
    if i % 2 == 0:
        # I recycled code from my JS assignment and adapted it to PY. 
        print(f"{i} Fizz")
    else:
     print(f"{i} Buzz")


