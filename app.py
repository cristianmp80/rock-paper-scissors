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
            print("\n\nIncorrect answer...")
            continue
    if resp == "n":
        break
    elif resp == "y":
        player_choice = playerChoose(player1)
        machine_choice = machineChoose(machine)
        compareResults(player1, machine, player_choice, machine_choice)


print("******** FINAL SCORE ********")
print("Your score: {}".format(player1.getScore()))
print("Machine score: {}".format(machine.getScore()))
if player1.getScore() > machine.getScore():
    print("\nYOU WIN, {}!!!".format(player1.name))
elif player1.getScore() < machine.getScore():
    print("\nYOU LOSE, {} :(".format(player1.name))
else:
    print("\nIT'S A DRAW")
c = input("Push any key...")

    