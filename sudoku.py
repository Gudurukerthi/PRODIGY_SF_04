
# Function to print the solved Sudoku grid
def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

# Function to check if a number is valid in a specific position
def is_valid(grid, row, col, num):
    # Check the row
    if num in grid[row]:
        return False

    # Check the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check the 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    if num in [grid[box_row + i][box_col + j] for i in range(3) for j in range(3)]:
        return False

    return True

# Recursive function to solve the Sudoku puzzle
def solve_sudoku(grid):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # Try all possible numbers
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        # Recursively solve the remaining cells
                        if solve_sudoku(grid):
                            return True

                        # If the current number doesn't lead to a solution, backtrack
                        grid[row][col] = 0

                # If no number works, the puzzle is unsolvable
                return False

    # If all cells are filled, the puzzle is solved
    return True

# Example usage
unsolved_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(unsolved_grid):
    print("Solved Sudoku:")
    print_grid(unsolved_grid)
else:
    print("No solution exists for the given Sudoku puzzle.")
