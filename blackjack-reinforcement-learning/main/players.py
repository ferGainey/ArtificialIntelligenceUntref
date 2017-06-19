from random import randint

class Player:

    game = None
    hand = []

    def get_card(self, card):
        self.hand.append(card)

    def clean_hand(self):
        self.hand = []

    def calculate_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value()

        return value


class HumanPlayer(Player):

    coins = 0
    actions = []
    states = []
    fg_values_matrix = {}
    temp_state_action = []

    def __init__(self, game, coins):
        self.game = game
        self.coins = coins
        #the actions are continue or stand. Split and bet more coins will be developed later
        self.actions = ['continue', 'stand']
        """
        The human player can take decisions only between 2 and 20. The '2' case is the lowest initial hand that the human
        can receive (two Aces). And the '20' case is the highest value that human can obtain without winning or loosing
        that round.
        """
        for i in range(2,21):
            #The lowest value card that the dealer can receive is 1 (an Ace) and the highest is 10 (King, Queen, Joker, Ten)
            #In this initial implementation the Ace will have one unique value: 1. Later it can be 1 or 11.
            for j in range(1,11):
                self.states.append((i,j))

        #Initialize fg_values_matrix with 0,5 probability each one. I use a dictionary to do this.
        # The key is: (the state,action). And the value will be the fg_value
        for x in range(0, len(self.states)):
            for y in range(0, len(self.actions)):
                current_state = self.states[x]
                current_action = self.actions[y]
                self.fg_values_matrix[current_state, current_action] = 0.5




    def bet(self):
        #TODO: Implement
        #This must get the player's bet from the command line
        #Returns the bet
        pass

    def ask_if_continues(self):
        #To modify
        random_number = randint(0, 9)
        if random_number < 1:
            return False
        else:
            return True
        #TODO: Implement
        #Returns true if the player keeps playing
        #Returns false to stop playing
        #pass

    def has_two_equal_valued_cards(self):

        if(self.hand[0].get_value() == self.hand[1].get_value()): return True
        else: return False

    def wants_to_split(self):
        #Returns true if the player chooses to split
        #Returns false if the player chooses to keep playing without splitting
        #TODO: Implement
        pass

    def stand(self, dealer_original_value, training_flag):
        if training_flag:
            random_number = randint(0, 9)
            if random_number < 3:
                if (self.calculate_value() <= 20):
                    self.temp_state_action.append(((self.calculate_value(), dealer_original_value),'continue'))
                return False
            else:
                if self.calculate_value() <= 20:
                    self.temp_state_action.append(((self.calculate_value(), dealer_original_value), 'stand'))
                return True
        #when it is not training
        elif self.calculate_value() <= 20:
            # compare the values, if stand_value is higher than continue_value, the next action will be stand
            stand_value = self.fg_values_matrix[(self.calculate_value(), dealer_original_value), 'stand']
            #print stand_value
            continue_value = self.fg_values_matrix[(self.calculate_value(), dealer_original_value), 'continue']
            #print continue_value
            if stand_value > continue_value:
                return True
            else:
                return False
        return True
        #Returns true if the player chooses to stand
        #Returns false if the player chooses to get another card
        #TODO: Implement
        #pass

    def make_move(self, dealer_original_value, training_flag):
        """
        #If the dealer is winning, then the player asks for a card. Obviously!
        while (self.calculate_value() < dealer_original_value):

            self.get_card(self.game.get_deck().give_a_card())

        #Once the player's hand value is higher than the dealer's, then
        #he chooses when to stand
        """
        while not (self.stand(dealer_original_value, training_flag)):
            new_card = self.game.get_deck().give_a_card()
            self.get_card(new_card)
            print str(new_card.rank) + ' of ' + str(new_card.suit)

        if (self.calculate_value() > 21):

             #TODO: Tell the game the player loses
             pass

    #the fg_values that are updated, are those that take you to directly win or lose. The previous values do not get updated
    def update_fg_values(self, result):
        number = 0
        if result == 'win':
            number = 0.01
        elif result == 'lose':
            number = -0.01
        """
        #with this code you update the complete path
        for x in range(0, len(self.temp_state_action)):
            self.fg_values_matrix[self.temp_state_action[x]] += number
        """
        self.fg_values_matrix[self.temp_state_action[len(self.temp_state_action) - 1]] += number

    def restart_temp_state_action(self):
        self.temp_state_action = []





class Dealer(Player):

    def __init__(self, game):
        self.game = game

    def make_move(self, player_value):

        while(self.calculate_value() < player_value and player_value <= 21 and self.calculate_value() < 17):
            new_card = self.game.get_deck().give_a_card()
            self.get_card(new_card)
            print str(new_card.rank) + ' of ' + str(new_card.suit)

        if (self.calculate_value() > 21):

            #TODO: Tell the game the dealer
            pass

