# Instruction
# ---------------------------------------------------------------
# Remember you are to do your solutions in the solutions folder
# Create a file with the exact same file name
# You can copy the questions from here down there
# But don't type anything inside this file

"""
# Question 1
------------------------------------------------------------------
Create a variable called `username`.
Using a python function check the length of the string in the variable
and use the result as follows:
- a case that the length is smaller than 3, print "Invalid username. Must be at least 3 characters long"
- a case that the lenght is greater than 15, print "Invalid username. Must be at most 15 characters long"
- a case where the two conditons are not meet, print "Valid username"
"""

#ANSWER TO QUESTION 1
username = "jolie"
length_of_username =len(username)
print (length_of_username)

if len(username) < 3:
    print("Invalid username")
if len(username) > 15:
    print("Invalid username")
elif len(username) > 3:
    print("Valid username")
elif len(username) < 15:
    print("Valid username")

""" 
# Question 2
------------------------------------------------------------------
Create a variable and assign any integer value to it.
Check whether is even and print "Even number".
In a case that the number is not even, print "Odd number".

TIP: to check whether a number is even use the modulo operator.
"""


#ANSWER TO QUESTION 2
Number = 9
print (Number % 2) #if this brings a remainder,that means its an odd number
if (Number % 2) == 0:
    print("Even number")
else:
    print("Odd number")


"""
# Question 3
------------------------------------------------------------------
Create a variable called `happy` and assign an integer to it.
If the number in that variable is greater than 6, print "Hello World!!!"
but if the number is less than 6, print "Hi World!!!"
"""

#ANSWER TO QUESTION 3
Happy = 10
if Happy > 6:
    print("Hello world") 
else:
    print("Hi world")

