# import random
# # you can also use from random import randint
# print("rock....")
# print("paper....")
# print("scissors...")

# player = input("player, make your move: ").lower()#turns evrything to lowercase
# rand_num = random.randint(0,2) # here you can use only random if line 2
# if rand_num == 0:
#     computer = "rock"
# elif rand_num == 1:
#     computer = "paper"
# else:
#     computer = "scissors"
# print("computer plays", computer)

# if player == computer:
#     print("its a tie!")
# elif player == "rock":
#     if computer == "scissors":
#         print("player wins!")
#     else:
#         print("computer wins!")
# elif player == "paper":
#     if computer == "rock":
#         print("player wins!")
#     elif computer == "scissors":
#         print("computer wins!")
# elif player == "scissors":
#     if computer == "rock":
#         print("computer wins!")
#     elif computer == "paper":
#         print("player wins!")
# else:
#     print("pls enter a valid move")


"""
write a code to loop the rock, paper scissors
"""
import random

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score: 
    print(f"player score:{player_wins} computer score:{computer_wins}")
#for time in range(3):  # this sets the number of times the loop runs
    print("rock....")
    print("paper....")
    print("scissors...")

    player = input("player, make your move: ").lower()  # turns evrything to lowercase
    if player == "quit":
        break
    rand_num = random.randint(0, 2)  # here you can use only random if line 2
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print("computer plays", computer)

    if player == computer:
        print("its a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        elif computer == "scissors":
            print("computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("player wins!")
            player_wins += 1
    else:
        print("pls enter a valid move")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("ITS A TIE")
else:
    print("OH NO:( THE COMPUTER WON...")

    print(f"FINAL SCORES...player score:{player_wins} computer score:{computer_wins}")

