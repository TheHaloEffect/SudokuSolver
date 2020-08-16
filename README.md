# Description
A Python program that solves sudoku problems with backtracking. It checks for empty cells and chooses numbers between 1 to 9 to see which one is valid. The program checks if the number is already in the row, column and box. If it isn't, it's valid. If a solution can't be found at that time, it backtracks and changes the number to 0 and tries again. 

Tried this out with what's known as the 'world's hardest sudoko', created by Finnish mathematician Arto Inkala. The solution by the program matches the one found online.

# Sudoku Rules
Sudoku is a logic-based number puzzle where you fill in numbers on a 9x9 grid. However, each number you fill in must not already be in the same row, column or 3x3 block.

<img src="https://www.sudokukingdom.com/images/rules1.jpg" alt="Sudoku Rules">

# Screenshots
<h3>'World's Hardest Sudoku'</h3>
<img src="https://preview.telegraph.co.uk/multimedia/archive/02260/Untitled-1_2260717b.jpg" alt="World's hardest sudoku">

<h3>Sudoku Solution</h3>
<img src="Screenshots/sudoku_solution.PNG" alt="Sudoku solution">

<h3>Checking Number Validity</h3>
<img src="Screenshots/check_valid.PNG" alt="Check valid code">
