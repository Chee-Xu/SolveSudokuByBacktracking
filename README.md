# SolveSudokuByBacktracking
In order to avoid try 1-9 at every single cell, I am going to make this algorithm to solve sudoku more like a human. For instance, starting from the cell with highest possible answer.

Sudoku solver:
The purpose of this programme is going to solve a 9*9 np.array board. 
The code should be able to identify whether the board is solvable or not.
	-if not, return -1 for each cell in the board
	-if yes, return the solution.

The basic ideas are:
	Step 1 : find the empty cell which is "0" in the board
	Step 2 : insert 1-9 into the empty cell
	Step 3 : whether step 2 is valid or not (check any duplicate number that displayed in the row, col and 3*3 box)
	Step 4 : use a backtracking algorithm to recurse step 1 to 4 until the board is solved or failed.

To reduce the number of times that backtracking:
   idea 1:
	-possible answer list : only try the numbers that are not shown in the same row, col and box.
   idea 2:
	-try the smallest length of idea 1 due to a higher chance to be correct.

In general, this could improve the backtracking algorithm significantly in the hard mode.
Simply because that idea 2 can greatly improve the accuracy.
