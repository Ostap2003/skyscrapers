"""
Skyskraper game
repo on github: https://github.com/Ostap2003/skyscrapers
"""

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    board = []
    with open(path, 'r', encoding='utf-8') as board_fl:
        for line in board_fl:
            board.append(line[:-1])

    return board


def left_to_right_check(input_line: str, pivot: int):
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
    >>> left_to_right_check('2 41325 1', 2))
    True
    """
    max_el_id = input_line.find(max(input_line[1:-1]))
    if max_el_id == 1:
        return 1 == pivot

    max_el_inside = max(input_line[1:max_el_id])
    max_el_inside_id = input_line[1:-1].find(max_el_inside) + 1
    
    visible = 0
    for el in range(len(input_line[1:max_el_id + 1])):
        if (input_line[el] <= max_el_inside) and (el <= max_el_inside_id):
            visible += 1
        elif (input_line[el] > max_el_inside) and (el > max_el_inside_id):
            visible += 1

    return pivot == visible


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        if '?' in line:
            return False

    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in range(1, len(board[:-1])):
        row_num_entry = set()
        for el in board[row][1:-1]:
            if el in row_num_entry:
                return False

            else:
                row_num_entry.add(el)

    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    pass


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

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
    for el in range(len(board)):
        try:
            if isinstance(int(board[0][el]), int):
                top_down = ''.join([board[row][el] for row in range(len(board))])
                # print('top-down = ', top_down)
                if left_to_right_check(top_down, int(top_down[0])):
                    pass
                else:
                    return False

        except ValueError:
            pass
    
    for el in range(len(board)):
        try:
            if isinstance(int(board[-1][el]), int):
                bottom_up = ''.join([board[row][el] for row in range(len(board))][::-1]) # reverse to pass to the left_to_right_check
                # print('bottom_up = ', bottom_up)
                if left_to_right_check(bottom_up, int(bottom_up[0])):
                    pass
                else:
                    return False

        except ValueError:
            pass

    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    pass


if __name__ == "__main__":
    # print(read_input('input.txt'))

    # print(left_to_right_check("452453*", 5))  # False
    # print(left_to_right_check("412453*", 4))  # True
    # print(left_to_right_check('2413251', 2))  # True

    # print(check_not_finished_board(['***21**', '412453*', '423145*', '*503215', '*35214*', '*41532*', '*2*1***']))

    # print(check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***']))


    # print(check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))  # True
    # print(check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***']))  # False
    # print(check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))  # False
