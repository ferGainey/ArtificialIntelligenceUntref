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
