"""
Making a function

Ex)
def your_function(input_1, input_2):
    ...
    result = input_1 + input_2
    ...
    return result

You will start by using the keyword 'def' to let the program know that that is a function

Then you will have your function name. This is how you will access/use that code later on.

Next, you will have your input. These will be inside parenthesis () and are separated by commas.
One thing which can be confusing is that the name of the variables inside your function dont have to match
when you call it.

    ex)
    def sample_func(input_1):
        return 1

    my_var = 2
    sample_func(my_var)

After the parenthesis' and input. you need a colon. The next line you will tab over. It needs to be indented one
tab more than what the "def" line is.

Inside of the function, you can do anything you coding you'd like. The general rule of thumb is that you use variables
only passed in. You can use variables that are avaialable throughout your whole program such as global variables.
So, if you need something, make sure you define that and pass it in.

Finally, to have your function have an output, you need to use the keyword return and then the thing you wish to return.


"""

def add_two_numbers(input_1, input_2):
    results = input_1 + input_2
    return results


"""
If you need a third number, make sure you define it.
"""