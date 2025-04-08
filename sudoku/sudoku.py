import streamlit as st
import numpy as np

def find_next_empty(puzzle):
    """Find the next empty cell (-1) in the puzzle."""
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    """Check if a guess is valid in the given row, column, and 3x3 grid."""
    if guess in puzzle[row]:  # Check row
        return False
    if guess in [puzzle[i][col] for i in range(9)]:  # Check column
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    """Solve the Sudoku puzzle using backtracking."""
    row, col = find_next_empty(puzzle)
    if row is None:  # If no empty space, puzzle is solved
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1  # Reset if not valid
    return False

def validate_sudoku_input(grid):
    """Validate the Sudoku input grid."""
    if len(grid) != 9:
        return "The puzzle must have exactly 9 rows."
    for i, row in enumerate(grid):
        if len(row) != 9:
            return f"Row {i+1} must contain exactly 9 numbers."
        for value in row:
            if not isinstance(value, int) or value < -1 or value > 9:
                return f"Invalid value '{value}' in row {i+1}. Allowed values: -1 to 9."
    return None

def main():
    st.title("Sudoku Solver")
    st.write("Enter your Sudoku puzzle below (-1 for empty spaces) and click 'Solve'.")

    default_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]

    grid = []
    for i in range(9):
        row_input = st.text_input(f"Row {i+1}", ",".join(map(str, default_board[i])))
        row_values = row_input.split(",")
        
        if len(row_values) != 9:
            st.error(f"Row {i+1} must contain exactly 9 numbers.")
            return
        
        try:
            row = [int(x) for x in row_values]
        except ValueError:
            st.error(f"Row {i+1} contains invalid characters. Please enter only numbers.")
            return

        grid.append(row)
    
    validation_error = validate_sudoku_input(grid)
    if validation_error:
        st.error(validation_error)
        return
    
    puzzle = np.array(grid, dtype=int)  # Ensure integer array
    puzzle_copy = puzzle.copy()  # Work on a copy to avoid modifying the original input

    if st.button("Solve"):
        try:
            if solve_sudoku(puzzle_copy):
                st.write("### Solved Sudoku")
                st.table(puzzle_copy)  # Display solved copy
            else:
                st.error("No solution exists for this Sudoku puzzle.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    st.write("\n---")
    st.write("Made by SABAHAT")

if __name__ == '__main__':
    main()
