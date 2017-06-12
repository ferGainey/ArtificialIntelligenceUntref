import unittest
from main.card import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card_ace_spades = Card('Ace', 'Spades')
        self.card_jack_diamonds = Card('Jack', 'Diamonds')
        self.card_king_hearts = Card('King', 'Hearts')
        self.card_queen_clubs = Card('Queen', 'Clubs')
        self.card_9_clubs = Card('9', 'Clubs')

    def test_card_rank(self):
        self.assertEqual(self.card_ace_spades.rank, 'Ace')
        self.assertEqual(self.card_jack_diamonds.rank, 'Jack')
        self.assertEqual(self.card_king_hearts.rank, 'King')
        self.assertEqual(self.card_queen_clubs.rank, 'Queen')
        self.assertEqual(self.card_9_clubs.rank, '9')

    def test_card_suit(self):
        self.assertEqual(self.card_ace_spades.suit, 'Spades')
        self.assertEqual(self.card_jack_diamonds.suit, 'Diamonds')
        self.assertEqual(self.card_king_hearts.suit, 'Hearts')
        self.assertEqual(self.card_queen_clubs.suit, 'Clubs')
        self.assertEqual(self.card_9_clubs.suit, 'Clubs')


if __name__ == '__main__':
    unittest.main()