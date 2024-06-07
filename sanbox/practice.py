# def print_full_name(first_name, last_name):
#     print(first_name + " " + last_name)


# def print_full_name_with_return(first_name, last_name):
#     return first_name + " " + last_name

# first_name = "Emem"
# last_name = "Udofia"
# print_full_name("john", 'doe')
# print_full_name("doe", 'john')  # positional argument
# print_full_name(last_name="doe", first_name='john')  # keyword argument
# print(print_full_name_with_return("john", "doe"))


# print_full_name(first_name, last_name)
# print(print_full_name_with_return(first_name, last_name))



# def square(num):
#     return num * num

# print(square(4))


# def sing_happy_birthday(name):
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print(f"Happy birthday to dear {name}")
#     print("Happy birthday to you")
# sing_happy_birthday("Emem")

#DEFAULT PARAMETERS
def exponent(num, power):
    return num ** power

print(exponent(2,4))
print(exponent(5,5))

def exponent(num, power=2):
    return num ** power

print(exponent(9))


# example 2
def add(a=10, b=13):
    return a + b

print(add(11, 28))
print(add())

# example 3
def show_information(first_name="colt", is_instructor = False):
    if first_name == "colt" and is_instructor:
        return "welcome back instructor colt"
    elif first_name == "colt":
        return "i really thought you were an intructor..."
    return f"Hello {first_name} !"
print(show_information())
print(show_information("eme"))
print(show_information(is_instructor=True))
