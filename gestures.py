from handgesture import Handgesture


class Gestures:

    def __init__(self):
        self.gestures = []
        self.add_to_list()

    def add_to_list(self):
        rock = Handgesture('rock', 'scissors', 'lizard')
        self.gestures.append(rock)
        paper = Handgesture('paper', 'rock', 'spock')
        self.gestures.append(paper)
        scissors = Handgesture('scissors', 'paper', 'lizard')
        self.gestures.append(scissors)
        lizard = Handgesture('lizard', 'paper', 'spock')
        self.gestures.append(lizard)
        spock = Handgesture('spock', 'rock', 'scissors')
        self.gestures.append(spock)
