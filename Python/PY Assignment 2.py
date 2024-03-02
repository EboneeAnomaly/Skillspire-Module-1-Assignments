artSupplies = ['Copics', 'Charcoal', 'Sketchpad', 'Paints', 'Canvas', "Eisel", 'Pencils', 'Palette', 'Drawing Tablet', 'Lightbox' ]
# I initiated my array and assigned it to the variable 'artSupplies'
fiveSupplies = [5, 6, 7, 8, 9,]
# here I told it the specifc parts of the array I wanted to target
for index in fiveSupplies:
    print(artSupplies[index])
    
    #I created a loop here to go through the array, and print back the targeted elements

    # At first I was going to use print console five times, but them I remebered that in that case
    # it's best to use a loop. I had to use chatGTP to learn the PY loop syntax, but it came easier than I thought.

#----- Part Two:
    #I just tweaked the code from above.
artSupplies2 = ['Copics', 'Charcoal', 'Sketchpad', 'Paints', 'Canvas', "Eisel", 'Pencils', 'Palette', 'Drawing Tablet', 'Lightbox' ]

sevenSupplies = [3, 4, 5, 6, 7, 8, 9,]

for index2 in sevenSupplies:
    print("3-10: " + artSupplies2[index2])

#to be able to better tell it apart from the above code, I added '3-10'.