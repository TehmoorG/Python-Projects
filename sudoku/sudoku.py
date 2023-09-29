import pprint

board = [
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

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i,j
    return None


def check(board,row,column,number):
    # check row and column for same number   
    for i in range(len(board)):
        if board[row][i] == number or board[i][column] == number:
            return False

    # check each 3x3 grid
    
    #checking which row + col the "grid" starts with
    row_start = (row//3) * 3
    col_start = (column//3) * 3

    for i in range(3):
        for j in range(3):
            if board[row_start + i][col_start + j] == number:
                return False
    return True

def solve(board):
    
    #make sure board has empty spaces
    if not find_empty(board):
        return True
    
    row, column = find_empty(board)
    for num in range(1,10):
        if check(board,row,column,num):
            board[row][column] = num
            if solve(board):
                return True
            board[row][column] = 0
    return False
solve(board)

new_board = pprint.PrettyPrinter(width=40, compact=True)
new_board.pprint(board)