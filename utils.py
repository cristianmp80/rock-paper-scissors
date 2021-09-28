import random

choices_dict = {"1": "Rock", "2": "Paper", "3": "Scissors"}

def playerChoose(player):
    choice = 0
    while choice not in list(choices_dict.keys()):
        print("\n\n*** Please, choose an option: ***")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Your choice: ")

    player.addChoice(choices_dict[choice])
    return choice


def machineChoose(machine):
    choice = random.choice(list(choices_dict.keys()))
    machine.addChoice(choices_dict[choice])
    return choice


def compareResults(player, machine, player_choice, machine_choice):
    print("******************")
    print("You chose: {}".format(choices_dict[player_choice]))
    print("Machine chose: {}".format(choices_dict[machine_choice]))
    if player_choice == machine_choice:
        print("DRAW")
    elif player_choice == "1" and machine_choice == "2":
        machine.win()
        print("MACHINE WINS")
    elif player_choice == "1" and machine_choice == "3":
        player.win()
        print("YOU WIN")
    elif player_choice == "2" and machine_choice == "1":
        player.win()
        print("YOU WIN")
    elif player_choice == "2" and machine_choice == "3":
        machine.win()
        print("MACHINE WINS")
    elif player_choice == "3" and machine_choice == "1":
        machine.win()
        print("MACHINE WINS")
    elif player_choice == "3" and machine_choice == "2":
        player.win()
        print("YOU WIN")
    print("*******************\n")
