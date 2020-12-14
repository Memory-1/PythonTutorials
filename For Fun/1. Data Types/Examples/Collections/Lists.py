"""
Lists:

Lists are a collection of different items. You can have shopping list, to-do list, etc

Lists can hold whatever you want and you can add, remove, or change items in it.
(In python you can mix different data types in a list.)

Lists can be made by using square brackets [] and each item needs to be seperated by a comma
"""


"""
Making lists examples
"""
Ex_1 = ['Eggs', 'Milk', 'Bread']

Ex_2 = [1, 2, 3, 4, 5]

Ex_nested_lists = [ ['Toby', 'Michael', 'Kevin'], ['SpiderMan', "Bat Man", "Super Man"], ['Fido', 'Gato', 'Roboto']]


"""
Adding to a list

You can use the append method that lists have in order to add. 
(If you need a refresher on the methods and what the '.' means, refer to 0. Background
"""
List_1 = [1,2,3]
print("Before Adding:")
print(List_1)
print()

List_1.append(4) #This will put 4 at the end of the list.
print("After Adding:")
print(List_1)
print()

"""
Modifying a list

Each item in the list has an index on how to access it. You access by [4]

Also, Indexes start counting at 0, so the first item in a list is 0, second is 1.
"""

Modifying_Ex = [1,2,3]
print("Before Modifying:")
print(Modifying_Ex)
print()

Modifying_Ex[0] = 'I changed!'
print("After Modifying:")
print(Modifying_Ex)
print()

"""For nested lists, you can keep adding index numbers to the end."""

Ex_nested_lists = [ ['Toby', 'Michael', 'Kevin'], ['SpiderMan', "Bat Man", "Super Man"], ['Fido', 'Gato', 'Roboto']]
# This will access the second list of names and then access the first item in that second list
print(Ex_nested_lists[1][0])