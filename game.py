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
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        if self.player_one.choose == self.player_two.choose.gestures.gestures.def_gest[0] or
            self.player_two.choose.gestures.gestures.def_gest[1]:


#keep score

#determine winner