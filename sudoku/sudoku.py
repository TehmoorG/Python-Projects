"""
Sudoku Solver using Backtracking.

This module provides functions to solve a Sudoku puzzle using the backtracking algorithm.
"""

def find_empty(board):
    """
    Find the first empty cell in the Sudoku board.
    
    Args:
    - board (list of list of int): The Sudoku board, represented as a 2D list.
    
    Returns:
    - tuple of int: Row and column indices of the first empty cell.
    - None: If there are no empty cells.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j
    return None

def check(board, row, column, number):
    """
    Check if it's valid to place a number in a given cell.
    
    Args:
    - board (list of list of int): The Sudoku board.
    - row (int): Row index of the cell.
    - column (int): Column index of the cell.
    - number (int): The number to check.
    
    Returns:
    - bool: True if it's valid to place the number, False otherwise.
    """
    # Check row and column for the same number
    for i in range(len(board)):
        if board[row][i] == number or board[i][column] == number:
            return False

    # Check the 3x3 grid the cell belongs to
    row_start = (row // 3) * 3
    col_start = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[row_start + i][col_start + j] == number:
                return False
    return True

def solve(board):
    """
    Solve the Sudoku board using backtracking.
    
    Args:
    - board (list of list of int): The Sudoku board.
    
    Returns:
    - bool: True if a solution is found, False otherwise.
    """
    # Check if the board has empty spaces
    empty_cell = find_empty(board)
    if not empty_cell:
        return True
    
    row, column = empty_cell
    for num in range(1, 10):
        if check(board, row, column, num):
            board[row][column] = num
            if solve(board):
                return True
            board[row][column] = 0
    return False

def print_board(board):
    """
    Print the Sudoku board in a formatted manner.
    
    Args:
    - board (list of list of int): The Sudoku board.
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def input_board():
    """
    Prompt the user to input each row of the Sudoku board.
    
    Returns:
    - list of list of int: The Sudoku board.
    """
    board = []
    print("Enter your Sudoku board. Use '0' for empty cells.")
    for i in range(9):
        while True:
            row = input(f"Enter row {i + 1} (e.g. 5 3 0 0 7 0 0 0 0): ").split()
            if len(row) == 9 and all(cell.isdigit() and 0 <= int(cell) <= 9 for cell in row):
                board.append(list(map(int, row)))
                break
            else:
                print("Invalid input. Please enter 9 numbers separated by spaces.")
    return board


if __name__ == "__main__":
    board = input_board()
    solve(board)
    print_board(board)