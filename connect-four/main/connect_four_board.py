from __future__ import print_function
import os
from human_player import HumanPlayer
from ai_player import AIPlayer


class ConnectFourBoard(object):
    board_width = 7
    board_height = 6
    matrix = None
    round = 1
    _finished = False
    _winner = None
    _current_player = None
    players = [None, None]
    colors = ['O', 'X']

    def start(self):
        self._print_state()
        while not self._finished:
            self._next_move()

    def start_new(self, option_choice):
        os.system(['clear', 'cls'][os.name == 'nt'])
        # reset game status
        self._round = 1
        self._finished = False
        self._winner = None
        # the human select if he wants to play first or second
        if option_choice == 1:
            self.players[0] = HumanPlayer(self.colors[0])
            self.players[1] = AIPlayer(self.colors[1], self)
            self._current_player = self.players[0]
        elif option_choice == 2:
            self.players[0] = AIPlayer(self.colors[0], self)
            self.players[1] = HumanPlayer(self.colors[1])
            self._current_player = self.players[0]

        # clear grid with white spaces
        self.matrix = []
        for i in xrange(self.board_height):
            self.matrix.append([])
            for j in xrange(self.board_width):
                self.matrix[i].append(' ')

        # start a new game
        self.start()

    def _switch_player(self):
        if self._current_player == self.players[0]:
            self._current_player = self.players[1]
        else:
            self._current_player = self.players[0]

    def _next_move(self):
        column = self._current_player.get_move(self.matrix)
        # search the available line in the selected column
        for i in xrange(self.board_height - 1, -1, -1):
            if self.matrix[i][column] == ' ':
                # set the color in the grid
                self.matrix[i][column] = self._current_player._color
                self._check_status()
                self._print_state()
                # swith player
                self._switch_player()
                # increment the round
                self._round += 1
                return

        # column selected is full
        print("This column is full. Please select another one")
        return

    def _check_status(self):
        if self._is_full():
            self._finished = True
        elif self._is_connect_four():
            self._finished = True
            self._winner = self._current_player

    def _is_full(self):
        return self._round > self.board_width * self.board_height

    def _is_connect_four(self):
        # for each box of the grid
        for i in xrange(self.board_height - 1, -1, -1):
            for j in xrange(self.board_width):
                if self.matrix[i][j] != ' ':
                    # check for vertical connect four
                    if self._find_vertical_four(i, j):
                        return True

                    # check for horizontal connect four
                    if self._find_horizontal_four(i, j):
                        return True

                    # check for diagonal connect four
                    if self._find_diagonal_four(i, j):
                        return True

        return False

    def _find_vertical_four(self, row, col):
        consecutive_count = 0

        if row + 3 < self.board_height:
            for i in xrange(4):
                if self.matrix[row][col] == self.matrix[row + i][col]:
                    consecutive_count += 1
                else:
                    break

            # define the winner
            if consecutive_count == 4:
                if self.players[0]._color == self.matrix[row][col]:
                    self._winner = self.players[0]
                else:
                    self._winner = self.players[1]
                return True

        return False

    def _find_horizontal_four(self, row, col):
        consecutive_count = 0

        if col + 3 < self.board_width:
            for i in xrange(4):
                if self.matrix[row][col] == self.matrix[row][col + i]:
                    consecutive_count += 1
                else:
                    break

            # define the winner
            if consecutive_count == 4:
                if self.players[0]._color == self.matrix[row][col]:
                    self._winner = self.players[0]
                else:
                    self._winner = self.players[1]
                return True

        return False

    def _find_diagonal_four(self, row, col):
        consecutive_count = 0
        # check positive sense
        if row + 3 < self.board_height and col + 3 < self.board_width:
            for i in xrange(4):
                if self.matrix[row][col] == self.matrix[row + i][col + i]:
                    consecutive_count += 1
                else:
                    break

            # define the winner
            if consecutive_count == 4:
                if self.players[0]._color == self.matrix[row][col]:
                    self._winner = self.players[0]
                else:
                    self._winner = self.players[1]
                return True

        consecutive_count = 0
        # check negative sense
        if row - 3 >= 0 and col + 3 < self.board_width:
            for i in xrange(4):
                if self.matrix[row][col] == self.matrix[row - i][col + i]:
                    consecutive_count += 1
                else:
                    break

            # define the winner
            if consecutive_count == 4:
                if self.players[0]._color == self.matrix[row][col]:
                    self._winner = self.players[0]
                else:
                    self._winner = self.players[1]
                return True

        return False

    def _print_state(self):
        #print ("________________________________________")
        # print the round
        # cross-platform clear screen
        os.system(['clear', 'cls'][os.name == 'nt'])
        print("             Round: " + str(self._round))
        print("")
        for i in xrange(self.board_height):
            print ('')
            for j in xrange(self.board_width):
                if self.matrix[i][j] != ' ':
                    print (str(self.matrix[i][j]) + ' ', end='')
                else:
                    print('- ', end='')
        print('')
        for k in xrange(self.board_width):
            print("%d " % (k + 1), end=''),
        print("")

        # print a final message when the game is finished
        if self._finished:
            print("The game is over!")
            if self._winner != None:
                if self._winner._type == "AI":
                    print ("Fatality!")
                    print ("AI wins! Flawless victory!")
                else:
                    print ("Human wins")
                    print ("If I had less bugs, I would win")

            else:
                print("This was a draw")