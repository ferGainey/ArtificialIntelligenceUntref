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

   def __init__(self, game, coins):
       self.game = game
       self.coins = coins

   def bet(self):
       #TODO: Implement
       #This must get the player's bet from the command line
       #Returns the bet
       pass

   def ask_if_continues(self):
       #TODO: Implement
       #Returns true if the player keeps playing
       #Returns false to stop playing
       pass

   def has_two_equal_valued_cards(self):

       if(self.hand[0].get_value() == self.hand[1].get_value()): return True
       else: return False

   def wants_to_split(self):
       #Returns true if the player chooses to split
       #Returns false if the player chooses to keep playing without splitting
       #TODO: Implement
       pass

   def stand(self):
       #Returns true if the player chooses to stand
       #Returns false if the player chooses to get another card
       #TODO: Implement
       pass

   def make_move(self, dealer_original_value):

       #If the dealer is winning, then the player asks for a card. Obviously!
       while (self.calculate_value() < dealer_original_value):

           self.get_card(self.game.get_deck().give_a_card())

       #Once the player's hand value is higher than the dealer's, then
       #he chooses when to stand
       while not (self.stand()):

           self.get_card(self.game.get_deck().give_a_card())

       if (self.calculate_value() > 21):

            #TODO: Tell the game the player loses
            pass





class Dealer(Player):

    def __init__(self, game):
        self.game = game

    def make_move(self, player_value):

        while(self.calculate_value() < player_value):

            self.get_card(self.game.get_deck().give_a_card())

        if (self.calculate_value() > 21):

            #TODO: Tell the game the dealer
            pass

