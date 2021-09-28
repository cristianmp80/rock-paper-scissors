class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.choices = []
    def win(self):
        self.wins += 1
    def getScore(self):
        return self.wins
    def addChoice(self, choice):
        self.choices.append(choice)
    
