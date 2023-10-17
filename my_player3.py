
import random
import copy








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


# This function checks whether the input element is in the input groups or not
def is_in_groups(input_groups, input_element):
    i = 0
    while i < len(input_groups):
        current_group = input_groups[i]
        if input_element in current_group:
            return True
        i += 1
    return False








# This function finds all of the groups whose color is the same as the input group_color
def groups_finder(input_board, group_color):
    groups = []
    i = 0
    board_size = len(input_board[0])
    while i < board_size:
        j = 0
        while j < board_size:
            if input_board[i][j] == group_color and (not is_in_groups(groups, [i, j])):
                frontier = [[i, j]]
                expanded = []
                while True:
                    m = frontier[0][0]
                    n = frontier[0][1]
                    frontier.pop(0)

                    if (m + 1) < board_size and input_board[m + 1][n] == group_color and ([m + 1, n] not in frontier) and ([m + 1, n] not in expanded):
                        frontier.append([m + 1, n])

                    if (m - 1) >= 0 and input_board[m - 1][n] == group_color and ([m - 1, n] not in frontier) and ([m - 1, n] not in expanded):
                        frontier.append([m - 1, n])

                    if (n + 1) < board_size and input_board[m][n + 1] == group_color and ([m, n + 1] not in frontier) and ([m, n + 1] not in expanded):
                        frontier.append([m, n + 1])

                    if (n - 1) >= 0 and input_board[m][n - 1] == group_color and ([m, n - 1] not in frontier) and ([m, n - 1] not in expanded):
                        frontier.append([m, n - 1])

                    expanded.append([m, n])
                    if len(frontier) == 0:
                        break

                groups.append(expanded)
            j += 1
        i += 1

    return groups


# This function checks whether the input group of points has liberty or not.
def has_liberty(input_group, input_board):
    board_size = len(input_board[0])
    i = 0
    while i < len(input_group):
        m = input_group[i][0]
        n = input_group[i][1]
        if (m + 1) < board_size and input_board[m + 1][n] == 0:
            return True

        if (m - 1) >= 0 and input_board[m - 1][n] == 0:
            return True

        if (n + 1) < board_size and input_board[m][n + 1] == 0:
            return True

        if (n - 1) >= 0 and input_board[m][n - 1] == 0:
            return True
        i += 1
    return False


# This function applies capturing on the input board and it only considers the input color. It returns a new board and the number of removed stones of the input stone color.
def capturing_applier(input_board, input_stone_color):
    output = copy.deepcopy(input_board)
    if input_stone_color == 1:
        groups = groups_finder(input_board, 1)

    if input_stone_color == 2:
        groups = groups_finder(input_board, 2)

    counter = 0
    i = 0
    while i < len(groups):
        if not has_liberty(groups[i], input_board):
            j = 0
            while j < len(groups[i]):
                m = groups[i][j][0]
                n = groups[i][j][1]
                output[m][n] = 0
                counter += 1
                j += 1
        i += 1
    return [output, counter]


# This function visualizes the input board
def visualizer(input_board):
    board_size = len(input_board[0])
    k = 1
    first_line = ""
    while k <= board_size:
        first_line = first_line + "=== "
        k += 1
    print(first_line)
    i = 0
    while i < board_size:
        j = 0
        line = ""
        while j < board_size:
            if input_board[i][j] == 1:
                line = line + " X  "
            if input_board[i][j] == 2:
                line = line + " O  "
            if input_board[i][j] == 0:
                line = line + "    "
            j += 1
        print(line)
        k = 1
        line = ""
        while k <= board_size:
            line = line + "=== "
            k += 1
        print(line)
        i += 1


# This function removes the suicide points from the input list of points for the given color
def suicide_points_remover(input_list, input_stone_color, input_board):
    output_list = copy.deepcopy(input_list)
    i = 0
    while i < len(input_list):
        current_point = input_list[i]
        is_suicide_point = False
        board_copy = copy.deepcopy(input_board)
        board_copy[current_point[0]][current_point[1]] = input_stone_color
        if input_stone_color == 1:
            output = capturing_applier(board_copy, 2)
        if input_stone_color == 2:
            output = capturing_applier(board_copy, 1)

        new_board = output[0]
        groups = groups_finder(new_board, input_stone_color)
        j = 0
        while j < len(groups):
            current_group = groups[j]
            if not has_liberty(current_group, new_board):
                is_suicide_point = True
                suicide_point = [current_point[0], current_point[1]]
                break
            j += 1

        if is_suicide_point:
            output_list.remove(suicide_point)

        i += 1
    return output_list


# This function checks whether the two input boards are the same or not
def are_the_same_boards(first_input_board, second_input_board):
    board_size = len(first_input_board[0])
    i = 0
    while i < board_size:
        j = 0
        while j < board_size:
            if first_input_board[i][j] != second_input_board[i][j]:
                return False
            j += 1
        i += 1
    return True


# This function counts the number of the stones of the input color which are removed from the first input board
def how_many_captured(first_input_board, second_input_board, input_color):
    board_size = len(first_input_board[0])
    count_in_first_board = 0
    i = 0
    while i < board_size:
        j = 0
        while j < board_size:
            if first_input_board[i][j] == input_color:
                count_in_first_board += 1
            j += 1
        i += 1

    count_in_second_board = 0
    i = 0
    while i < board_size:
        j = 0
        while j < board_size:
            if second_input_board[i][j] == input_color:
                count_in_second_board += 1
            j += 1
        i += 1

    return count_in_first_board - count_in_second_board


# This function applies the KO rule on the elements of the input list and removes the elements which violate the KO rule
def KO_rule_applier(input_list, input_current_board, input_previous_board, input_my_stone_color):
    output_list = copy.deepcopy(input_list)
    i = 0
    while i < len(input_list):
        current_point = input_list[i]
        is_KO_violator = False
        count_of_captures = how_many_captured(input_previous_board, input_current_board, input_my_stone_color)
        if count_of_captures == 1:
            copy_board = copy.deepcopy(input_current_board)
            copy_board[current_point[0]][current_point[1]] = input_my_stone_color
            if input_my_stone_color == 1:
                new_board = capturing_applier(copy_board, 2)
            if input_my_stone_color == 2:
                new_board = capturing_applier(copy_board, 1)
            if are_the_same_boards(new_board[0], input_previous_board):
                is_KO_violator = True
        if is_KO_violator:
            violator_point = [current_point[0], current_point[1]]
            output_list.remove(violator_point)

        i += 1

    return output_list



# Minimax algorithm is implemented in this function
def minimax_algorithm(input_points_list, input_current_board, input_my_stone_color):
    points_and_utilities = []
    i = 0
    while i < len(input_points_list):
        current_point = input_points_list[i]
        copy_board = copy.deepcopy(input_current_board)
        copy_board[current_point[0]][current_point[1]] = input_my_stone_color
        if input_my_stone_color == 1:
            capturing_output = capturing_applier(copy_board, 2)
        if input_my_stone_color == 2:
            capturing_output = capturing_applier(copy_board, 1)

        # playing as the opponent














        i += 1























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


my_list = [[4, 0], [4, 1], [3, 2]]
print(KO_rule_applier(my_list, current_board, previous_board, 2))







exit()

output = go_game(my_stone_color, previous_board, current_board)
output_file_generator(output)





















