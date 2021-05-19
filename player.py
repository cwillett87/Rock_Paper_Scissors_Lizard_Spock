from gestures import Gestures


class Player:

    def __init__(self):
        self.name = ''
        self.gestures = Gestures()
        self.score = []
        self.choose = []

    def set_name(self):
        self.name = input('Enter player name:')

    def choose_gesture(self):
        print(f'Gestures to choose from: {self.gestures.gestures[0].name}, '
              f'{self.gestures.gestures[1].name}, {self.gestures.gestures[2].name}, '
              f'{self.gestures.gestures[3].name}, {self.gestures.gestures[4].name}')
        print(' ')
        choice = input(f'{self.name} Please choose a gesture:')
        case = choice.casefold()
        print(' ')
        if case == self.gestures.gestures[0].name:
            self.choose = self.gestures.gestures[0]
        elif case == self.gestures.gestures[1].name:
            self.choose = self.gestures.gestures[1]
        elif case == self.gestures.gestures[2].name:
            self.choose = self.gestures.gestures[2]
        elif case == self.gestures.gestures[3].name:
            self.choose = self.gestures.gestures[3]
        elif case == self.gestures.gestures[4].name:
            self.choose = self.gestures.gestures[4]
        else:
            print('Invalid Input!')
            self.choose_gesture()
