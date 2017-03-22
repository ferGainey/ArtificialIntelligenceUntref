class BinarySearch:

    def do_search(self, received_list, matrix):
        item = self.convert_matrix_to_number(matrix)
        first = 0
        last = len(received_list) - 1
        found = False
        while first <= last and not found:
            midpoint = (first + last) // 2
            if received_list[midpoint] == item:
                found = True
            else:
                if item < received_list[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found

    def convert_matrix_to_number(self, matrix):
        number_str = ''
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                number_str += matrix[i][j]
        item = int(number_str)
        return item
