
#### sudoku maker and solver in python

use forward checking to enforce consistency of arcs pointing to new assignment and backtrack when domain is empty.

####files

helper.py: classes for nice shorthand
base.py: base sudoku class with helper functions
make.py: make a sudoku board
solve.py: solve a sudoku board
run.py: parse user input and make/solve board of chosen size

####terms

square: sqrt_n by sqrt_n section of nxn board

squares are zero indexed from upper left to bottom right

0 represents a blank cell

####run

    python3 run.py

example output:

    Enter sudoku size ("9" for 9x9 sudoku):
    9

    Puzzle:

    [8, 6, 7, 0, 0, 4, 0, 1, 9]
    [5, 3, 4, 7, 9, 0, 2, 6, 8]
    [0, 1, 2, 8, 6, 5, 0, 3, 4]
    [6, 0, 9, 1, 5, 0, 0, 4, 7]
    [2, 5, 0, 4, 3, 7, 8, 9, 6]
    [4, 7, 3, 6, 8, 9, 1, 5, 2]
    [1, 9, 6, 2, 7, 3, 4, 8, 5]
    [7, 4, 8, 5, 1, 6, 9, 2, 3]
    [3, 2, 5, 9, 4, 8, 6, 7, 1]

    Solved:

    [8, 6, 7, 3, 2, 4, 5, 1, 9]
    [5, 3, 4, 7, 9, 1, 2, 6, 8]
    [9, 1, 2, 8, 6, 5, 7, 3, 4]
    [6, 8, 9, 1, 5, 2, 3, 4, 7]
    [2, 5, 1, 4, 3, 7, 8, 9, 6]
    [4, 7, 3, 6, 8, 9, 1, 5, 2]
    [1, 9, 6, 2, 7, 3, 4, 8, 5]
    [7, 4, 8, 5, 1, 6, 9, 2, 3]
    [3, 2, 5, 9, 4, 8, 6, 7, 1]

    Valid solution!
