from gestures import Gestures

class Player:

    def __init__(self):
        self.name = ''
        self.gestures = Gestures()
        self.score = []
        self.choose = ''

    def set_name(self):
        self.name = input('Enter player name:')

    def choose_gesture(self):
        print(self.gestures)
        self.choose = input('choose a gesture:')