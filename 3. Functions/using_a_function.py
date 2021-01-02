"""
Using a function

Using a function or often referred to as calling a function, is simple.
You simply type the name of your function followed by parenthesis with your input inside.

If you want to save the output you'll just assign it to a variable. Below is an example.


"""


def add_two_numbers(num1, num2):
    return num1 + num2


def doubler(num1):
    return num1*2

result_1 = add_two_numbers(1,2)
print(doubler(2))


"""
You can even pass a function as an input!
 
"""

#This should equal to 30
print("The result of a function passed into a function: \n" + add_two_numbers(doubler(1), doubler(14)))