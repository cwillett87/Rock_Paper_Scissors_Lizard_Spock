from player import Player

class Human(Player):

    def __init__(self):
        super().__init__()
        self.name = ''
        self.score = []
        self.choose = ''
        self.set_name()


    def set_name(self):
        self.name = input('name:')

    def choose_gesture(self):
        print(self.gestures.gestures[0].name)
        print(self.gestures.gestures[1].name)
        print(self.gestures.gestures[2].name)
        print(self.gestures.gestures[3].name)
        print(self.gestures.gestures[4].name)
        choice = input(f'{self.name} Please choose a gesture:')
        if choice == self.gestures.gestures[0].name:
            self.choose = self.gestures.gestures[0].name
        elif choice == self.gestures.gestures[1].name:
            self.choose = self.gestures.gestures[1].name
        elif choice == self.gestures.gestures[2].name:
            self.choose = self.gestures.gestures[2].name
        elif choice == self.gestures.gestures[3].name:
            self.choose = self.gestures.gestures[3].name
        elif choice == self.gestures.gestures[4].name:
            self.choose = self.gestures.gestures[4].name