from unittest import TestCase
from Objects import *


class test_deck(TestCase):
	#confirm an append Card is now in self.cardsinhand array
	#currently doesn't test initialize by file
	def test___init__(self):
		testRank = "queen"
		testSuit = "clubs"
		testCard = Card(testSuit,testRank)
		testHand = Hand("Jake")

		testHand.add_card(testCard)

		#should return only card in Hand array
		expectedCard = testHand.cardsinhand[0]

		#confirm the suit and rank are expected and exist
		self.assertEqual(expectedCard.suit, testSuit, "fails if built card has incorrect suit")
		self.assertEqual(expectedCard.rank, testRank, "fails if built card has incorrect rank")

	#confirms a new card is returned and deck size has decreaed
	def test_popCard(self):
		deckCount = 2
		deck = Deck(deckCount)
		card = deck.popCard()
		self.assertEqual( len(deck.deckarray) , deckCount*52 - 1, "fails if deck size has not decreased by 1" )
		self.assertIsNotNone( card , "fails if a new card has not been built" )


	#confirms deck has been shuffled by ensuring <45 cards are in the same spot after shuffling
	def test_shuffle(self):
		deckCount = 1
		tDeck = Deck(deckCount)
		tDeckNonShuffle = Deck(deckCount)
		tDeck.shuffle()
		error = 0
		#goes through every card in deck and counts error if same card is in the same place
		for i in range(52):
			logicTest = tDeck.deckarray[i].value == tDeckNonShuffle.deckarray[i].value and tDeck.deckarray[i].rank == tDeckNonShuffle.deckarray[i].rank
			if logicTest:
				error += 1
		self.assertTrue(error < 45, "More than 45 cards are the same, deck probably didn't shuffle")