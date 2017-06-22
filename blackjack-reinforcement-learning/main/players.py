from random import randint

class Player:

    game = None
    hand = []
    victories = 0

    def get_card(self, card):
        self.hand.append(card)

    def clean_hand(self):
        self.hand = []

    def calculate_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value()

        return value

    def compute_victory(self):
        self.victories += 1


class HumanPlayer(Player):

    coins = 0
    actions = []
    states = []
    fg_values_matrix = {}
    ace_values_matrix = {}
    split_matrix = {}
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

        #Initialize the Ace possible values. It can be 1 or 11
        #The initial value is 0.5 for both Ace possibility
        self.ace_values_matrix[1] = 0.5
        self.ace_values_matrix[11] = 0.5



    def bet(self):
        #This must get the player's bet from the command line
        #Returns the bet
        self.coins -= 1
        return 1 #The automated player only bets 1 coin

    def get_prize(self, prize):
        #This gives the player the prize if won a hand
        self.coins += prize

    def print_victories(self):
        print 'Player won ' + str(self.victories) + ' times'

    def ask_if_continues(self):
        #To modify

        random_number = randint(0, 9)
        if random_number < 0.01: #It will likely continue forever!
            return False
        else:
            return True
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

    def have_an_ace(self):
        for card in self.hand:
            if (card.rank == 'Ace'):
                return True

        return False

    def have_more_than_1_ace(self):
        aces_count = 0
        for card in self.hand:
            if (card.rank == 'Ace'): aces_count += 1

        if (aces_count > 1): return True
        else: return False

    def define_ace_value(self, training_flag):

        #This method should decide the value of every ace you've got

        #Unused code
        """
        if self.have_more_than_1_ace():
            #Aces are naturally 1. If I have more than 1, then I'll set one of them to 11
            #After that, I'll check that I'm not over 21.
            for card in self.hand:

                if card.get_value() == 1:
                    card.set_ace_value(11)
                    break
                    #This line is necessary to get out of the loop whenever the first ace is reached

            if (self.calculate_value() > 21):

                #If you are over 21, then set every Ace to 1
                for card in self.hand:

                    if card.get_value() == 11:
                        card.set_value(1)
        """


        if training_flag: #When I'm training, I choose randomly

            number = randint(0, 9)

            if (number > 5):
                for card in self.hand:

                    if card.get_value() == 1:
                        card.set_value(11)
                        break #Only the first one is turned to 11, if you have more than one

            else:
                for card in self.hand:

                    if card.get_value() == 11:
                        card.set_value(1)


        else: #If I'm not training, I just pick the best option from the matrix

            one_value = self.ace_values_matrix[1]
            eleven_value = self.ace_values_matrix[11]

            if one_value >= eleven_value:

                for card in self.hand:

                    if card.get_value() == 11:
                        card.set_value(1)

            else:

                for card in self.hand:

                    if card.get_value() == 1:
                        card.set_value(11)
                        break
                        #Again, the break line is necessary because you can only have
                        #ONE eleven-ace per hand, or you'd be over 21

    def stand(self, dealer_original_value, training_flag):

        if (self.have_an_ace):
            self.define_ace_value(training_flag)

        if training_flag:

            random_number = randint(0, 9)
            if random_number < 5:
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


    #the fg_values that are updated, are those that take you to directly win or lose. The previous values do not get updated
    def update_fg_values(self, result):
        number = 0
        if result == 'win':
            number = 0.02
        elif result == 'lose':
            number = -0.04

        #self.update_full_path_values(number)
        self.update_only_the_terminal_value(number)
        #self.update_every_value(number) //TODO: Implement and see how it changes the results. This means, add value to the winning node, substract value from every other

        if self.have_an_ace():

            #Ace values in the matrix are updated
            ace_value = 1

            for card in self.hand:
                if (card.get_value() == 11): ace_value = 11

            if result == 'win':
                number = 0.02

            elif result == 'lose':
                number = -0.04

            self.ace_values_matrix[ace_value] += number

    def update_full_path_values(self, number):
        for x in range(0, len(self.temp_state_action)):
            self.fg_values_matrix[self.temp_state_action[x]] += number

    def update_only_the_terminal_value(self, number):
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


    def print_victories(self):
        print 'Dealer won ' + str(self.victories) + ' times'