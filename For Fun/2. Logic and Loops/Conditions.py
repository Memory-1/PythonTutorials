"""
When trying to make a task, there may be 2 or more possible inputs/states/conditions that the program can experience.
Say for example if your program had a special welcome for someone who was left handed compared to a right-handed person
then you will have two possible outcomes. This is where conditions come in!

In python we can do conditions in a couple of different ways:
    * If
    * While
    * Switch cases

I won't be going over switch cases, but in short it's a special "tricky" shortcut to check a lot of different conditions

There are special characters to tell the computer that you're trying to compare stuff

Greater Than:           >
Greater Than or Equal:  >=
Equal to:               ==
Less Than or Equal:     <=
Less Than:              <
Not Equal too:          !=

Since we use the "=" to assign values to variables, we use the double "="

FORMAT
if (condition):

If you want to chain a lot of conditions you can do
if (condition):
elif (condition):
elif (condition):
...
else:

elif is else if: it will only trigger if the previous condition wasn't met and that condition is met
else: it will only execute if the previous statement wasn't.
"""


# Example 1
age_of_toby = 70
if age_of_toby >= 65:
    print("Toby get's a discount!")

# Example 2
age_of_toby = 20
if age_of_toby >= 65:
    print("Toby get's a discount!")

""" 
In example 1 it will print out the message, but in example 2 it will skip over the print statement. 
"""

# Elif and Else example

score = 89

if score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
else:
    print("A")

"""
So, it will go through and score is not less 70, so it'll go to the next if and check if it's in the 70's, it's not
so it checks if it's in the 80's and it is so it'll print "B" 
"""


# MULTIPLE CONDITIONS

"""
So, say you need to check if some object is red and a square? Or maybe you'll just need it to be blue or a circle to do 
a specific thing. You're in luck because there are special keywords to do it in one line.

and, or, & not

not is mostly used when comparing datatypes or negating an expression. I would suggest looking up "not" online.
You'll use != more often than 'not' when programming. 
"""
color = "red"
shape = "square"
if color == "red" and shape == "square":
    print("This is the object we were looking for")

color = "blue"
size = "BIG"
if color == 'blue' or size == "small":
    print("One of them is good enough for me")

