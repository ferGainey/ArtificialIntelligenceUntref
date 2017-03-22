class MatrixPrinter:

    def print_matrix(self, matrix):
        matrix_string = ''
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                matrix_string += matrix[i][j]
                matrix_string += ' '
            matrix_string += '\n'
        print matrix_string