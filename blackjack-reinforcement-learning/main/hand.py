class Hand:

    hardness = None
    cards = []

    def __init__(self):
        self.hardness = 'h' #This can be 'h' = hard or 's' = soft. Default initialized as hard


    def add_card(self, card):

        if (card.rank == 'Ace'):
            self.hardness = 's'

        self.cards.append(card)

    def clean(self):
        self.cards = []
        self.hardness = 'h'

    def calculate_value(self):
        value = 0
        for card in self.cards:
            value += card.get_value()

        return value

    def calculate_status(self):

        #Status is a mix of the value and the hardness
        #This returns something like '14s'
        status = ''
        status += str(self.calculate_value())
        status += self.hardness
        return status

    def get_hardness(self):
        return self.hardness

    def has_two_equal_valued_cards(self):

        if (self.cards[0].get_value() == self.cards[1].get_value()):
            return True
        else:
            return False

    def have_an_ace(self):
        for card in self.cards:
            if (card.rank == 'Ace'):
                return True

        return False

    def have_more_than_1_ace(self):
        aces_count = 0
        for card in self.cards:
            if (card.rank == 'Ace'): aces_count += 1

        if (aces_count > 1): return True
        else: return False

    def set_an_ace_1(self):

        #This will turn to 1 the first found ace
        for card in self.cards:

            if (card.get_value == 11):

                card.set_value(1)
                break


