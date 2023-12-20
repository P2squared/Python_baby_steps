def next_location(puzzle): # Find next row & column that's not filled yet
    # Return row,col tuple for co-ordinate

    for r in range(9): # move across board till we find the next unsolved location
        for c in range(9): # indices are from 0 to 8 (<9)
            if puzzle[r][c] == -1:
                return r,c

    return None, None # If every location is filled, return empty

def is_correct(puzzle, guess, row, col):
    # Finds out if guess made at location is correct
    # Return True if guess is correct

    row_vals = puzzle[row] # Get digits in that row
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)] # Get digits in that column
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3): # Get digits in the smaller box
        for c in range(col_start, col_start+3):
            if guess == puzzle[r][c]:
                return False

    return True # Return true if guess is not in that column or row or box

def solve_sudoku(puzzle): # returns whether a solution exists
    # Step1 : Choose a location on the board to make a guess
    row, col = next_location(puzzle)

    if row is None: # If every location is already filled,
        return True

    # Step 2 : Make a guess at that location
    for guess in range(1,10): # cannot be 0, thus define range explicitly
    # Step 3 : Check if that guess is correct
        if is_correct(puzzle, guess, row, col):
            # Step 4 : If valid, add guess to unsolved puzzle
            puzzle[row][col] = guess

            if solve_sudoku(puzzle): # recursion with modified puzzle here we go
                return True # Guess was correct if every location is filled
    # Step 3b : If guess isn't correct, delete guess
        puzzle[row][col] = -1 # If guess isn't correct, reset board & guess again

    return False # If every location cannot be filled, sudoku cannot be solved



if __name__ == '__main__':
    test_board = [
        [-1, 8, 3,  5, 9,-1,  7,-1,-1],
        [-1,-1,-1,  7,-1,-1, -1,-1, 2],
        [-1,-1, 1, -1,-1,-1, -1,-1,-1],
        [-1, 5, 8, -1,-1, 3, -1,-1, 6],
        [ 1,-1,-1, -1,-1,-1,  8,-1,-1],
        [ 2,-1,-1, -1, 5,-1, -1,-1,-1],
        [-1, 9, 7, -1, 3,-1,  2,-1,-1],
        [ 5,-1,-1, -1,-1,-1, -1,-1,-1],
        [-1,-1,-1, -1,-1, 6, -1, 4,-1]
    ]

    print(solve_sudoku(test_board)) # Is the board solvable ?
    print(test_board) # What is the solution