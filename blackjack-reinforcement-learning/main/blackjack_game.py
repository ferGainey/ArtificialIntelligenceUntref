from deck_of_cards import DeckOfCards
from players import Dealer
from players import Player
from players import HumanPlayer
import copy


class BlackjackGame:

    deck_of_cards = None
    dealer = None
    player = None
    active = None #This indicates if the game is active or not
    current_player_bet = None


    def __init__(self):
        self.deck_of_cards = DeckOfCards()
        self.dealer = Dealer(self)
        self.player = HumanPlayer(self, 10000) #The human player starts with 10000 coins
        self.start_game()

    def start_game(self):

        self.active = True  # As the game begins, we set this flag the True value
        training_flag = True #It's time to train!
        training_repetitions = 2000 #this number can be changed
        for x in range(0, training_repetitions):
            print 'Training hand #' + str(x) + '\n'
            self.begin_hand(training_flag)
            #print 'Q-Matrix: ' + str(self.player.fg_values_matrix) + '\n'
            #print 'Split-Matrix: ' + str(self.player.split_matrix) + '\n'
            self.deck_of_cards.restart_deck_of_cards()

        training_flag = False #I'm tired of training, I want to play seriously!!
        print 'END OF TRAINING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        self.player.print_victories()
        self.dealer.print_victories()
        #On the while condition we could ask if the player wants to keep playing,
        #But here we prefer the automated player to play a fixed set of hands, let's say, 250
        real_hands_to_play = 250
        i = 0
        while (self.not_ended() and i < real_hands_to_play):

            i+=1
            print '--------------------------------------------------'
            print '\n\nReal hand #' + str(i) + '\n'
            self.begin_hand(training_flag)
            self.deck_of_cards.restart_deck_of_cards()
            print 'Q-Matrix: ' + str(self.player.fg_values_matrix) + '\n'
            #print 'Split-Matrix: ' + str(self.player.split_matrix) + '\n'

        self.player.print_victories()
        self.dealer.print_victories()


    def not_ended(self):
        return self.active

    def clean_hands(self):
        self.player.clean_hand()
        self.dealer.clean_hand()

    def get_deck(self):
        return self.deck_of_cards

    def begin_hand(self, training_flag):
        self.current_player_bet = self.player.bet()

        self.clean_hands() #Makes sure both the dealer and the player have empty hands

        print '\n \n NEW ROUND:'

        print '\n Dealer Hand:'
        self.dealer.get_card(self.deck_of_cards.give_a_card())
        self.dealer.print_hand()

        print '\n Human Hand:'
        self.player.get_card(self.deck_of_cards.give_a_card())
        self.player.get_card(self.deck_of_cards.give_a_card())
        self.player.print_hand()

        #if (self.player.calculate_value() == 21):


        if (self.player.calculate_value() == self.dealer.calculate_value()):

            print "It's a tie! Your bet is refunded"
            self.player.get_prize(self.current_player_bet)
            return 'tie'

        else:

            dealer_original_value = self.dealer.calculate_value()

            move = self.player.make_move(dealer_original_value, training_flag)

            if (move == 'split'):

                self.split_hand(training_flag)

            else:

                player_value = self.player.calculate_value()

                self.dealer.make_move(player_value)

                #print player_value
                #print self.dealer.calculate_value()
                result = ''
                result = self.compute_and_print_hand_results(self.current_player_bet, player_value, result, training_flag)

                return result

    #This should be refactored
    def compute_and_print_hand_results(self, bet, player_value, result, training_flag):
        if player_value == 21:
            print 'BlackJack! You win'
            print '-------------------------------------------------'
            self.player.get_prize(2 * self.current_player_bet)
            if training_flag and (len(self.player.temp_state_action) > 0):
                self.player.update_fg_values('win')
            elif not training_flag:
                self.player.compute_victory()
            result = 'win'
        elif player_value > 21:
            print ' \nThe Dealer WINS! (Human got over 21)'
            print '-------------------------------------------------'
            if training_flag:
                self.player.update_fg_values('lose')
            else:
                self.dealer.compute_victory()
            result = 'lose'
            self.player.restart_temp_state_action()
        elif self.dealer.calculate_value() > 21:
            print '\nHuman Player WINS! (Dealer got over 21)'
            print '-------------------------------------------------'
            self.player.get_prize(2 * bet)
            if training_flag:
                self.player.update_fg_values('win')
            else:
                self.player.compute_victory()
            result = 'win'
            self.player.restart_temp_state_action()
        elif (21 - player_value) < (21 - self.dealer.calculate_value()):
            print "\nHuman Player WINS! (Has a better score)"
            print '-------------------------------------------------'
            self.player.get_prize(2 * bet)
            if training_flag:
                self.player.update_fg_values('win')
            else:
                self.player.compute_victory()
            result = 'win'
            self.player.restart_temp_state_action()
        elif (21 - player_value) > (21 - self.dealer.calculate_value()):
            print "\nThe Dealer WINS! (Has a better score)"
            print '-------------------------------------------------'
            if training_flag:
                self.player.update_fg_values('lose')
            else:
                self.dealer.compute_victory()
            result = 'lose'
            self.player.restart_temp_state_action()
        return result

    def split_hand(self, training_flag):
        #If the player chooses to split, then two 'sub-hands' are played
        #instead of one. Each hand with one of the cards, and each hand
        #with the same bet. Obviously, if the player chooses to split, he
        #must bet again the same quantity.
        player_hand_a = self.player.hand
        dealer_hand_a = self.dealer.hand
        player_hand_b = copy.deepcopy(self.player.hand)
        dealer_hand_b = copy.deepcopy(self.dealer.hand)
        print 'SPLIT!\n'
        print '----Split hand 1\n'
        self.begin_one_split_hand(training_flag, player_hand_a, dealer_hand_a)
        aux_temp_state_action_a = copy.deepcopy(self.player.temp_state_action)
        print '----Split hand 2\n'
        self.player.temp_state_action.append(((player_hand_b.calculate_status(),dealer_hand_b.calculate_value()), 'split'))
        self.begin_one_split_hand(training_flag, player_hand_b, dealer_hand_b)
        self.dealer.make_move(0) #0 because it play with 2 hands at the same time
        player_value = self.player.calculate_value()
        result = ''
        #hand b
        result = self.compute_and_print_hand_results(self.current_player_bet, player_value, result, training_flag)
        #hand a
        self.player.temp_state_action = aux_temp_state_action_a
        result = self.compute_and_print_hand_results(self.current_player_bet, player_value, result, training_flag)
        return result




    def begin_one_split_hand(self, training_flag, player_hand, dealer_hand):
        dealer_original_value = dealer_hand.calculate_value()
        self.player.hand = player_hand
        self.player.make_move(dealer_original_value, training_flag)









