from unittest import TestCase


class TestHand(TestCase):

	#confirm an append Card() is now in self.cardsinhand array
	def test_add_card(self):
		testRank = ?
		testSuit = ?
		testCard = ?
		testHand = Hand()

		#should be a Card object
		expectedCard = testHand.cardsinhand[0]

		logic1 = expectedCard.suit == testSuit
		logic2 = testHand.cardsinhand[0].rank == testRank
		logic = logic1 and logic2
		print("run test case")
		self.fail()
