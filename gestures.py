from handgesture import Handgesture

class Gestures:

    def __init__(self):
        self.gestures = []
        self.add_to_list()

    def add_to_list(self):
        Rock = Handgesture('Rock', 'Scissors', 'Lizard')
        self.gestures.append(Rock)
        Paper = Handgesture('Paper', 'Rock', 'Spock')
        self.gestures.append(Paper)
        Scissors = Handgesture('Scissors' , 'Paper', 'Lizard')
        self.gestures.append(Scissors)
        Lizard = Handgesture('Lizard', 'Paper', 'Spock')
        self.gestures.append(Lizard)
        Spock = Handgesture('Spock', 'Rock', 'Scissors')
        self.gestures.append(Spock)