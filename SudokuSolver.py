# puzzle taken from https://sudoku.com/hard/
sudoku = [
            [3, 6, 0, 9, 0, 4, 1, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 7, 0], 
            [0, 0, 4, 0, 0, 3, 0, 6, 0], 
            [9, 0, 5, 0, 1, 0, 8, 0, 7], 
            [0, 0, 0, 7, 5, 0, 0, 0, 9], 
            [0, 0, 0, 0, 0, 0, 0, 3, 0], 
            [7, 0, 0, 0, 0, 8, 0, 9, 0], 
            [0, 0, 3, 5, 4, 0, 0, 0, 8], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

def print_grid(sudoku):

    print('\n\n\n\n')

    for row in range(len(sudoku)):
        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - - - - -') # print horizontal lines every 3 rows
        
        for col in range(len(sudoku[row])):
            if col % 3 == 0 and col != 0:
                print('| ', end="") # print vertical lines every 3 columns

            if col == len(sudoku[row]) - 1:
                print(sudoku[row][col]) # goes down to next row if it reaches the end of a row
            else:
                print(str(sudoku[row][col]) + "  ", end="") 

    print('\n\n\n')


print_grid(sudoku)

# finds empty cells to put numbers in
def findEmptyCell(sudoku):

    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            if sudoku[row][col] == 0:
                return row, col
    return -1, -1

# checks if num is the right number to insert in empty cells
def checkValid(sudoku, row, col, guess):

    # check the row  
    for i in range(len(sudoku)):
        if sudoku[row][i] == guess:
            return False

    # check the column 
    for i in range(len(sudoku[i])):
        if sudoku[i][col] == guess:
            return False

    for subgridX