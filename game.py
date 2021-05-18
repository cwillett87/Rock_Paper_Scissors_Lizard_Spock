from human import Human
from computer import AI

class Game:

    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or AI()

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')

    def choose_player_two(self):
        self.player_two = input('Press 1 for single player or 2 for multiplayer')
        if self.player_two == '1':
            self.player_two = AI()
        elif self.player_two == '2':
            self.player_two = Human()
#run game

#def round

#keep score

#determine winner