"""
Dictionaries are key value pairs. They're great for storing information for a particular thing and being able to quickly
access it without even knowing it's index

Once again, you can store anything for the value in the key-value pair, but the key must be either a string or an int
"""

Dictionary_1 = {}   # Making one
Dict_with_items = {'a_number': 1, 'some_strimg': "I'm a string!", 'a list': [1,2,3], 'tuples!': ('a','b','c')}
Person = {"age": 30, 'name': "Joe", "children":('amy','bob','sue'), 'job': "Yellow jelly bean tester"}

"""
Accessing values in a dictionary

Technique 1: some_dict.get("key")
Technique 2: some_dict["key"]
"""

print("NAME: " + Person['name'])
print("JOB: " + Person.get('job'))
print()

""" Updating/Adding 

To update there are two methods either
1. Calling the index with some_dict['name'] and assign a value
2. use the update method and enter in a new dictionary to add 
"""

Ex_1 = {}
Ex_1['name'] = 'Floyd'
print(Ex_1)
print()

Ex_2 = {}
Ex_2.update({"name": "Jeff"})
print(Ex_2)
print()