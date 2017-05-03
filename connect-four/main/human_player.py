class HumanPlayer:
    _color = None
    _type = None

    def __init__(self, color):
        self._type = "Human"
        self._color = color

    def get_move(self, board):
        column = None
        while column == None:
            try:
                column = int(raw_input("Select your move : ")) - 1
            except ValueError:
                column = None
            if 0 <= column <= 6:
                return column
            else:
                column = None
                print("The number must be between 1 and 7")