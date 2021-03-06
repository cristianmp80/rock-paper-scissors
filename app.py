from classes import Player
from utils import playerChoose, machineChoose, compareResults


print("""
**********************************
*   ROCK ** PAPER ** SCISSORS    *
**********************************  
""")
print("\n\nWelcome to the Rock-Paper-Scissors game!")
name = ""
while len(name) == 0:
    name = input("Please, give me your name: ")

player1 = Player(name)
machine = Player("")   

while True:
    resp = ""
    while resp != "y" and resp != "n":
        resp = input("Do you want to keep playing? (y/n) ")
        if resp != "y" and resp != "n":
            print("\nIncorrect answer...")
            continue
    if resp == "n":
        break
    elif resp == "y":
        player_choice = playerChoose(player1)
        machine_choice = machineChoose(machine)
        compareResults(player1, machine, player_choice, machine_choice)


print("\n\n******** FINAL SCORE ********")
print("Your score: {}".format(player1.getScore()))
print("Machine score: {}".format(machine.getScore()))
print("*****************************")
if player1.getScore() > machine.getScore():
    print("\n>>> YOU WIN, {}!!!".format(player1.name))
elif player1.getScore() < machine.getScore():
    print("\n>>> YOU LOSE, {} :(".format(player1.name))
else:
    print("\n>>> IT'S A DRAW")
c = input("\n\nPush ENTER key...")

    