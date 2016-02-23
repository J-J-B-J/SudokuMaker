# run.py

from make import MakeSudoku
from solve import SolveSudoku
from math import sqrt
from enum import Enum

class Error(Enum):
    not_integer = 0
    not_perfect_square = 1
    not_greater_than_3 = 2

def print_help(e):
    if e == Error.not_integer:
        print("Input must be an integer.")
    elif e == Error.not_perfect_square:
        print("Input must be a perfect square.")
    elif e == Error.not_greater_than_3:
        print("Input must be 4 or greater.")
    return False

def valid_input(num):
    try:
        int_num = int(num)
        if int_num < 4:
            return print_help(Error.not_greater_than_3)
        if sqrt(int_num) % int(sqrt(int_num)) != 0:
            return print_help(Error.not_perfect_square)
        return True

    except:
        return print_help(Error.not_integer)

def main():
    print("\nEnter sudoku size (\"9\" for 9x9 sudoku): ")
    num = input()
    while not valid_input(num):
        num = input()

    num = int(sqrt(int(num)))
    puzzle = MakeSudoku(num).get_puzzle()
    s = SolveSudoku(num, puzzle)

    print("\nPuzzle:\n")
    s.print_board()
    s.solve_puzzle()

    print("Solved:\n")
    s.print_board()
    s.is_valid_board()

if __name__ == "__main__":
    main()
