from player import Player
import random


class AI(Player):

    def __init__(self):
        super().__init__()
        self.set_name()

    def set_name(self):
        self.name = input('Enter player name:')

    def choose_gesture(self):
        choice = random.choice(self.gestures.gestures)
        if choice == self.gestures.gestures[0]:
            self.choose = self.gestures.gestures[0]
            print(f'{self.name} chose {self.gestures.gestures[0].name}')
        elif choice == self.gestures.gestures[1]:
            self.choose = self.gestures.gestures[1]
            print(f'{self.name} chose {self.gestures.gestures[1].name}')
        elif choice == self.gestures.gestures[2]:
            self.choose = self.gestures.gestures[2]
            print(f'{self.name} chose {self.gestures.gestures[2].name}')
        elif choice == self.gestures.gestures[3]:
            self.choose = self.gestures.gestures[3]
            print(f'{self.name} chose {self.gestures.gestures[3].name}')
        elif choice == self.gestures.gestures[4]:
            self.choose = self.gestures.gestures[4]
            print(f'{self.name} chose {self.gestures.gestures[4].name}')

