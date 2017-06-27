from deck_of_cards import DeckOfCards
from players import Dealer
from players import Player
from players import HumanPlayer


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
            print 'Split-Matrix: ' + str(self.player.split_matrix) + '\n'
            self.deck_of_cards.restart_deck_of_cards()

        training_flag = False #I'm tired of training, I want to play seriously!!
        print 'END OF TRAINING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

        #On the while condition we could ask if the player wants to keep playing,
        #But here we prefer the automated player to play a fixed set of hands, let's say, 250
        real_hands_to_play = 250
        i = 0
        while (self.not_ended() and i < real_hands_to_play):

            i+=1
            print 'Real hand n' + str(i) + '\n'
            self.begin_hand(training_flag)
            self.deck_of_cards.restart_deck_of_cards()
            #print 'Q-Matrix: ' + str(self.player.fg_values_matrix) + '\n'
            print 'Split-Matrix: ' + str(self.player.split_matrix) + '\n'

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

        if (self.player.calculate_value() == 21):

            print 'BlackJack! You win'
            self.player.get_prize(3*self.current_player_bet)
            return 'win'

        elif (self.player.calculate_value() == self.dealer.calculate_value()):

            print "It's a tie! Your bet is refunded"
            self.player.get_prize(self.current_player_bet)
            return 'tie'

        else:

            split_flag = False
            if (self.player.has_two_equal_valued_cards()):

                if (self.player.wants_to_split(training_flag)):

                    split_flag = True
                    result = self.split_hand(training_flag) #Code the split hand
                    self.print_split_game_results(result)

                    self.player.restart_temp_state_action()
                    return result


            if not split_flag:

                dealer_original_value = self.dealer.calculate_value()

                self.player.make_move(dealer_original_value, training_flag)

                player_value = self.player.calculate_value()

                self.dealer.make_move(player_value)

                #print player_value
                #print self.dealer.calculate_value()
                result = ''
                result = self.print_hand_results(self.current_player_bet, player_value, result, training_flag)

                return result

    def print_hand_results(self, bet, player_value, result, training_flag):
        if player_value > 21:
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

    def print_split_game_results(self, result):
        if (result == 'win'):
            print '\n----Human Player WINS the Split Game (Two victories)'
            print '-------------------------------------------------'

        elif (result == 'tie'):
            print '\n----The Split Game is a TIE (One victory)'
            print '-------------------------------------------------'

        elif (result == 'lose'):
            print '\n----Dealer WINS the Split Game (Zero victories)'
            print '-------------------------------------------------'

    def split_hand(self, training_flag):
        #If the player chooses to split, then two 'sub-hands' are played
        #instead of one. Each hand with one of the cards, and each hand
        #with the same bet. Obviously, if the player chooses to split, he
        #must bet again the same quantity.
        points = 0
        print 'SPLIT!\n'
        print '----Split hand 1\n'
        result1 = self.begin_hand(training_flag)
        print '----Split hand 2\n'
        result2 = self.begin_hand(training_flag)

        if (result1 == 'win'): points +=1

        if (result2 == 'win'): points +=1

        if (training_flag): self.player.update_split_matrix(points)

        #This works like this: two wins on a split game are computed as ONE WIN.
        #One win in a split game is computed as a TIE
        #Zero wins in a split game are computed as a LOSE
        if (points == 2): return 'win'
        if (points == 1): return 'tie'
        if (points == 0): return 'lose'








