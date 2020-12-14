# What is a string?

# A string is basically how you can tell a computer to use a word.
# You can think of a string as basically a bunch of characters (numbers, letters, symbols, etc...)
# connected by a string.
String_ex_1 = 'This uses single quotes'
String_ex_2 = "These are double quotes"


# Above, I made a string two different ways, one with single quotes and the other with double

###################
#                 #
###################

###################
# Printing a word #
###################

# If you want to see a string stored in a variable you can use the print() method to have it output to the console

#Example 1 - Just entering in something into print will send it
print("Printing a word example")
print("hello")
print() #This is just adding a blank line

print("print a variable example")
something = "I'm a variable!"
print(something)
print()

###################
# Combining words #
###################

word_1 = "Hi there, my name is "
word_2 = "Kyle"
combined_words = word_1 + word_2
print("Combining Strings Example")
print(word_1 + word_2)
print(combined_words)
print()
# If you have two strings and want to put them together you can use a plus sign "+" to combine them


###################
#      Extra      #
###################

# There are special characters that mean different things to the computer

# New line - '\n'
# If you add \n to a string and print it, it will make a new line instead of printing out \n

#Example
print("New Line Example")
print("I'm line 1 \n I am line 2")