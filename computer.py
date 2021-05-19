from player import Player
import random

class AI(Player):

    def __init__(self):
        super().__init__()
        self.name = ''
        #self.gestures = Gestures()
        self.score = []
        self.choose = []

    def set_name(self):
        self.name = input('Enter player name:')

    def choose_gesture(self):
        print(self.gestures)
        #self.choose = #choose randomly