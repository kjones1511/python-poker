class Cat:
    def init(self, name, gender):
        self.name = name
        self.gender = gender #note, isn't binary

    def runs(self):
        print( self.name + " runs")

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = [rank, suit]

    def display(self):
        print(self.rank + " of " + self.suit)

class Hand:
    def __init__(self, player):
       self.cardsinhand = []
       self.player = player

    def add_card(self, card):
        self.cardsinhand.append(card)

    def show_hand(self):
        print(self.cardsinhand)

    #returns boolean true/false if pair exists in hand
    def isPair(self):
        return True

class Deck:
    def __int__(self):
        self.deckarray = []

    def initialize(self):

        def file_read(fname):

            with open(fname) as f:
                # Content_list is the list that contains the read lines.
                for line in f:
                    self.deckarray.append(line)

        file_read("pokerdeck.txt")


