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

# recurively iterates through board
#finds an empty space, checks if there exists a valid input, if so set the input, else begin backtracking by reseting values
def solve(board):
    printBoard(board)
    print('')
    find = findEmpty(board)

    if not find:
        return True #board complete

    else:
         row, col = find
    
    for i in range(1,10):
        if checkValid(board, i, (row,col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    return False


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

#function that iterates over the board to find empty spaces
#input: 9x9 board matrix
#returns: (row, col) tuple of row x collumn
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i , j) 
    return None

#input: 
#  9x9 board matrix
#  num: input value
#  pos: tuple of (row, col)
#output:
#   False if there exists the same number in the row/column or in the 3x3 space, True if not
def checkValid(board, num, pos):
    #check row
    #iterate over the length of a row (9) (board[0] is just a base case)
    for i in range(len(board[0])):
        #if (row , i) == number and not the space we're inputing into
        #then false
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check 3x3 space
    #we'll have to use floor division to figure out what space we're in
    xBox = pos[1] // 3
    yBox = pos[0] // 3

    for i in range(yBox * 3, yBox * 3 + 3):
        for j in range(xBox * 3, xBox * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

# printBoard(board)
solve(board)

# printBoard(board)