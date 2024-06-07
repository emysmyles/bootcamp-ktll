"""
#FUNCTIONS
----------------------------------
A function is a construct that allows you to group related lines 
of code into a single unit.

You use the 'def' keyword to define a function
Python has some in built function as well
Every function must return a "value".

function takes argument inside the bracket ().
"""


def functionname():
    return 1


def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(4, 6, 7))
print(sum_all_nums(3, 4, 5, 1, 3, 4, 5, 2))


def ensure_correct_info(*args):
    if "Emem" in args and "Jolie" in args:
        return "Welcome back Emem!"
    return "Not sure who you are..."


print(ensure_correct_info())
print(ensure_correct_info("Emem", "Jolie"))

# **kwargs
def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite colour is {color}")


print(fav_colors(colt="purple", ruby="red", ethel="teal"))
