from deck_of_cards import DeckOfCards
from players import Dealer
from players import Player
from players import HumanPlayer


class BlackjackGame:

    deck_of_cards = None
    dealer = None
    player = None
    active = None #This indicates if the game is active or not

    def __init__(self):
        self.deck_of_cards = DeckOfCards()
        self.dealer = Dealer(self)
        self.player = HumanPlayer(self, 10) #The human player starts with 10 coins
        self.start_game()

    def start_game(self):

        self.active = True  # As the game begins, we set this flag the True value
        training_flag = True #It's time to train!
        #TRAIN 9999 times!! It
        training_repetitions = 9999 #this number can be changed
        for x in range(0,training_repetitions):
            self.begin_hand(training_flag)
            self.player.ask_if_continues()  # The player if asked if he wants to keep playing
            self.deck_of_cards.restart_deck_of_cards()

        training_flag = False #I'm tired of training, I wan to play seriously!!
        print 'END OF TRAINING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        print self.player.fg_values_matrix
        while (self.not_ended() and self.player.ask_if_continues()):

            self.begin_hand(training_flag)
            #No hace nada aca! #self.player.ask_if_continues() #The player if asked if he wants to keep playing
            self.deck_of_cards.restart_deck_of_cards()
        #print self.player.fg_values_matrix


    def not_ended(self):
        return self.active

    def clean_hands(self):
        self.player.clean_hand()
        self.dealer.clean_hand()

    def get_deck(self):
        return self.deck_of_cards

    def begin_hand(self, training_flag):
        bet = self.player.bet()

        self.clean_hands() #Makes sure both the dealer and the player have empty hands

        print '\n \n NEW ROUND:'

        self.dealer.get_card(self.deck_of_cards.give_a_card())
        print '\n Dealer Hand:'
        print str(self.dealer.hand[0].rank) + ' of ' + str(self.dealer.hand[0].suit)
        self.player.get_card(self.deck_of_cards.give_a_card())
        self.player.get_card(self.deck_of_cards.give_a_card())
        print '\n Human Hand:'
        print str(self.player.hand[0].rank) + ' of ' + str(self.player.hand[0].suit)
        print str(self.player.hand[1].rank) + ' of ' + str(self.player.hand[1].suit)

        if (self.player.calculate_value() == 21):

            print 'BlackJack! You win'
            self.player.get_prize(bet + 1.5*bet)

        else:

            if (self.player.has_two_equal_valued_cards):

                if (self.player.wants_to_split()):

                    self.split_hand() #Code the spit hand

            dealer_original_value = self.dealer.calculate_value()

            self.player.make_move(dealer_original_value, training_flag)

            player_value = self.player.calculate_value()

            print '\n Dealer Cards: '
            self.dealer.make_move(player_value)

            #print player_value
            #print self.dealer.calculate_value()
            if player_value > 21:
                print ' \nThe Dealer WIN (Human Has more than 21)'
                print '-------------------------------------------------'
                if training_flag: self.player.update_fg_values('lose')
            elif self.dealer.calculate_value() > 21:
                print '\nHuman Player WIN. (Dealer has more than 21)'
                print '-------------------------------------------------'
                if training_flag: self.player.update_fg_values('win')
            elif (21 - player_value) < (21 - self.dealer.calculate_value()):
                print "\nHuman Player WIN. (Have better hand)"
                print '-------------------------------------------------'
                if training_flag: self.player.update_fg_values('win')
            elif (21 - player_value) > (21 - self.dealer.calculate_value()):
                print "\nThe Dealer WIN. (Have better hand)"
                print '-------------------------------------------------'
                if training_flag: self.player.update_fg_values('lose')
            self.player.restart_temp_state_action()

            #TODO: If both have the same hand value, the bid is returned.



    def split_hand(self):
        #TODO: Implement
        #If the player chooses to split, then two 'sub-hands' are played
        #instead of one. Each hand with one of the cards, and each hand
        #with the same bet. Obviously, if the player chooses to split, he
        #must bet again the same quantity.
        pass








