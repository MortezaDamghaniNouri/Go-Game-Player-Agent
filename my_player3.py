
import random









# This function reads the input text file
def input_file_reader():
    lines = []
    input_file = open("input.txt", "rt")
    while True:
        line = input_file.readline()
        if line == "":
            break
        lines.append(line.rstrip("\n"))
    input_file.close()
    input_my_stone_color = int(lines[0])
    input_previous_board = []
    input_current_board = []
    i = 1
    while i <= 5:
        temp = list(lines[i])
        new_temp = []
        j = 0
        while j < len(temp):
            new_temp.append(int(temp[j]))
            j += 1
        input_previous_board.append(new_temp)
        i += 1

    i = 6
    while i < len(lines):
        temp = list(lines[i])
        new_temp = []
        j = 0
        while j < len(temp):
            new_temp.append(int(temp[j]))
            j += 1
        input_current_board.append(new_temp)
        i += 1

    return input_my_stone_color, input_previous_board, input_current_board


# This function finds all of the empty squares around the stones of the input color
def all_of_my_empty_neighbors_finder(input_my_stone_color, input_current_board):
    output_list = []
    board_size = len(input_current_board[0])
    i = 0
    while i < board_size:
        j = 0
        while j < board_size:
            if input_current_board[i][j] == input_my_stone_color:
                if (i + 1) < board_size and input_current_board[i + 1][j] == 0 and ([i + 1, j] not in output_list):
                    output_list.append([i + 1, j])

                if (i - 1) >= 0 and input_current_board[i - 1][j] == 0 and ([i - 1, j] not in output_list):
                    output_list.append([i - 1, j])

                if (j + 1) < board_size and input_current_board[i][j + 1] == 0 and ([i, j + 1] not in output_list):
                    output_list.append([i, j + 1])

                if (j - 1) >= 0 and input_current_board[i][j - 1] == 0 and ([i, j - 1] not in output_list):
                    output_list.append([i, j - 1])

            j += 1
        i += 1

    return output_list


# This function finds all of the empty points on the board
def all_empty_points_finder(input_current_board):
    output_list = []
    board_size = len(input_current_board[0])
    i = 0
    while i < board_size:
        j = 0
        while j < board_size:
            if input_current_board[i][j] == 0:
                output_list.append([i, j])
            j += 1
        i += 1
    return output_list


# This function chooses one of the elements of the input list randomly and returns it
def random_chooser(input_list):
    random_number = random.randint(0, (len(input_list) - 1))
    return input_list[random_number]


# Go game is implemented in this function
def go_game(input_my_stone_color, input_previous_board, input_current_board):
    board_size = len(input_current_board[0])
    # playing as the black player
    if input_my_stone_color == 1:
        # checking whether it is the first move or not
        all_zero = True
        i = 0
        while i < board_size:
            j = 0
            while j < board_size:
                if input_current_board[i][j] != 0 or input_previous_board[i][j] != 0:
                    all_zero = False
                    break
                j += 1

            if not all_zero:
                break

            i += 1

        if all_zero:
            return [2, 2]

        all_of_my_empty_neighbors = all_of_my_empty_neighbors_finder(input_my_stone_color, input_current_board)
        if len(all_of_my_empty_neighbors) == 0:
            all_empty_points = all_empty_points_finder(input_current_board)
            all_legal_points = suicide_points_remover(all_empty_points)
            all_legal_points = KO_rule_applier(all_legal_points)
            all_legal_points = minimax_algorithm(all_legal_points)
            if len(all_legal_points) == 0:
                return "PASS"
            if len(all_legal_points) == 1:
                return all_legal_points[0]
            if len(all_legal_points) >= 2:
                return random_chooser(all_legal_points)










    # playing as the white player
    if input_my_stone_color == 2:
        pass






















# This function generates the output file
def output_file_generator(final_output):
    pass

























# The main part of the code starts here
my_stone_color, previous_board, current_board = input_file_reader()

print(random_chooser([[1, 3], [1, 1], [1, 2], [1, 8], [1, 0]]))
exit()

output = go_game(my_stone_color, previous_board, current_board)
output_file_generator(output)





















