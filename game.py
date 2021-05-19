from human import Human
from computer import AI

class Game:

    def __init__(self):
        self.run_game()
        self.player_one = ''
        self.player_two = ''


    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!  Enter player 1')
        self.player_one = Human()

    def choose_player_two(self):
        self.player_two = input('Press 1 for single player or 2 for multiplayer!')
        if self.player_two == '1':
            self.player_two = AI()
        elif self.player_two == '2':
            print('Enter player 2')
            self.player_two = Human()

    def run_game(self):
        self.display_welcome()
        self.choose_player_two()
        self.round()

    def round(self):
        print('Let the game begin!')
        while len(self.player_one.score) < 2 and len(self.player_one.score) < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.keep_score()
            if len(self.player_one.score) == 2 or len(self.player_one.score) == 2:
                self.display_winner()

    def keep_score(self):
        if self.player_two.choose.def_gest[0] == self.player_one.choose.name or self.player_two.choose.def_gest[1] == self.player_one.choose.name:
            self.player_two.score.append('Win')
        elif self.player_one.choose.def_gest[0] == self.player_two.choose.name or self.player_one.choose.def_gest[1] == self.player_two.choose.name:
            self.player_one.score.append('Win')
        else:
            print('Round ended in a Draw!')

    def display_winner(self):
        pass