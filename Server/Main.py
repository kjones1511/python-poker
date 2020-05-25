import random
from Objects import *

def main():

    #task1: build a Card
    #task2: print card value
    #task3: print values interpreting face cards

#populates and displays first card
    card1 = Card("Spades", "Ace")
    card1.display()
#populates and displays second card
    card2 = Card("Hearts", "Ace")
    card2.display()
#populates and displays hand empty
    hand1 = Hand("Jake")
    hand1.show_hand()
#populates and displays hand after adding first card
    hand1.add_card(card1.value)
    hand1.show_hand()
#populates and displays hand after adding first card
    hand1.add_card(card2.value)
    hand1.show_hand()

    deck1 = Deck()
    deck1.initialize()




main()