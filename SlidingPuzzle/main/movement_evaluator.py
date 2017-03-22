class MovementEvaluator:

    #the movements follow always the same order: 1)up, 2)right, 3)down, 4)left
    def get_possible_movements(self, matrix):
        free_position_row = self.search_free_position_row(matrix)
        free_position_column = self.search_free_position_column(matrix)
        movements_list = None
        #column in position 0, and the row in all the posible positions
        if free_position_row == 0 and free_position_column == 0:
            movements_list = ['right', 'down']
        elif free_position_row == len(matrix)-1 and free_position_column == 0:
            movements_list = ['up', 'right']
        elif free_position_row > 0 and free_position_row < len(matrix)-1 and free_position_column == 0:
            movements_list = ['up', 'right', 'down']
        #column in last position and the row in all the possible positions
        elif free_position_row == 0 and free_position_column == len(matrix)-1:
            movements_list = ['down', 'left']
        elif free_position_row == len(matrix)-1 and free_position_column == len(matrix)-1:
            movements_list = ['up', 'left']
        elif free_position_row > 0 and free_position_row < len(matrix)-1 and free_position_column == len(matrix)-1:
            movements_list = ['up', 'down', 'left']
        #column is in the middle and the row is in all the possible positions
        elif free_position_row == 0 and free_position_column < len(matrix) - 1 and free_position_column > 0:
            movements_list = ['right', 'down', 'left']
        elif free_position_row == len(matrix) - 1 and free_position_column < len(matrix) - 1 and free_position_column > 0:
            movements_list = ['up', 'right' , 'left']
        elif free_position_row > 0 and free_position_row < len(matrix) - 1 and free_position_column < len(matrix) - 1 and free_position_column > 0:
            movements_list = ['up', 'right', 'down', 'left']
        return movements_list


    def search_free_position_row(self, matrix):
        free_position_row = -1
        for current_row in range(0, len(matrix)):
            for number in matrix[current_row]:
                if number == '0':
                    free_position_row = current_row
                    break
        return  free_position_row

    def search_free_position_column(self, matrix):
        free_position_column = -1
        for current_row in range(0, len(matrix)):
            position = 0
            for number in matrix[current_row]:
                if number == '0':
                    free_position_column = position
                    break
                position += 1
        return  free_position_column

