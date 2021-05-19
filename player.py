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
        print(self.gestures.gestures[0].name)
        print(self.gestures.gestures[1].name)
        print(self.gestures.gestures[2].name)
        print(self.gestures.gestures[3].name)
        print(self.gestures.gestures[4].name)
        choice = input(f'{self.name} Please choose a gesture:')
        if choice == self.gestures.gestures[0].name:
            self.choose = self.gestures.gestures[0]
        elif choice == self.gestures.gestures[1].name:
            self.choose = self.gestures.gestures[1]
        elif choice == self.gestures.gestures[2].name:
            self.choose = self.gestures.gestures[2]
        elif choice == self.gestures.gestures[3].name:
            self.choose = self.gestures.gestures[3]
        elif choice == self.gestures.gestures[4].name:
            self.choose = self.gestures.gestures[4]
