print("rock....")
print("paper....")
print("scissors...")

player1 = input("player1, make your move: ")
print("NO CHEATING!\n\n" * 20)
player2 = input("player2, make your move: ")

if player1 == player2:
    print("its a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins!")
    elif player2 == "scissors":
        print("player2 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins!")
    elif player2 == "paper":
        print("player1 wins!")
else:
    print("something went wrong")


# OR
p1 = input("player 1:rock, paper,scissors")
p2 = input("player 2:rock, paper,scissors")

if p1 == p2:
    print("draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")

import random

int1 = random.randint(0, 9)
print(int1)


import random

beg = 10
end = 100

for i in range(6):
    random_int = random.randint(beg, end)
    print(random_int)
    #print(random.randint(beg, end))

#OR
for i in range(6):
    print(random.randint(beg, end))
