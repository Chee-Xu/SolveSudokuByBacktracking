import time
# the key to improve the solving speed is going to make the solver to have least amount of backtrackings.
# for instance, start from the cell contains only one candidate.
board = [
    [0, 0, 2, 0, 6, 0, 0, 3, 0],
    [0, 5, 0, 0, 1, 0, 0, 0, 7],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 8, 0, 0, 0],
    [5, 0, 4, 1, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 9, 0, 0, 0, 2, 5, 0, 8],
    [0, 0, 0, 0, 5, 0, 0, 6, 0]
]


def solve(board):
    row, col = find_empty(board)
    if row is None:
        return True
    elif row == "False":
        return False

    ava_list = ava(board, row, col)  # find availiable numbers
    for i in ava_list:
        if valid(board, row, col, i):  # check availiable numbers
            board[row][col] = i  # insert

            if solve(board):  # backtracking
                return True
            else:
                board[row][col] = 0

    return False
def ava(board, row, col):
    result = []
    rows = list(board[row])
    rows.extend([board[i][col] for i in range(9)])

    box_row = row // 3 * 3
    box_col = col // 3 * 3
    rows.extend([board[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)])

    num = set(rows)
    for i in range(1, 10):
        if i not in num:
            result.append(i)
    return result

def valid(board, row, col, val):
    for i in board[row]:
        if i == val:
            return False
    for cols in board:
        if cols[col] == val:
            return False
    box_x = row // 3 * 3
    box_y = col // 3 * 3
    for r in range(box_x, box_x + 3):
        for c in range(box_y, box_y + 3):
            if board[r][c] == val:
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    row, col = None, None
    maxlength = 10
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                length = len(ava(board, i, j))
                if length == 1:   # find the cell that contains exactly one candidate
                    return i, j
                elif length == 0: # whether the board is valid or not
                    return "False", "False"
                elif length < maxlength: # otherwise, try the cell with minimum candidates
                    maxlength = length
                    row, col = i, j
    return row, col

start_time = time.process_time()
your_solution = solve(board)
end_time = time.process_time()
print_board(board)
print("This sudoku took", end_time - start_time, "seconds to solve.\n")
