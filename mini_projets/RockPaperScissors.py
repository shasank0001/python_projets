import random

list=["rock","paper","scissor"]
comp_choise=random.choice(list)

while True:
    player_choise=input("enter your choise [rock,paper,scissors]: ")
    if player_choise in list:
        break

if comp_choise == player_choise:
    print("game is a tie ")
elif comp_choise=="rock" and player_choise == "paper":
    print("you won")
elif comp_choise == "paper" and player_choise == "scissor":
    print("you won")
elif comp_choise == "scissors" and player_choise == "rock":
    print("you won")
else:
    print("you lost")
