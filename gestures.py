from handgesture import Handgesture


class Gestures:

    def __init__(self):
        self.gestures = []
        self.add_to_list()

    def add_to_list(self):
        rock = Handgesture('Rock', 'Scissors', 'Lizard')
        self.gestures.append(rock)
        paper = Handgesture('Paper', 'Rock', 'Spock')
        self.gestures.append(paper)
        scissors = Handgesture('Scissors', 'Paper', 'Lizard')
        self.gestures.append(scissors)
        lizard = Handgesture('Lizard', 'Paper', 'Spock')
        self.gestures.append(lizard)
        spock = Handgesture('Spock', 'Rock', 'Scissors')
        self.gestures.append(spock)
