import random

MY_CHOICE = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self, name, human):
        self.choices = []
        self.name = name
        self.human = human

    def __str__(self):
        return self.name

    def choice(self):
        if self.human:
            choice = input("rock, paper, or scissors?")
            self.choices.append(choice)

    def random_choice(self):
        if not self.human:
            random_choice = random.choice(MY_CHOICE)
            self.choices.append(random_choice)


class Game:
    def __init__(self):
        self.player = Player("Laura", True)
        self.computer = Player("Computer", False)


new_game = Game()
print(new_game.__dict__)
new_game.player.choice()
print(new_game.player.choices)
new_game.computer.random_choice()
print(new_game.computer.choices)
