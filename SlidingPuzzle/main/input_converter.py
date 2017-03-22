class InputConverter:

    def convert_input(self, user_input):
        input_string = str(user_input)
        input_string_list = input_string.split(',')
        return input_string_list

    def create_matrix(self, user_input_list):
        if len(user_input_list) == 9:
            three_x_three_matrix = [[],[],[]]
            current_number = 1
            for number in user_input_list:
                if current_number <= 3:
                    three_x_three_matrix[0].append(number)
                    current_number += 1
                elif current_number <= 6:
                    three_x_three_matrix[1].append(number)
                    current_number += 1
                elif current_number <= 9:
                    three_x_three_matrix[2].append(number)
                    current_number += 1
            return three_x_three_matrix
        if len(user_input_list) == 16:
            four_x_four_matrix = [[], [], [], []]
            current_number = 1
            for number in user_input_list:
                if current_number <= 4:
                    four_x_four_matrix[0].append(number)
                    current_number += 1
                elif current_number <= 8:
                    four_x_four_matrix[1].append(number)
                    current_number += 1
                elif current_number <= 12:
                    four_x_four_matrix[2].append(number)
                    current_number += 1
                elif current_number <= 16:
                    four_x_four_matrix[3].append(number)
                    current_number += 1
            return four_x_four_matrix
        else:
            print "The amount of numbers must be 9 or 16"


