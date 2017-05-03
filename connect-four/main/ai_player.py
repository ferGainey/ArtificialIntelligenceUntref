import time
from copy import deepcopy

class AIPlayer:
    _board_width = None
    _board_height = None
    _colors = [None, None]
    _color = None
    _depth_search = 5
    _ai_first_move = False

    def __init__(self, color, board):
        self._type = "AI"
        self._board_width = board.board_width
        self._board_height = board.board_height
        self._colors[0] = board.colors[0]
        self._colors[1] = board.colors[1]
        self._color = color

    def get_move(self, board):
        first_round = True
        for j in xrange(len(board[0])):
            if board[5][j] != ' ':
                first_round = False
            elif self._ai_first_move == False:
                if board[5][3] == ' ':
                    self._ai_first_move = True
                    return 3 #atack the center!
                elif board[5][2] == ' ':
                    return 2 #atack the center!
        if first_round:
            return 3
        else:
            #return self._get_best_move_beta(board)
            return self._get_best_move(board)

    def _get_best_move(self, grid):
        absolute_start_time = time.time()
        # determine opponent's color
        if self._color == self._colors[0]:
            human_color = self._colors[1]
        else:
            human_color = self._colors[0]

        # enumerate all the legal moves of the first node
        # each legal move will be mapped with their alpha values
        legal_moves = {}
        # check for each column if the move is legal
        for col in xrange(self._board_width):
            if self._is_legal_move(col, grid):
                # simulate the move in column col for the current player and generate the new state (board)
                tmp_board = self.simulate_move(grid, col, self._color)
                start_time = time.time()
                legal_moves[col] = -self._search_value_function(self._depth_search - 1, tmp_board, human_color, start_time)

        best_alpha = -99999999
        best_move = None
        moves = legal_moves.items()
        # search the best move (with the highest alpha value)
        for move, alpha in moves:
            print str(move) + "  el alpha es:" + str(alpha)
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move
        print "the absolute time of though was:  " + str(time.time() - absolute_start_time)
        return best_move

    def _search_value_function(self, depth, grid, curr_player_color, start_time):
        current_time = time.time()
        # enumerate all legal moves from this state
        legal_moves = []
        for j in xrange(self._board_width):
            if self._is_legal_move(j, grid):
                # simulate the move in column j for curr_player
                tmp_board = self.simulate_move(grid, j, curr_player_color)
                legal_moves.append(tmp_board)
        #each original start move have a time of 1.4285, this is because they are maximum 7 moves. And the idea is that
        #the AI must move in less than second. So (10 / 7 = 1.42857).
        if depth == 0 or len(legal_moves) == 0 or self._game_is_over(grid): #or (current_time - start_time) > 1.428571429:
            # return the heuristic value of node
            return self._evaluation_function(depth, grid, curr_player_color)

        # determine opponent's color
        if curr_player_color == self._colors[0]:
            opp_player_color = self._colors[1]
        else:
            opp_player_color = self._colors[0]

        alpha = -99999999
        for child in legal_moves:
            if child == None:
                print("child == None (search)")
            alpha = max(alpha, -self._search_value_function(depth - 1, child, opp_player_color, start_time))
        return alpha

    def _is_legal_move(self, column, grid):
        #this function check if a move (column) is a legal move
        for i in xrange(self._board_height - 1, -1, -1):
            if grid[i][column] == ' ':
                # once we find an empty position, we can ensure that it is a legal move
                return True
        # if no blank position was found, it is because the column is full
        return False

    def _game_is_over(self, grid):
        horizontal_lines_list_O = self.find_horizontal_line_beta(grid, self._colors[0])
        horizontal_fours_O = horizontal_lines_list_O[2]
        horizontal_lines_list_X = self.find_horizontal_line_beta(grid, self._colors[1])
        horizontal_fours_X = horizontal_lines_list_X[2]
        vertical_lines_list_O = self.find_vertical_line_beta(grid, self._colors[0])
        vertical_fours_O = vertical_lines_list_O[2]
        vertical_lines_list_X = self.find_vertical_line_beta(grid, self._colors[1])
        vertical_fours_X = vertical_lines_list_X[2]
        diagonal_lines_list_O = self.find_diagonal_line_beta(grid, self._colors[0])
        diagonal_fours_O = diagonal_lines_list_O[2]
        diagonal_lines_list_X = self.find_diagonal_line_beta(grid, self._colors[1])
        diagonal_fours_X = diagonal_lines_list_X[2]
        if horizontal_fours_O > 0 or diagonal_fours_O > 0 or vertical_fours_O > 0:
            return True
        elif horizontal_fours_X > 0 or diagonal_fours_X or vertical_fours_X > 0:
            return True
        else:
            return False

    def simulate_move(self, board, column, color):
        #first I copy the original board
        tmp_grid = deepcopy(board)
        #then I search where to put the piece
        for i in xrange(self._board_height - 1, -1, -1):
            if tmp_grid[i][column] == ' ':
                tmp_grid[i][column] = color
                return tmp_grid

    def _evaluation_function(self, depth, board, player_color):
        if player_color == self._colors[0]:
            opp_color = self._colors[1]
        else:
            opp_color = self._colors[0]
        # AI player
        ia_horizontal_list = self.find_horizontal_line_beta(board, player_color)
        ia_vertical_list = self.find_vertical_line_beta(board, player_color)
        ia_diagonal_list = self.find_diagonal_line_beta(board, player_color)
        #
        ia_diagonal_fours = int(ia_diagonal_list[2])
        ia_horizontal_fours = int(ia_horizontal_list[2])
        ia_vertical_fours = int(ia_vertical_list[2])
        ia_diagonal_threes = int(ia_diagonal_list[1])
        ia_horizontal_threes = int(ia_horizontal_list[1])
        ia_vertical_threes = int(ia_vertical_list[1])
        ia_diagonal_twos = int(ia_diagonal_list[0])
        ia_horizontal_twos = int(ia_horizontal_list[0])
        ia_vertical_twos = int(ia_vertical_list[0])
        # Human
        human_horizontal_list = self.find_horizontal_line_beta(board, opp_color)
        human_vertical_list = self.find_vertical_line_beta(board, opp_color)
        human_diagonal_list = self.find_diagonal_line_beta(board, opp_color)
        #
        human_diagonal_fours = int(human_diagonal_list[2])
        human_horizontal_fours = int(human_horizontal_list[2])
        human_vertical_fours = int(human_vertical_list[2])
        human_diagonal_threes = int(human_diagonal_list[1])
        human_horizontal_threes = int(human_horizontal_list[1])
        human_vertical_threes = int(human_vertical_list[1])
        human_diagonal_twos = int(human_diagonal_list[0])
        human_horizontal_twos = int(human_horizontal_list[0])
        human_vertical_twos = int(human_vertical_list[0])
        # calculate and return the alpha
        if human_diagonal_fours > 0 or human_horizontal_fours > 0 or human_vertical_fours > 0:
            #human reach the fours
            return -1000000 * (human_diagonal_fours + human_horizontal_fours + human_vertical_fours) #- depth
        else:
            value = (ia_diagonal_fours * 1000000 + ia_horizontal_fours * 1000000 + ia_vertical_fours * 1000000
                    + ia_diagonal_threes * 1390.7 + ia_horizontal_threes * 520.6 + ia_vertical_threes * 250.8 + ia_diagonal_twos * 450.7
                    + ia_horizontal_twos * 150.5 + ia_vertical_twos * 50.5) - (human_diagonal_fours * 1000000
                                                                        + human_horizontal_fours * 1000000
                                                                        + human_vertical_fours * 1000000
                    + human_diagonal_threes * 1390.8 + human_horizontal_threes * 520.71 + human_vertical_threes * 250.8 + human_diagonal_twos * 450.8
                    + human_horizontal_twos * 150.62 + human_vertical_twos * 50.5) #+ depth
            return value

    def find_horizontal_line_beta(self, board, color):
        horizontal_twos = 0
        horizontal_threes = 0
        horizontal_fours = 0
        for i in xrange(self._board_height):
            j = 0
            while j < self._board_width:
                consecutive_count = 0
                if board[i][j] == color:
                    if (j + 1) < self._board_width:
                        for k in xrange(j+1, self._board_width):
                            if board[i][k] == color:
                                consecutive_count += 1
                                j += 1
                            else:
                                j += 1
                                break
                j += 1
                if consecutive_count == 1:
                    horizontal_twos += 1
                if consecutive_count == 2:
                    horizontal_threes += 1
                if consecutive_count >= 3:
                    horizontal_fours += 1
        horizontal_list = [0, 0, 0]
        horizontal_list[0] = horizontal_twos
        horizontal_list[1] = horizontal_threes
        horizontal_list[2] = horizontal_fours
        return horizontal_list


    def find_vertical_line_beta(self, board, color):
        vertical_twos = 0
        vertical_threes = 0
        vertical_fours = 0
        for j in xrange(self._board_width):
            i = 0
            while i < self._board_height:
                consecutive_count = 0
                if board[i][j] == color:
                    if (i + 1) < self._board_height:
                        for k in xrange(i+1, self._board_height):
                            if board[k][j] == color:
                                consecutive_count += 1
                                i += 1
                            else:
                                i += 1
                                break
                i += 1
                if consecutive_count == 1:
                    vertical_twos += 1
                if consecutive_count == 2:
                    vertical_threes += 1
                if consecutive_count >= 3:
                    vertical_fours += 1
        vertical_list = [0, 0, 0]
        vertical_list[0] = vertical_twos
        vertical_list[1] = vertical_threes
        vertical_list[2] = vertical_fours
        return vertical_list


    def find_diagonal_line_beta(self, board, color):
        diagonal_twos = 0
        diagonal_threes = 0
        diagonal_fours = 0
        for j in xrange(self._board_width):
            i = 0
            consecutive_count = 0
            while i < self._board_height:
                if (j + i) < self._board_width:
                    if board[i][i + j] == color:
                        consecutive_count += 1
                    else:
                        if consecutive_count == 2:
                            diagonal_twos += 1
                        if consecutive_count == 3:
                            diagonal_threes += 1
                        if consecutive_count >= 4:
                            diagonal_fours += 1
                        consecutive_count = 0
                i += 1
            if consecutive_count >= 1:
                if consecutive_count == 2:
                    diagonal_twos += 1
                if consecutive_count == 3:
                    diagonal_threes += 1
                if consecutive_count >= 4:
                    diagonal_fours += 1

        ######
        for i in xrange(self._board_height - 1):
            j = 1
            consecutive_count = 0
            while j < self._board_height:
                if (j + i) < self._board_height:
                    if board[i + j][j - 1] == color:
                        consecutive_count += 1
                    else:
                        if consecutive_count == 2:
                            diagonal_twos += 1
                        if consecutive_count == 3:
                            diagonal_threes += 1
                        if consecutive_count >= 4:
                            diagonal_fours += 1
                        consecutive_count = 0
                    #
                j += 1
            if consecutive_count >= 1:
                if consecutive_count == 2:
                    diagonal_twos += 1
                if consecutive_count == 3:
                    diagonal_threes += 1
                if consecutive_count >= 4:
                    diagonal_fours += 1

        #positive diagonal
        for j in xrange(self._board_width):
            i = 0
            consecutive_count = 0
            while i < self._board_height:
                if (self._board_width - 1 - j - i) >= 0:
                    if board[i][self._board_width - 1 - j - i] == color:
                        consecutive_count += 1
                    else:
                        if consecutive_count == 2:
                            diagonal_twos += 1
                        if consecutive_count == 3:
                            diagonal_threes += 1
                        if consecutive_count >= 4:
                            diagonal_fours += 1
                        consecutive_count = 0
                i += 1
            if consecutive_count >= 1:
                if consecutive_count == 2:
                    diagonal_twos += 1
                if consecutive_count == 3:
                    diagonal_threes += 1
                if consecutive_count >= 4:
                    diagonal_fours += 1

        ######
        for i in xrange(self._board_height - 1):
            j = 1
            consecutive_count = 0
            while j < self._board_height:
                if (j + i) < self._board_height:
                    if board[i + j][7 - j] == color:
                        consecutive_count += 1
                    else:
                        if consecutive_count == 2:
                            diagonal_twos += 1
                        if consecutive_count == 3:
                            diagonal_threes += 1
                        if consecutive_count >= 4:
                            diagonal_fours += 1
                        consecutive_count = 0
                    #
                j += 1
            if consecutive_count >= 1:
                if consecutive_count == 2:
                    diagonal_twos += 1
                if consecutive_count == 3:
                    diagonal_threes += 1
                if consecutive_count >= 4:
                    diagonal_fours += 1
        diagonal_list = [0, 0, 0]
        diagonal_list[0] = diagonal_twos
        diagonal_list[1] = diagonal_threes
        diagonal_list[2] = diagonal_fours
        return diagonal_list

        # To do:
        # - Add a method that look for incomplete diagonal. That means that if it exists blank spaces between two pieces
        # and the space is enough to do do 4 in line, I can conclude that it is a good situation.
        # - Make a revision of the points assigned to each state
