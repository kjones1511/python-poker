class Cat:
    def init(self, name, gender):
        self.name = name
        self.gender = gender #note, isn't binary

    def runs(self):
        print( self.name + " runs")

class Card:
    # we expect suit and rank to both be string inputs
    # value will be a 2 element array containing the card's rank and suit
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = [rank, suit]

    # we expect display to print the rank and suit of the defined card object
    def display(self):
        print(self.rank + " of " + self.suit)

class Hand:
    #intialize function we expect the class Hand to inherit a Player name in the form of a string "player" and initialize an empty array called cardsinhand
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
    def __init__(self, deckCount = None, file = None ):
        self.deckarray = []
        if file == None:
            cardCount = deckCount * 52
            suits = ["heart", "club", "diamond", "spades"]
            ranks = ["2", "3"......."Jack", "Queen", "King", "Ace"]
            for n in cardCount:
                print("card")
        else:
            Deck.initialize(file)


    #todo: doesn't work, return to build later. referenced in Deck.__init__
    def initialize(self):
        def file_read(fname):
            with open(fname) as f:
                # Content_list is the list that contains the read lines.
                for line in f:
                    self.deckarray.append(line)

        file_read("pokerdeck.txt")


