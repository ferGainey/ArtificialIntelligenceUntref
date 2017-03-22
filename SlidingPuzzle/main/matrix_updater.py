from movement_evaluator import MovementEvaluator

class MatrixUpdater:

    def update_matrix(self, matrix, movement):
        if len(matrix) == 3:
            edited_matrix = [['-1','-1','-1'], ['-1','-1','-1'], ['-1','-1','-1']]
            for i in range(0,3):
                for j in range(0,3):
                    edited_matrix[i][j] = matrix[i][j]
        if len(matrix) == 4:
            edited_matrix = [['-1','-1','-1','-1'], ['-1','-1','-1','-1'], ['-1','-1','-1','-1'], ['-1','-1','-1','-1']]
            for i in range(0,4):
                for j in range(0,4):
                    edited_matrix[i][j] = matrix[i][j]

        movement_evaluator = MovementEvaluator()
        free_position_row = movement_evaluator.search_free_position_row(edited_matrix)
        free_position_column = movement_evaluator.search_free_position_column(edited_matrix)
        if movement == 'up':
            new_free_position_row = free_position_row - 1
            new_free_position_column = free_position_column
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        elif movement == 'right':
            new_free_position_row = free_position_row
            new_free_position_column = free_position_column + 1
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        elif movement == 'down':
            new_free_position_row = free_position_row + 1
            new_free_position_column = free_position_column
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        elif movement == 'left':
            new_free_position_row = free_position_row
            new_free_position_column = free_position_column - 1
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        return edited_matrix