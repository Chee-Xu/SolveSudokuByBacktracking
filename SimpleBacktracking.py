import time
"""
The following board is a very complex one and very targeted to backtracking method.
Simply because that many liitle tricks can force this algorithm to keep going back and back...
Therefore, it is not very efficient, we need to reduce the number of times that backtracks.
But, it is really useful for beginner for this alogrithm to understand the logic of it.

The author of this code is Tim, you can find his Youtube:
https://www.youtube.com/watch?v=eqUwSA0xI-s&t=396s
To see a better explaination..
"""
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
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
start_time = time.process_time()
your_solution = solve(board)
end_time = time.process_time()
print_board(board)
print("This sudoku took", end_time - start_time, "seconds to solve.\n")

