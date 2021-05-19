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
        print(' ')

    def choose_player_two(self):
        self.player_two = input('Press 1 for single player or 2 for multiplayer!')
        print(' ')
        if self.player_two == '1':
            self.player_two = AI()
            print(' ')
        elif self.player_two == '2':
            print('Enter player 2')
            self.player_two = Human()
            print(' ')
        else:
            print('Enter a 1 or 2')
            self.choose_player_two()

    def run_game(self):
        self.display_welcome()
        self.choose_player_two()
        self.round()

    def round(self):
        print('Let the game begin!')
        print(' ')
        while len(self.player_one.score) < 2 and len(self.player_one.score) < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.keep_score()
            if len(self.player_one.score) == 2 or len(self.player_two.score) == 2:
                self.display_winner()
                break

    def keep_score(self):
        if self.player_two.choose.def_gest[0] == self.player_one.choose.name or self.player_two.choose.def_gest[1] == self.player_one.choose.name:
            self.player_two.score.append('Win')
            print(' ')
            print(f'{self.player_two.name} Won this round!')
            print(' ')
        elif self.player_one.choose.def_gest[0] == self.player_two.choose.name or self.player_one.choose.def_gest[1] == self.player_two.choose.name:
            self.player_one.score.append('Win')
            print(' ')
            print(f'{self.player_one.name} Won this round!')
            print(' ')
        else:
            print(' ')
            print('Round ended in a Draw!')
            print(' ')

    def display_winner(self):
        if len(self.player_one.score) == 2:
            print(f'{self.player_one.name} Wins the game!')
            print(' ')
            self.replay()
        elif len(self.player_two.score) == 2:
            print(f'{self.player_two.name} Wins the game!')
            print(' ')
            self.replay()

    def replay(self):
        replay = input(f'{self.player_one.name} Would you like to play again?')
        if replay == 'yes':
            self.run_game()
        elif replay == 'no':
            print(' ')
            print(f'Thanks for playing {self.player_one.name}, see you later!')
        else:
            self.replay()
