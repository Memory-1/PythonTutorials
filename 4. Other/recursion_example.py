"""

Recursion is one of those things in coding which can be confusing. Once you understand what's going on though, can be
pretty cool in my opinion.

Honestly, recursion isn't used very often. But, once again, to be able to understand it will be helpful.

Recursion is basically a function calling itself over and over to solve a problem. Below is an example of that.

I will make a recursive function to calculate triangle numbers (1+2+3+4+5...)

"""


def recursive_adder(num):
    if num == 1:
        return 1
    else:
        return num + recursive_adder(num-1)


print(recursive_adder(5))
print(recursive_adder(100))




