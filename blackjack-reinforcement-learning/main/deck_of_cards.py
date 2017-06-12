from random import shuffle
from card import Card


class DeckOfCards:

    all_cards = []
    #available_cards = None

    def __init__(self):
        self.restart_deck_of_cards()

    def give_a_card(self):
        selected_card = self.all_cards.pop()
        return selected_card

    #put the cards in random positions
    def shuffle_cards(self):
        shuffle(self.all_cards)

    #all the cards get available again
    def restart_deck_of_cards(self):
        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        for x in range(0, 4):
            for y in range(2, 11):
                card_rank = str(y)
                card_suit = suits[x]
                new_card = Card(card_rank, card_suit)
                self.all_cards.append(new_card)
            for z in range(11, 14):
                if z == 11:
                    card_rank = 'Jack'
                    card_suit = suits[x]
                    new_card = Card(card_rank, card_suit)
                    self.all_cards.append(new_card)
                if z == 12:
                    card_rank = 'Queen'
                    card_suit = suits[x]
                    new_card = Card(card_rank, card_suit)
                    self.all_cards.append(new_card)
                if z == 13:
                    card_rank = 'King'
                    card_suit = suits[x]
                    new_card = Card(card_rank, card_suit)
                    self.all_cards.append(new_card)
            #the Aces creation
            card_rank = 'Ace'
            card_suit = suits[x]
            new_card = Card(card_rank, card_suit)
            self.all_cards.append(new_card)

        self.shuffle_cards()







    """
        #ACES
        ace_spades = Card('Ace', 'Spades')
        self.all_cards.append(ace_spades)
        ace_diamonds = Card('Ace', 'Diamonds')
        self.all_cards.append(ace_diamonds)
        ace_hearts = Card('Ace', 'Hearts')
        self.all_cards.append(ace_hearts)
        ace_clubs = Card('Ace', 'Clubs')
        self.all_cards.append(ace_clubs)

        #2
        two_spades = Card('2', 'Spades')
        self.all_cards.append(two_spades)
        two_diamonds = Card('2', 'Diamonds')
        self.all_cards.append(two_diamonds)
        two_hearts = Card('2', 'Hearts')
        self.all_cards.append(two_hearts)
        two_clubs = Card('2', 'Clubs')
        self.all_cards.append(two_clubs)

        #3
        three_spades = Card('3', 'Spades')
        self.all_cards.append(three_spades)
        three_diamonds = Card('3', 'Diamonds')
        self.all_cards.append(three_diamonds)
        three_hearts = Card('3', 'Hearts')
        self.all_cards.append(three_hearts)
        three_clubs = Card('3', 'Clubs')
        self.all_cards.append(three_clubs)

        #4
        four_spades = Card('4', 'Spades')
        self.all_cards.append(four_spades)
        four_diamonds = Card('4', 'Diamonds')
        self.all_cards.append(four_diamonds)
        four_hearts = Card('4', 'Hearts')
        self.all_cards.append(four_hearts)
        four_clubs = Card('4', 'Clubs')
        self.all_cards.append(four_clubs)

        #5
        five_spades = Card('5', 'Spades')
        self.all_cards.append(five_spades)
        five_diamonds = Card('5', 'Diamonds')
        self.all_cards.append(five_diamonds)
        five_hearts = Card('5', 'Hearts')
        self.all_cards.append(five_hearts)
        five_clubs = Card('5', 'Clubs')
        self.all_cards.append(five_clubs)

        #6
        xxx_spades = Card('Ace', 'Spades')
        self.all_cards.append(xxx_spades)
        xxx_diamonds = Card('Ace', 'Diamonds')
        self.all_cards.append(xxx_diamonds)
        xxx_hearts = Card('Ace', 'Hearts')
        self.all_cards.append(xxx_hearts)
        xxx_clubs = Card('Ace', 'Clubs')
        self.all_cards.append(xxx_clubs)
        """
