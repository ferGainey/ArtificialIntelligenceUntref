class Card:

    value = None
    suit = None
    rank = None

    def __init__(self, rank, suit):

        self.initialize_values(rank, suit)

    def initialize_values(self, rank, suit):
        if suit.lower() == 'diamonds' or suit.lower() == 'spades' or suit.lower() == 'clubs' or suit.lower() == 'hearts':

            if rank == 'Ace':
                self.rank = rank
                self.suit = suit
                self.value = 11

            elif rank == '2':
                self.rank = rank
                self.suit = suit
                self.value = 2

            elif rank == '3':
                self.rank = rank
                self.suit = suit
                self.value = 3

            elif rank == '4':
                self.rank = rank
                self.suit = suit
                self.value = 4

            elif rank == '5':
                self.rank = rank
                self.suit = suit
                self.value = 5

            elif rank == '6':
                self.rank = rank
                self.suit = suit
                self.value = 6

            elif rank == '7':
                self.rank = rank
                self.suit = suit
                self.value = 7

            elif rank == '8':
                self.rank = rank
                self.suit = suit
                self.value = 8

            elif rank == '9':
                self.rank = rank
                self.suit = suit
                self.value = 9

            elif rank == '10':
                self.rank = rank
                self.suit = suit
                self.value = 10

            elif rank == 'Jack':
                self.rank = rank
                self.suit = suit
                self.value = 10

            elif rank == 'Queen':
                self.rank = rank
                self.suit = suit
                self.value = 10

            elif rank == 'King':
                self.rank = rank
                self.suit = suit
                self.value = 10

            else:
                print 'Select an existing card rank!'

        else:
            print 'Select an existing card suit!'

    def get_value(self):
        return self.value

    def get_rank(self):
        return self.rank

    def set_value(self, value):

        if (self.rank == 'Ace'):
            self.value = value
