"""
Skyskraper game
repo on github: https://github.com/Ostap2003/skyscrapers
"""

def read_input(path: str) -> list:
    """
    Read game board file from path.
    Return list of str.

    """
    board = []
    with open(path, 'r', encoding='utf-8') as board_fl:
        for line in board_fl:
            if '\n' in line:
                board.append(line[:-1])
            else:
                board.append(line)

    return board


def left_to_right_check(input_line: str, pivot: int, depth=0) -> bool:
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    >>> left_to_right_check('423145*', 4)
    True
    """
    if len(input_line) == 0:
        return 0
    elif depth == 0:
        max_el = max(input_line[1:-1])
        # add 1 so indexing doesn't get affected by slicing
        max_el_id = input_line[1:-1].find(max_el) + 1
        return len(max_el) + left_to_right_check(input_line[1:max_el_id], pivot, depth+1) == pivot
    else:
        max_el = max(input_line)
        max_el_id = input_line.find(max_el)

    return len(max_el) + left_to_right_check(input_line[:max_el_id], pivot, depth+1)


def check_not_finished_board(board: list) -> bool:
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*',\
         '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    """
    for line in board:
        if '?' in line:
            return False

    return True


def check_uniqueness_in_rows(board: list) -> bool:
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    """
    for row in range(1, len(board[:-1])):
        row_num_entry = set()
        for elem in board[row][1:-1]:
            if elem in row_num_entry:
                return False

            else:
                row_num_entry.add(elem)

    return True


def check_horizontal_visibility(board: list) -> bool:
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', \
        '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', \
        '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', \
        '*41532*', '*2*1***'])
    False
    """
    for row in range(1, len(board[:-1])):
        try:
            if not left_to_right_check(board[row], int(board[row][0])):
                return False
        except ValueError:
            pass

        try:
            if not left_to_right_check(board[row][::-1], int(board[row][-1])):
                return False
        except ValueError:
            pass

    return True


def check_columns(board: list) -> bool:
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    # check uniqueness
    for row in range(1, len(board[:-1])):
        col_num_entry = set()
        for col in range(1, len(board[:-1])):
            if int(board[col][row]) in col_num_entry:
                return False
            else:
                col_num_entry.add(int(board[col][row]))

    # check visibility
    for elem in range(len(board)):
        # check top-down
        try:
            top_down = ''.join([board[row][elem] for row in range(len(board))])
            if left_to_right_check(top_down, int(top_down[0])):
                pass
            else:
                return False

        except ValueError:
            pass

        # check bottom-up
        try:
            bottom_up = ''.join([board[row][elem] for row in range(len(board))][::-1])
            if left_to_right_check(bottom_up, int(bottom_up[0])):
                pass
            else:
                return False

        except ValueError:
            pass

    return True


def check_skyscrapers(input_path: str) -> bool:
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    """
    board = read_input(input_path)
    if check_not_finished_board(board):
        if check_uniqueness_in_rows(board):
            if check_horizontal_visibility(board):
                if check_columns(board):
                    return True

    return False
