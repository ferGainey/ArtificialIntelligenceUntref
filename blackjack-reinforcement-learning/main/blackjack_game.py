from deck_of_cards import DeckOfCards
from players import Dealer
from players import Player


class BlackjackGame:

    deck_of_cards = None
    dealer = None
    player = None
    active = None #This indicates if the game is active or not

    def __init__(self):
        self.deck_of_cards = DeckOfCards()
        self.dealer = Dealer(self)
        self.player = Player(self, 10) #The human player starts with 10 coins
        self.start_game()

    def start_game(self):

        self.active = True  # As the game begins, we set this flag the True value
        while (self.not_ended()):

            self.begin_hand()
            self.player.ask_if_continues() #The player if asked if he wants to keep playing


    def not_ended(self):
        return self.active

    def clean_hands(self):
        self.player.clean_hand()
        self.dealer.clean_hand()

    def get_deck(self):
        return self.deck_of_cards

    def begin_hand(self):
        bet = self.player.bet()

        self.clean_hands() #Makes sure both the dealer and the player have empty hands

        self.dealer.get_card(self.deck_of_cards.give_a_card())
        self.player.get_card(self.deck_of_cards.give_a_card())
        self.player.get_card(self.deck_of_cards.give_a_card())

        if (self.player.calculate_value() == 21):

            print 'BlackJack! You win'
            self.player.get_prize(bet + 1.5*bet)

        else:

            if (self.player.has_two_equal_valued_cards):

                if (self.player.wants_to_split()):

                    self.split_hand() #Code the spit hand

            dealer_original_value = self.dealer.calculate_value()

            self.player.make_move(dealer_original_value)

            player_value = self.player.calculate_value()

            self.dealer.make_move(player_value)

            #TODO: Calculate results. If player's hand value is higher
            #TODO: than dealer's hand value, then the player wins.
            #TODO: If both have the same hand value, the bid is returned.
            #TODO: If anyone's hand value is over 21, he loses



    def split_hand(self):
        #TODO: Implement
        #If the player chooses to split, then two 'sub-hands' are played
        #instead of one. Each hand with one of the cards, and each hand
        #with the same bet. Obviously, if the player chooses to split, he
        #must bet again the same quantity.
        pass








