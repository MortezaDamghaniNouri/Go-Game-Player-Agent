
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



# This function gets the current board and the color of a player and tells him his best move for getting the most possible score out of opponent
def what_is_the_best_choice(input_current_board, input_previous_board, input_my_stone_color):
    all_empty_points = all_empty_points_finder(input_current_board)
    if len(all_empty_points) == 0:
        return [[all_empty_points, 0]]
    else:
        legal_points = suicide_points_remover(all_empty_points, input_my_stone_color, input_current_board)
        legal_points = KO_rule_applier(legal_points, input_current_board, input_previous_board, input_my_stone_color)
        if len(legal_points) == 0:
            return [[legal_points, 0]]
        else:
            points_and_their_scores = []
            if input_my_stone_color == 1:
                my_opponent_color = 2
            if input_my_stone_color == 2:
                my_opponent_color = 1
            i = 0
            while i < len(legal_points):
                current_point = legal_points[i]
                new_current_board = copy.deepcopy(input_current_board)
                new_current_board[current_point[0]][current_point[1]] = input_my_stone_color
                capturing_applier_output = capturing_applier(new_current_board, my_opponent_color)
                points_and_their_scores.append([current_point, capturing_applier_output[1]])
                i += 1

            maximum_score = points_and_their_scores[0][1]
            i = 1
            while i < len(points_and_their_scores):
                if points_and_their_scores[i][1] > maximum_score:
                    maximum_score = points_and_their_scores[i][1]
                i += 1

            best_final_choices = []
            i = 0
            while i < len(points_and_their_scores):
                if points_and_their_scores[i][1] == maximum_score:
                    best_final_choices.append(points_and_their_scores[i])
                i += 1

            return best_final_choices





# Minimax algorithm is implemented in this function and it returns the best choices and the scores of them
def minimax_algorithm_returning_scores(input_points_list, input_current_board, input_my_stone_color):
    points_and_utilities = []
    i = 0
    while i < len(input_points_list):
        current_point = input_points_list[i]
        copy_board = copy.deepcopy(input_current_board)
        copy_board[current_point[0]][current_point[1]] = input_my_stone_color
        if input_my_stone_color == 1:
            capturing_output = capturing_applier(copy_board, 2)
            my_opponent_color = 2
            new_current_board = capturing_output[0]
            my_capturing_point = capturing_output[1]

        if input_my_stone_color == 2:
            capturing_output = capturing_applier(copy_board, 1)
            my_opponent_color = 1
            new_current_board = capturing_output[0]
            my_capturing_point = capturing_output[1]

        # playing as the opponent
        empty_points_list = all_empty_points_finder(new_current_board)
        if len(empty_points_list) == 0:
            points_and_utilities.append([current_point, my_capturing_point])
        else:
            my_opponent_legal_choices = suicide_points_remover(empty_points_list, my_opponent_color, new_current_board)
            my_opponent_legal_choices = KO_rule_applier(my_opponent_legal_choices, new_current_board, copy_board, my_opponent_color)
            if len(my_opponent_legal_choices) == 0:
                points_and_utilities.append([current_point, my_capturing_point])
            else:
                my_opponent_points_and_utilities = []
                k = 0
                while k < len(my_opponent_legal_choices):
                    current_opponent_point = my_opponent_legal_choices[k]
                    new_copy_map = copy.deepcopy(new_current_board)
                    new_copy_map[current_opponent_point[0]][current_opponent_point[1]] = my_opponent_color
                    new_capturing_output = capturing_applier(new_copy_map, input_my_stone_color)
                    my_opponent_points_and_utilities.append([current_opponent_point, new_capturing_output[1]])
                    k += 1

                my_opponent_best_choices = []
                my_opponent_maximum_point = my_opponent_points_and_utilities[0][1]
                b = 1
                while b < len(my_opponent_points_and_utilities):
                    if my_opponent_points_and_utilities[b][1] > my_opponent_maximum_point:
                        my_opponent_maximum_point = my_opponent_points_and_utilities[b][1]
                    b += 1

                b = 0
                while b < len(my_opponent_points_and_utilities):
                    if my_opponent_points_and_utilities[b][1] == my_opponent_maximum_point:
                        my_opponent_best_choices.append(my_opponent_points_and_utilities[b])
                    b += 1

                my_opponent_final_choice = random_chooser(my_opponent_best_choices)
                points_and_utilities.append([current_point, (my_capturing_point - my_opponent_final_choice[1])])

        i += 1

    if len(input_points_list) == 0:
        return input_points_list
    else:
        my_maximum_point = points_and_utilities[0][1]
        b = 1
        while b < len(points_and_utilities):
            if points_and_utilities[b][1] > my_maximum_point:
                my_maximum_point = points_and_utilities[b][1]
            b += 1

        my_best_choices = []
        b = 0
        while b < len(points_and_utilities):
            if points_and_utilities[b][1] == my_maximum_point:
                my_best_choices.append(points_and_utilities[b])
            b += 1

    return my_best_choices




# A deepeer version of minimax algorithm is implemented in this function
def deeper_minimax_algorithm(input_points_list, input_current_board, input_my_stone_color):
    if input_my_stone_color == 1:
        my_opponent_color = 2
    if input_my_stone_color == 2:
        my_opponent_color = 1

    my_choices_and_their_points = []
    i = 0
    while i < len(input_points_list):
        current_point = input_points_list[i]
        previous_board = copy.deepcopy(input_current_board)
        new_current_board = copy.deepcopy(input_current_board)
        new_current_board[current_point[0]][current_point[1]] = input_my_stone_color
        capturing_applier_output = capturing_applier(new_current_board, my_opponent_color)
        new_current_board = capturing_applier_output[0]
        current_point_score = capturing_applier_output[1]

        what_is_the_best_choice_output = what_is_the_best_choice(new_current_board, previous_board, my_opponent_color)
        if len(what_is_the_best_choice_output[0][0]) == 0:
            my_choices_and_their_points.append([current_point, current_point_score])
        else:
            my_opponent_choice = random_chooser(what_is_the_best_choice_output)
            previous_board = copy.deepcopy(new_current_board)
            new_current_board = copy.deepcopy(new_current_board)
            new_current_board[my_opponent_choice[0][0]][my_opponent_choice[0][1]] = my_opponent_color
            capturing_applier_output = capturing_applier(new_current_board, input_my_stone_color)
            new_current_board = capturing_applier_output[0]
            current_point_score = current_point_score - capturing_applier_output[1]
            what_is_the_best_choice_output = what_is_the_best_choice(new_current_board, previous_board, input_my_stone_color)
            if len(what_is_the_best_choice_output[0][0]) == 0:
                my_choices_and_their_points.append([current_point, current_point_score])
            else:
                my_temp_choices = []
                a = 0
                while a < len(what_is_the_best_choice_output):
                    my_temp_choices.append(what_is_the_best_choice_output[a][0])
                    a += 1

                my_temp_choices = two_eyes_points_remover(my_temp_choices, input_my_stone_color, new_current_board)
                if len(my_temp_choices) == 0:
                    my_choices_and_their_points.append([current_point, current_point_score])
                else:
                    shallow_minimax_output = minimax_algorithm_returning_scores(my_temp_choices, new_current_board, input_my_stone_color)
                    a = 0
                    while a < len(shallow_minimax_output):
                        shallow_minimax_output[a][1] = current_point_score + shallow_minimax_output[a][1]
                        a += 1
                    my_maximum = shallow_minimax_output[0][1]
                    a = 1
                    while a < len(shallow_minimax_output):
                        if shallow_minimax_output[a][1] > my_maximum:
                            my_maximum = shallow_minimax_output[a][1]
                        a += 1
                    my_choices_and_their_points.append([current_point, my_maximum])

        i += 1

    maximum_point = my_choices_and_their_points[0][1]
    h = 1
    while h < len(my_choices_and_their_points):
        if my_choices_and_their_points[h][1] > maximum_point:
            maximum_point = my_choices_and_their_points[h][1]
        h += 1

    my_best_choices = []
    h = 0
    while h < len(my_choices_and_their_points):
        if my_choices_and_their_points[h][1] == maximum_point:
            my_best_choices.append(my_choices_and_their_points[h][0])
        h += 1

    return my_best_choices




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
            my_opponent_color = 2
            new_current_board = capturing_output[0]
            my_capturing_point = capturing_output[1]

        if input_my_stone_color == 2:
            capturing_output = capturing_applier(copy_board, 1)
            my_opponent_color = 1
            new_current_board = capturing_output[0]
            my_capturing_point = capturing_output[1]

        # playing as the opponent
        empty_points_list = all_empty_points_finder(new_current_board)
        if len(empty_points_list) == 0:
            points_and_utilities.append([current_point, my_capturing_point])
        else:
            my_opponent_legal_choices = suicide_points_remover(empty_points_list, my_opponent_color, new_current_board)
            my_opponent_legal_choices = KO_rule_applier(my_opponent_legal_choices, new_current_board, copy_board, my_opponent_color)
            if len(my_opponent_legal_choices) == 0:
                points_and_utilities.append([current_point, my_capturing_point])
            else:
                my_opponent_points_and_utilities = []
                k = 0
                while k < len(my_opponent_legal_choices):
                    current_opponent_point = my_opponent_legal_choices[k]
                    new_copy_map = copy.deepcopy(new_current_board)
                    new_copy_map[current_opponent_point[0]][current_opponent_point[1]] = my_opponent_color
                    new_capturing_output = capturing_applier(new_copy_map, input_my_stone_color)
                    my_opponent_points_and_utilities.append([current_opponent_point, new_capturing_output[1]])
                    k += 1

                my_opponent_best_choices = []
                my_opponent_maximum_point = my_opponent_points_and_utilities[0][1]
                b = 1
                while b < len(my_opponent_points_and_utilities):
                    if my_opponent_points_and_utilities[b][1] > my_opponent_maximum_point:
                        my_opponent_maximum_point = my_opponent_points_and_utilities[b][1]
                    b += 1

                b = 0
                while b < len(my_opponent_points_and_utilities):
                    if my_opponent_points_and_utilities[b][1] == my_opponent_maximum_point:
                        my_opponent_best_choices.append(my_opponent_points_and_utilities[b])
                    b += 1

                my_opponent_final_choice = random_chooser(my_opponent_best_choices)
                points_and_utilities.append([current_point, (my_capturing_point - my_opponent_final_choice[1])])

        i += 1

    if len(input_points_list) == 0:
        return input_points_list
    else:
        my_maximum_point = points_and_utilities[0][1]
        b = 1
        while b < len(points_and_utilities):
            if points_and_utilities[b][1] > my_maximum_point:
                my_maximum_point = points_and_utilities[b][1]
            b += 1

        my_best_choices = []
        b = 0
        while b < len(points_and_utilities):
            if points_and_utilities[b][1] == my_maximum_point:
                my_best_choices.append(points_and_utilities[b][0])
            b += 1

    return my_best_choices


# This function removes the two eyes of groups from the input list
def two_eyes_points_remover(input_list, input_my_stone_color, input_current_board):
    if len(input_list) == 0:
        return input_list
    output_list = copy.deepcopy(input_list)
    board_size = len(input_current_board[0])
    groups = groups_finder(input_current_board, input_my_stone_color)

    if len(groups) == 0:
        return input_list

    maximum_group_length = len(groups[0])
    p = 1
    while p < len(groups):
        if len(groups[p]) > maximum_group_length:
            maximum_group_length = len(groups[p])
        p += 1

    i = 0
    while i < len(groups):
        current_group = groups[i]
        if len(current_group) == maximum_group_length:
            j = 0
            empty_neighbors_of_the_group = []
            while j < len(current_group):
                current_member = current_group[j]
                m = current_member[0]
                n = current_member[1]
                if (m + 1) < board_size and input_current_board[m + 1][n] == 0 and [(m + 1), n] not in empty_neighbors_of_the_group:
                    empty_neighbors_of_the_group.append([(m + 1), n])

                if (m - 1) >= 0 and input_current_board[m - 1][n] == 0 and [(m - 1), n] not in empty_neighbors_of_the_group:
                    empty_neighbors_of_the_group.append([(m - 1), n])

                if (n + 1) < board_size and input_current_board[m][n + 1] == 0 and [m, (n + 1)] not in empty_neighbors_of_the_group:
                    empty_neighbors_of_the_group.append([m, (n + 1)])

                if (n - 1) >= 0 and input_current_board[m][n - 1] == 0 and [m, (n - 1)] not in empty_neighbors_of_the_group:
                    empty_neighbors_of_the_group.append([m, (n - 1)])

                j += 1

            if len(empty_neighbors_of_the_group) == 2:
                if empty_neighbors_of_the_group[0] in output_list:
                    copy_board = copy.deepcopy(input_current_board)
                    copy_board[empty_neighbors_of_the_group[0][0]][empty_neighbors_of_the_group[0][1]] = input_my_stone_color
                    if input_my_stone_color == 1:
                        my_opponent_color = 2
                    if input_my_stone_color == 2:
                        my_opponent_color = 1

                    capturing_applier_output = capturing_applier(copy_board, my_opponent_color)
                    my_groups_in_new_board = groups_finder(capturing_applier_output[0], input_my_stone_color)
                    new_current_board = capturing_applier_output[0]
                    new_maximum_group_length = len(my_groups_in_new_board[0])
                    p = 1
                    while p < len(my_groups_in_new_board):
                        if len(my_groups_in_new_board[p]) > new_maximum_group_length:
                            new_maximum_group_length = len(my_groups_in_new_board[p])
                        p += 1
                    a = 0
                    while a < len(my_groups_in_new_board):
                        current_group = my_groups_in_new_board[a]
                        if len(my_groups_in_new_board[a]) == new_maximum_group_length:
                            j = 0
                            new_empty_neighbors_of_the_group = []
                            while j < len(current_group):
                                current_member = current_group[j]
                                m = current_member[0]
                                n = current_member[1]
                                if (m + 1) < board_size and new_current_board[m + 1][n] == 0 and [(m + 1), n] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([(m + 1), n])

                                if (m - 1) >= 0 and new_current_board[m - 1][n] == 0 and [(m - 1), n] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([(m - 1), n])

                                if (n + 1) < board_size and new_current_board[m][n + 1] == 0 and [m, (n + 1)] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([m, (n + 1)])

                                if (n - 1) >= 0 and new_current_board[m][n - 1] == 0 and [m, (n - 1)] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([m, (n - 1)])

                                j += 1

                            if len(new_empty_neighbors_of_the_group) <= 1 and (empty_neighbors_of_the_group[0] in output_list):
                                output_list.remove(empty_neighbors_of_the_group[0])

                        a += 1


                if empty_neighbors_of_the_group[1] in output_list:
                    copy_board = copy.deepcopy(input_current_board)
                    copy_board[empty_neighbors_of_the_group[1][0]][empty_neighbors_of_the_group[1][1]] = input_my_stone_color
                    if input_my_stone_color == 1:
                        my_opponent_color = 2
                    if input_my_stone_color == 2:
                        my_opponent_color = 1

                    capturing_applier_output = capturing_applier(copy_board, my_opponent_color)
                    my_groups_in_new_board = groups_finder(capturing_applier_output[0], input_my_stone_color)
                    new_current_board = capturing_applier_output[0]
                    new_maximum_group_length = len(my_groups_in_new_board[0])
                    p = 1
                    while p < len(my_groups_in_new_board):
                        if len(my_groups_in_new_board[p]) > new_maximum_group_length:
                            new_maximum_group_length = len(my_groups_in_new_board[p])
                        p += 1
                    a = 0
                    while a < len(my_groups_in_new_board):
                        current_group = my_groups_in_new_board[a]
                        if len(my_groups_in_new_board[a]) == new_maximum_group_length:
                            j = 0
                            new_empty_neighbors_of_the_group = []
                            while j < len(current_group):
                                current_member = current_group[j]
                                m = current_member[0]
                                n = current_member[1]
                                if (m + 1) < board_size and new_current_board[m + 1][n] == 0 and [(m + 1), n] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([(m + 1), n])

                                if (m - 1) >= 0 and new_current_board[m - 1][n] == 0 and [(m - 1), n] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([(m - 1), n])

                                if (n + 1) < board_size and new_current_board[m][n + 1] == 0 and [m, (n + 1)] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([m, (n + 1)])

                                if (n - 1) >= 0 and new_current_board[m][n - 1] == 0 and [m, (n - 1)] not in new_empty_neighbors_of_the_group:
                                    new_empty_neighbors_of_the_group.append([m, (n - 1)])

                                j += 1

                            if len(new_empty_neighbors_of_the_group) <= 1 and (empty_neighbors_of_the_group[1] in output_list):
                                output_list.remove(empty_neighbors_of_the_group[1])

                        a += 1


        i += 1

    return output_list


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
            black_helper_file = open("black_helper.txt", "wt")
            black_helper_file.write("2\n")
            black_helper_file.close()
            return [2, 2]

        black_helper_file = open("black_helper.txt", "rt")
        line = black_helper_file.readline()
        step = int(line.rstrip())
        black_helper_file.close()
        black_helper_file = open("black_helper.txt", "wt")
        black_helper_file.write(str(step + 1) + "\n")
        black_helper_file.close()

        if step == 2 or step == 3:
            if input_current_board[1][2] == 0 or input_current_board[2][1] == 0 or input_current_board[2][3] == 0 or input_current_board[3][2] == 0:
                my_good_starting_choices = []
                if input_current_board[1][2] == 0:
                    my_good_starting_choices.append([1, 2])
                if input_current_board[2][1] == 0:
                    my_good_starting_choices.append([2, 1])
                if input_current_board[2][3] == 0:
                    my_good_starting_choices.append([2, 3])
                if input_current_board[3][2] == 0:
                    my_good_starting_choices.append([3, 2])
                my_good_starting_choices = suicide_points_remover(my_good_starting_choices, input_my_stone_color, input_current_board)
                my_good_starting_choices = KO_rule_applier(my_good_starting_choices, input_current_board, input_previous_board, input_my_stone_color)
                if len(my_good_starting_choices) != 0:
                    return random_chooser(my_good_starting_choices)

        all_empty_points = all_empty_points_finder(input_current_board)
        all_remaining_points = suicide_points_remover(all_empty_points, input_my_stone_color, input_current_board)
        all_remaining_points = KO_rule_applier(all_remaining_points, input_current_board, input_previous_board,
                                               input_my_stone_color)
        all_remaining_points = two_eyes_points_remover(all_remaining_points, input_my_stone_color,
                                                       input_current_board)
        all_remaining_points = minimax_algorithm(all_remaining_points, input_current_board, input_my_stone_color)
        if len(all_remaining_points) == 1:
            return all_remaining_points[0]
        else:
            if len(all_remaining_points) == 0:
                return "PASS"

            else:
                all_of_my_empty_neighbors = all_of_my_empty_neighbors_finder(input_my_stone_color,
                                                                             input_current_board)
                good_choices = []
                p = 0
                while p < len(all_remaining_points):
                    if all_remaining_points[p] in all_of_my_empty_neighbors:
                        good_choices.append(all_remaining_points[p])
                    p += 1

                if len(good_choices) == 0:
                    copy_of_remaining_points = copy.deepcopy(all_remaining_points)
                    if [0, 0] in all_remaining_points:
                        all_remaining_points.remove([0, 0])
                    if [0, 4] in all_remaining_points:
                        all_remaining_points.remove([0, 4])
                    if [4, 0] in all_remaining_points:
                        all_remaining_points.remove([4, 0])
                    if [4, 4] in all_remaining_points:
                        all_remaining_points.remove([4, 4])
                    if len(all_remaining_points) == 0:
                        return random_chooser(copy_of_remaining_points)
                    else:
                        return random_chooser(all_remaining_points)

                else:
                    good_choices_copy = copy.deepcopy(good_choices)
                    if [0, 0] in good_choices:
                        good_choices.remove([0, 0])
                    if [0, 4] in good_choices:
                        good_choices.remove([0, 4])
                    if [4, 0] in good_choices:
                        good_choices.remove([4, 0])
                    if [4, 4] in good_choices:
                        good_choices.remove([4, 4])

                    if len(good_choices) == 0:
                        return random_chooser(good_choices_copy)
                    else:
                        return random_chooser(good_choices)


    # playing as the white player
    if input_my_stone_color == 2:
        all_zero = True
        i = 0
        while i < board_size:
            j = 0
            while j < board_size:
                if input_previous_board[i][j] != 0:
                    all_zero = False
                    break
                j += 1
            if not all_zero:
                break
            i += 1

        if all_zero:
            # generating helper.txt
            helper_file = open("helper.txt", "wt")
            helper_file.write("2\n")
            helper_file.close()

            if input_current_board[2][2] == 0:
                return [2, 2]

            else:
                good_choices_for_start = []
                if input_current_board[1][2] == 0:
                    good_choices_for_start.append([1, 2])
                if input_current_board[2][3] == 0:
                    good_choices_for_start.append([2, 3])
                if input_current_board[2][1] == 0:
                    good_choices_for_start.append([2, 1])
                if input_current_board[3][2] == 0:
                    good_choices_for_start.append([3, 2])
                return random_chooser(good_choices_for_start)

        else:
            helper_file = open("helper.txt", "rt")
            line = helper_file.readline()
            step = int(line.rstrip())
            helper_file.close()

            if step == 2 or step == 3 or step == 4 or step == 5:
                if input_current_board[1][2] == 0 or input_current_board[2][1] == 0 or input_current_board[2][3] == 0 or input_current_board[3][2] == 0:
                    my_good_starting_choices = []
                    if input_current_board[1][2] == 0:
                        my_good_starting_choices.append([1, 2])
                    if input_current_board[2][1] == 0:
                        my_good_starting_choices.append([2, 1])
                    if input_current_board[2][3] == 0:
                        my_good_starting_choices.append([2, 3])
                    if input_current_board[3][2] == 0:
                        my_good_starting_choices.append([3, 2])
                    helper_file = open("helper.txt", "wt")
                    new_step = step + 1
                    helper_file.write(str(new_step) + "\n")
                    helper_file.close()
                    my_good_starting_choices = suicide_points_remover(my_good_starting_choices, input_my_stone_color, input_current_board)
                    my_good_starting_choices = KO_rule_applier(my_good_starting_choices, input_current_board, input_previous_board, input_my_stone_color)
                    if len(my_good_starting_choices) != 0:
                        return random_chooser(my_good_starting_choices)


            if step == 12:
                all_empty_points = all_empty_points_finder(input_current_board)
                all_legal_points = suicide_points_remover(all_empty_points, input_my_stone_color, input_current_board)
                all_legal_points = KO_rule_applier(all_legal_points, input_current_board, input_previous_board, input_my_stone_color)
                if len(all_legal_points) == 0:
                    return "PASS"
                else:
                    my_final_choices = []
                    r = 0
                    while r < len(all_legal_points):
                        current_point = all_legal_points[r]
                        copy_current_board = copy.deepcopy(input_current_board)
                        copy_current_board[current_point[0]][current_point[1]] = input_my_stone_color
                        capturing_output = capturing_applier(copy_current_board, 1)
                        my_final_choices.append([current_point, capturing_output[1]])
                        r += 1

                    maximum_point = my_final_choices[0][1]
                    r = 1
                    while r < len(my_final_choices):
                        if my_final_choices[r][1] > maximum_point:
                            maximum_point = my_final_choices[r][1]
                        r += 1

                    my_best_choices = []
                    r = 0
                    while r < len(my_final_choices):
                        if my_final_choices[r][1] == maximum_point:
                            my_best_choices.append(my_final_choices[r][0])
                        r += 1

                    return random_chooser(my_best_choices)

            else:
                helper_file = open("helper.txt", "wt")
                new_step = step + 1
                helper_file.write(str(new_step) + "\n")
                helper_file.close()

                all_empty_points = all_empty_points_finder(input_current_board)
                all_remaining_points = suicide_points_remover(all_empty_points, input_my_stone_color,
                                                              input_current_board)
                all_remaining_points = KO_rule_applier(all_remaining_points, input_current_board,
                                                       input_previous_board, input_my_stone_color)
                all_remaining_points = two_eyes_points_remover(all_remaining_points, input_my_stone_color,
                                                               input_current_board)
                all_remaining_points = minimax_algorithm(all_remaining_points, input_current_board,
                                                         input_my_stone_color)
                if len(all_remaining_points) == 1:
                    return all_remaining_points[0]
                else:
                    if len(all_remaining_points) == 0:
                        return "PASS"

                    else:
                        all_of_my_empty_neighbors = all_of_my_empty_neighbors_finder(input_my_stone_color,
                                                                                     input_current_board)
                        good_choices = []
                        p = 0
                        while p < len(all_remaining_points):
                            if all_remaining_points[p] in all_of_my_empty_neighbors:
                                good_choices.append(all_remaining_points[p])
                            p += 1

                        if len(good_choices) == 0:
                            copy_of_remaining_points = copy.deepcopy(all_remaining_points)
                            if [0, 0] in all_remaining_points:
                                all_remaining_points.remove([0, 0])
                            if [0, 4] in all_remaining_points:
                                all_remaining_points.remove([0, 4])
                            if [4, 0] in all_remaining_points:
                                all_remaining_points.remove([4, 0])
                            if [4, 4] in all_remaining_points:
                                all_remaining_points.remove([4, 4])
                            if len(all_remaining_points) == 0:
                                return random_chooser(copy_of_remaining_points)
                            else:
                                return random_chooser(all_remaining_points)

                        else:
                            good_choices_copy = copy.deepcopy(good_choices)
                            if [0, 0] in good_choices:
                                good_choices.remove([0, 0])
                            if [0, 4] in good_choices:
                                good_choices.remove([0, 4])
                            if [4, 0] in good_choices:
                                good_choices.remove([4, 0])
                            if [4, 4] in good_choices:
                                good_choices.remove([4, 4])

                            if len(good_choices) == 0:
                                return random_chooser(good_choices_copy)
                            else:
                                return random_chooser(good_choices)



# This function generates the output file
def output_file_generator(final_output):
    output_file = open("output.txt", "wt")
    if final_output == "PASS":
        output_file.write("PASS")
    else:
        output_file.write(str(final_output[0]) + "," + str(final_output[1]))
    output_file.close()

# This function generates the output file
def output_file_generator(final_output):
    pass


# This function calculates the points of white and black players
def points_calculator(input_board):
    board_size = len(input_board[0])
    black_counter = 0
    white_counter = 0
    i = 0
    while i < board_size:
        j = 0
        while j < board_size:
            if input_board[i][j] == 1:
                black_counter += 1
            if input_board[i][j] == 2:
                white_counter += 1
            j += 1
        i += 1
    return black_counter, white_counter


# The main part of the code starts here
my_stone_color, previous_board, current_board = input_file_reader()
board_size = len(current_board[0])
number_of_moves = 0
round_number = 1
while True:
    print("Round Number: " + str(round_number))
    # black player turn
    black_player_all_empty_points = all_empty_points_finder(current_board)
    all_legal_points = suicide_points_remover(black_player_all_empty_points, 1, current_board)
    all_legal_points = KO_rule_applier(all_legal_points, current_board, previous_board, 1)

    if len(all_legal_points) == 0:
        my_opponent_move = "PASS"
    else:
        all_zero = True
        r = 0
        while r < board_size:
            p = 0
            while p < board_size:
                if previous_board[r][p] != 0:
                    all_zero = False
                    break
                p += 1

            if not all_zero:
                break

            r += 1

        if all_zero:
            my_opponent_move = [2, 2]
        else:
            my_opponent_move = random_chooser(all_legal_points)

        previous_board = copy.deepcopy(current_board)
        current_board[my_opponent_move[0]][my_opponent_move[1]] = 1
        capturing_output = capturing_applier(current_board, 2)
        current_board = capturing_output[0]

    number_of_moves += 1


    # white player turn
    my_agent_move = go_game(my_stone_color, previous_board, current_board)
    number_of_moves += 1
    if my_agent_move != "PASS":
        all_empty_points = all_empty_points_finder(current_board)
        if my_agent_move not in all_empty_points:
            visualizer(current_board)
            print("My Agent Move: " + str(my_agent_move))
            print(str(my_stone_color) + " is the loser because of an occupied point.")
            break
        if len(suicide_points_remover([my_agent_move], my_stone_color, current_board)) == 0 or len(KO_rule_applier([my_agent_move], current_board, previous_board, my_stone_color)) == 0:
            visualizer(current_board)
            print("My Agent Move: " + str(my_agent_move))
            print(str(my_stone_color) + " is the loser because of KO or Suicide.")
            break
        previous_board = copy.deepcopy(current_board)
        current_board[my_agent_move[0]][my_agent_move[1]] = my_stone_color
        capturing_output = capturing_applier(current_board, 1)
        current_board = capturing_output[0]

    print("My Agent Move: " + str(my_agent_move))
    print("My Opponent Move: " + str(my_opponent_move))
    visualizer(current_board)




    if my_opponent_move == "PASS" and my_agent_move == "PASS":
        black_point, white_point = points_calculator(current_board)
        white_point = white_point + 2.5
        print("Black point: " + str(black_point))
        print("White point: " + str(white_point))
        if black_point == white_point:
            print("DRAW")
        if black_point > white_point:
            print("BLACK WON")
        if white_point > black_point:
            print("WHITE WON")
        break

    if number_of_moves >= 24:
        if number_of_moves == 24:
            print("The maximum number of moves is reached")
            black_point, white_point = points_calculator(current_board)
            white_point = white_point + 2.5
            print("Black point: " + str(black_point))
            print("White point: " + str(white_point))
            if black_point == white_point:
                print("DRAW")
            if black_point > white_point:
                print("BLACK WON")
            if white_point > black_point:
                print("WHITE WON")
        else:
            print("ERROR: The total number of moves is more than 24!")
        break


    print("================================================================================")
    round_number += 1





