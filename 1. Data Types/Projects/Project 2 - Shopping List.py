"""
Some things to be aware. Python is indent sensitive. Inside of the if and else statement, you need to make sure
that your statement is indented (As far right as the TODO statements.

I use while, if, and else. I haven't talked about these yet so briefly.
while: As long as the condition inside of () is correct/true, it will continue to repeat the code inside of it.
if: if the condition inside of the if is true, then it will execute the code in that "scope" (the same indentation)
otherwise, it will execute the code inside of the else.
"""

List = []
keep_going = True
print("Please enter your items or press enter if list is done")
while (keep_going == True):
    temp = input('Item: ') # This will just display Item: , but it won't save "Item: " to the temp variable.
    if temp == "":
        # TODO: What to do if the item is empty ("")
    else:
        # TODO: Add an item to a list

# TODO: Print the list
print(List)


"""
One step further is to have this to read and write to a file. That way every time you launch this file, it will
retain all that you've added from the last time. This may be a later project :) 
"""
