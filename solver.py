#first make a sudoku board, its a 9x9 matrix. 0 represents a blank space
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
# print out the board, formatting. helps visualize it for the future

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - -')
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) +  ' ', end='')
            
# print_board(board)