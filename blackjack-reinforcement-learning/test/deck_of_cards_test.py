import unittest
from main.deck_of_cards import DeckOfCards


class TestDeckOfCards(unittest.TestCase):

    def setUp(self):
        self.deck_of_cards = DeckOfCards()

    def test_get_a_card(self):
        card_1 = self.deck_of_cards.give_a_card()
        card_2 = self.deck_of_cards.give_a_card()
        """
        print 'CARTA 1'
        print card_1.rank
        print card_1.suit
        print card_1.value
        print 'CARTA 2'
        print card_2.rank
        print card_2.suit
        print card_2.value
        """
        self.assertNotEqual(card_1, card_2)


if __name__ == '__main__':
    unittest.main()