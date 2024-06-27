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

"""
create a tuple of 6 email addresses, then write a function that 
takes the tuple as argument. The function will check if the email
is not ending with a ".com". it will change it to a ".com" and 
add it to a list. if it is ending with a ".com", it will simply 
just add it to the list. Then will return the list.

"""
# email_addresses = ("jolie@gmail.com","donnie@aviance.net",
#                    "mime@yahoo.com","mami@nahco.net",
#                    "wasiu@yahoo.com","daddy@gmail.co.uk")

# def

nums =[2,4,6,8,10]
doubles = map(lambda x: x*2, nums)# to turn it into a list
#list(map(lambda x: x*2,nums))
print(doubles)
for num in doubles:
    print(num)

people =["Darcy", "Christina", "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)
print(list(peeps))


