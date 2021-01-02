"""
There are two kinds of loops that are most common.

1. The While loop: This repeats the code within it until a certain condition is met.

"""

print("\n Printing 0-9 \n")
i = 0
while i < 10:
    print(i)
    i = i + 1
print("Done")

"""
The above will print the number 0 to 99. Once i is equal to 100, the condition i < 100 is no longer true and
the loop will finish. 
"""

"""
2. The For loop: this will loop through each item or element in some collection.

The for loop follows this format

    for ITEM in LIST:
        something
        
You don't have to increment something for the for loop, it will automatically go to the next item in a 
collection
"""

print("\nPRINTING EVEN NUMBERS:")
# I will construct a list here, this is just a fancy shortcut
evens = [i*2 for i in range(5)]

for number in evens:
    print(number)
