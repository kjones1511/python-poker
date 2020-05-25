from unittest import TestCase
from Objects import *


class TestHand(TestCase):

	#confirm an append Card is now in self.cardsinhand array
	def test_add_card(self):
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
