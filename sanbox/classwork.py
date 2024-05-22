# msg = input ("what's the secret password?")
# while msg != "bananas":
#     print("WRONG")
#     msg = input ("what's the secret password?").lower()
# print("CORRECT")

# for num in range(1,11):
#     print(num)

# num = 1
# while num < 11:
#     print (num)
#     num += 1

# for x in range(3):#this prints the result 3 times
#     for num in range(1,10):
#         print("\U0001f600" * num)

# times = 1
# while times < 11:
#     print("\U0001f600" * times )
#     times += 1  

#without string multiplication
# for num in range(1,11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "\U0001f600" 
#         count += 1
#     print()


# times = 1
# while times < 11:
#     print("\U0001f600" * times )
#     times += 2  

# msg = input("say something: ")

# while msg != "stop copying me":
#     print(msg)
#     msg = input()
# print("UGH FINE YOU WIN, BROTHER!")

#OR
# msg = input("say something: ")

# while msg != "stop copying me":
#     msg = input(f"{msg}\n")
# print("UGH FINE YOU WIN, BROTHER!")


# import random

# random_number = random.randint(1,10)
# msg = None

# while msg != random_number:
#     msg = input("pick a number from 1 to 10: ")
#     msg = int(msg)
#     if msg > random_number:
#         print("too high")
#     elif msg < random_number:
#         print("you are too low")
#     else:
#         print("you got it")

#         print(random_number)
#         game = input("do you wanna continue?: (y/n) ")
#         if game == "y":
#             random_number = random.randint(1,10)
#             msg = None
#             # msg = input("pick a number from 1 to 10: ")
#             # msg = int(msg)
#         else:
#             print("thank you for playing!")





""" 
create a dictionary of at least 3 flowers with at least 
2 features of each
"""
flowers = {"hibiscus":{"colour": "pink",
                       "smell": "nice",
                       "beautiful": True,
                       "botanical_name": "tali"},
           "queen_of_the_night":{"colour":"purple",
                                 "smell": "mild",
                                 "beautiful": True,
                                 "botanical_name":"lalu"},
           "rose":{"colour":"red",
                   "smell":"lovely",
                   "beautiful": True,
                   "botanical_name":"orling"} 
           }
print(flowers)

print("-------k,v--------")

for k,v in flowers.items():
    print(k,v)

print("keyyysssssssss")
for k in flowers.keys():
    print(k)

print("valuesssssss")
for values in flowers.values():
    print(values)

print(flowers["hibiscus"]["botanical_name"])# to get the botanical name of hibiscus

"""
create a dcitionary of account details of customers of
a bank.You can use the different customer acct number as 
keys and each acct number may have up to 3 properties
"""
account_details ={"acct_number1":{"name":"joseph",
                                  }}