from timeit import default_timer as timer


# known as the 'world's hardest sudoku'
# created by Finnish mathematician Arto Inkala
sudoku_grid = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 3, 6, 0, 0, 0, 0, 0], 
            [0, 7, 0, 0, 9, 0, 2, 0, 0], 
            [0, 5, 0, 0, 0, 7, 0, 0, 0], 
            [0, 0, 0, 0, 4, 5, 7, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0, 3, 0], 
            [0, 0, 1, 0, 0, 0, 0, 6, 8], 
            [0, 0, 8, 5, 0, 0, 0, 1, 0], 
            [0, 9, 0, 0, 0, 0, 4, 0, 0]
            ]

def printGrid(sudoku_grid):

    print('\n')

    for row in range(9):
        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - - - - -') # print horizontal lines every 3 rows
        
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print('| ', end="") # print vertical lines every 3 columns

            if col == 8:
                print(sudoku_grid[row][col]) # goes down to next row if it reaches the end of a row
            else:
                print(str(sudoku_grid[row][col]) + "  ", end="") 

    print('\n')


# finds empty cells to put numbers in
def findEmptyCell(sudoku_grid):

    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] == 0:
                return row, col
    return -1, -1

# checks if num is the right number to insert in empty cells
def checkValid(sudoku_grid, row, col, guess):

    # check the row  
    for i in range(9):
        if sudoku_grid[row][i] == guess:
            return False

    # check the column 
    for j in range(9):
        if sudoku_grid[j][col] == guess:
            return False

    # checks what box we're in
    # we divide by 3 to find the 3x3 block we're in e.g. block 2 starts at (0, 3)
    # 0 // 3 = 0 and 3 // 3 = 1. So we know we're in the second block on the first row which is at (0, 1)
    # we multiply by 3 to get to the index the box starts at 
    block_x, block_y = (row // 3) * 3, (col // 3) * 3

    # loop through each element of the 3x3 blocks
    for i in range(block_x, block_x + 3):
        for j in range(block_y, block_y + 3):
            if sudoku_grid[i][j] == guess:
                return False

    return True

def solveSudokuGrid(sudoku_grid):

    # retrieves empty cell coordinates 
    i, j = findEmptyCell(sudoku_grid)

    # i will be -1 if there are no empty squares left
    if i == -1:
        return True
    
    # tries each digit from 1 - 9 to see if its valid
    for num in range(1, 10):
        if checkValid(sudoku_grid, i, j, num):
            sudoku_grid[i][j] = num

            # recursively try to find the solution to every square
            if solveSudokuGrid(sudoku_grid): 
                return True
            
            # resets last-entered element to 0 if no number was valid
            # runs loop again on that element to find a valid solution
            sudoku_grid[i][j] = 0
    
    return False


printGrid(sudoku_grid)

start = timer()
solveSudokuGrid(sudoku_grid)
end = timer()

execution_time = round(end - start, 3)

printGrid(sudoku_grid)
print(f'Execution time: {execution_time}\n')
