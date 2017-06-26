from random import randint

from hand import Hand


class Player:

    game = None
    hand = None
    victories = 0

    def get_card(self, card):
        if (self.hand.have_an_ace() and card.rank == 'Ace'):
            card.set_value(1)
        self.hand.add_card(card)


    def clean_hand(self):
        self.hand.clean()

    def calculate_value(self):
        return self.hand.calculate_value()

    def calculate_hardness(self):
        return self.hand.get_hardness()

    def calculate_status(self):
        return self.hand.calculate_status()

    def compute_victory(self):
        self.victories += 1


class HumanPlayer(Player):

    coins = 0
    actions = []
    states = []
    fg_values_matrix = {}
    split_matrix = {}
    temp_state_action = []

    def __init__(self, game, coins):
        self.game = game
        self.hand = Hand()
        self.coins = coins
        #the actions are continue or stand. Split and bet more coins will be developed later
        self.actions = ['continue', 'stand', 'double bet']
        """
        The human player can take decisions only between 2 and 20. The '2' case is the lowest initial hand that the human
        can receive (two Aces). And the '20' case is the highest value that human can obtain without winning or loosing
        that round.
        """
        for i in range(2,21):
            #The lowest value card that the dealer can receive is 1 (an Ace) and the highest is 11 (Soft Ace)
            #In this initial implementation the Ace will have one unique value: 1. Later it can be 1 or 11. (in progress)
            for j in range(1,12):
                player_status = str(i) + 's'
                self.states.append((player_status,j))
                player_status = str(i) + 'h'
                self.states.append((player_status,j))

        #Initialize fg_values_matrix with 0.0 probability each one. I use a dictionary to do this.
        # The key is: (the state,action). And the value will be the fg_value
        for x in range(0, len(self.states)):
            for y in range(0, len(self.actions)):
                current_state = self.states[x]
                current_action = self.actions[y]
                self.fg_values_matrix[current_state, current_action] = 0.0

        #Initialize the Ace possible values. It can be 1 or 11
        #The initial value is 0.5 for both Ace possibility
        self.split_matrix['yes'] = 0.5
        self.split_matrix['no'] = 0.5



    def bet(self):
        #This must get the player's bet from the command line
        #Returns the bet
        self.coins -= 1
        return 1 #The automated player only bets 1 coin

    def double_bet(self):
        self.game.current_player_bet *= 2

    def get_prize(self, prize):
        #This gives the player the prize if won a hand
        self.coins += prize

    def print_victories(self):
        print 'Player won ' + str(self.victories) + ' times'

    def has_two_equal_valued_cards(self):
        return self.hand.has_two_equal_valued_cards()

    def wants_to_split(self, training_flag):
        #Returns true if the player chooses to split
        #Returns false if the player chooses to keep playing without splitting
        if (training_flag):

            number = randint(0,9)
            if (number > 5): return True
            else: return False

        else:

            if self.split_matrix['yes'] >= self.split_matrix['no']: return True
            else: return False

    def have_an_ace(self):
        return self.hand.have_an_ace()

    def have_more_than_1_ace(self):
        return self.hand.have_more_than_1_ace()


    #Fix
    def stand(self, dealer_original_value, training_flag):

        if training_flag:

            random_number = randint(0, 9)
            #double bet
            if random_number < 1:
                if (self.calculate_value() <= 20):
                    self.temp_state_action.append(((self.hand.calculate_status(), dealer_original_value),'double bet'))
                    self.double_bet()
                    print 'Action: Asks for a card'
                    new_card = self.game.get_deck().give_a_card()
                    self.get_card(new_card)
                    print str(new_card.rank) + ' of ' + str(new_card.suit)
                    if (self.calculate_value() <= 20):
                        self.temp_state_action.append(((self.hand.calculate_status(), dealer_original_value), 'stand'))
                return True
            #continue
            elif 2 <= random_number < 5:
                if (self.calculate_value() <= 20):
                    self.temp_state_action.append(((self.hand.calculate_status(), dealer_original_value),'continue'))
                return False
            #stand
            else:
                if self.calculate_value() <= 20:
                    self.temp_state_action.append(((self.hand.calculate_status(), dealer_original_value), 'stand'))
                print 'Action: Stand'
                return True
        #when it is not training
        elif self.calculate_value() <= 20:

            # compare the values, if stand_value is higher than continue_value, the next action will be stand
            stand_value = self.fg_values_matrix[(self.calculate_value(), dealer_original_value), 'stand']
            continue_value = self.fg_values_matrix[(self.calculate_value(), dealer_original_value), 'continue']
            double_bet_value = self.fg_values_matrix[(self.calculate_value(), dealer_original_value), 'double bet']
            if stand_value > continue_value:
                return True
            else:
                return False
        return True
        #Returns true if the player chooses to stand
        #Returns false if the player chooses to get another card


    def make_move(self, dealer_original_value, training_flag):

        while not (self.stand(dealer_original_value, training_flag)):
            print 'Action: Asks for a card'
            new_card = self.game.get_deck().give_a_card()
            self.get_card(new_card)
            print str(new_card.rank) + ' of ' + str(new_card.suit)


    #the fg_values that are updated, are those that take you to directly win or lose. The previous values do not get updated
    def update_fg_values(self, result):
        alpha = 0.5  # it can be modified
        gamma = 0.5  # it can be modified, but between 0 and 1
        reward = 0.0

        if result == 'win':
            reward = 0.2
        elif result == 'lose':
            reward = -0.2

        terminal_s_a = self.temp_state_action[len(self.temp_state_action) - 1]
        q_s_a = self.fg_values_matrix[self.temp_state_action[len(self.temp_state_action) - 1]]

        # max Q(s', a') is 0, because is a terminal state
        self.fg_values_matrix[terminal_s_a] = (1 - alpha) * q_s_a + alpha * (reward + gamma * 0)

        # if is not a terminal state-action, the reward is 0
        reward = 0.0
        if (len(self.temp_state_action) - 2) >= 0:
            for x in range((len(self.temp_state_action) - 2), -1):
                s_a = self.temp_state_action[x]
                s_a_prime = self.temp_state_action[x + 1]
                q_s_a_x = self.fg_values_matrix[s_a]

                # CALCULATE THE MAX Q(s',a')
                q_stand_value_prime = self.fg_values_matrix[s_a_prime, 'stand']
                q_continue_value_prime = self.fg_values_matrix[s_a_prime, 'continue']
                q_double_bet_value_prime = self.fg_values_matrix[s_a_prime, 'double bet']
                q_values_prime = [q_stand_value_prime, q_continue_value_prime, q_double_bet_value_prime]

                self.fg_values_matrix[s_a] = (1 - alpha) * q_s_a_x + alpha * [reward + gamma * max(q_values_prime)]



    def update_split_matrix(self, points):
        if (points == 2):
            self.split_matrix['yes'] += 0.04

        elif (points == 0):
            self.split_matrix['no'] += 0.02

        #If you win 1 and lose 1 split hand, the matrix stays the same


    def restart_temp_state_action(self):
        self.temp_state_action = []

    def print_hand(self):
        print str(self.hand.cards[0].rank) + ' of ' + str(self.hand.cards[0].suit)
        print str(self.hand.cards[1].rank) + ' of ' + str(self.hand.cards[1].suit) + '\n'





class Dealer(Player):

    def __init__(self, game):
        self.game = game
        self.hand = Hand()


    def make_move(self, player_value):

        while(self.calculate_value() < player_value and player_value <= 21 and self.calculate_value() < 17):
            print '\n Dealer Action: Asks for a card '
            new_card = self.game.get_deck().give_a_card()
            self.get_card(new_card)
            print str(new_card.rank) + ' of ' + str(new_card.suit)

        print '\nDealer Action: Stand '


    def print_victories(self):
        print 'Dealer won ' + str(self.victories) + ' times'


    def print_hand(self):
        print str(self.hand.cards[0].rank) + ' of ' + str(self.hand.cards[0].suit)

