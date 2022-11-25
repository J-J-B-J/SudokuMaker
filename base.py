"""Base sudoku class with helper functions"""

import heapq
from math import sqrt
from helper import Coords


class Sudoku:
    """A sudoku"""
    def __init__(self, sqrt_n):
        self.sqrt_n = sqrt_n
        self.n = sqrt_n ** 2
        self.board = []

    def is_valid_board(self):
        """
        Valid solution has different coordinates for occurrence of same number.
        Check for duplicate coordinates (row or col).
        Return bool.
        """
        d = {x: [set([]), set([])] for x in range(1, self.n + 1)}
        for row_index in range(self.n):
            for col_index in range(self.n):
                num = self.board[row_index][col_index]
                try:
                    if row_index in d[num][0] or col_index in d[num][1]:
                        print("Invalid solution.")
                        return
                except KeyError:
                    print("Unsolved solution.")  # d[0]
                    return

                d[num][0].add(row_index)
                d[num][1].add(col_index)
        print("Valid solution!")

    def num_to_coords(self, num):
        """Converts a number to a coordinate"""
        row_index = num // self.n
        col_index = num % self.n
        return int(row_index), int(col_index)

    def square_num_to_coords(self, num):
        """Converts a number to a coordinate"""
        index = (num // self.sqrt_n) * self.sqrt_n
        return int(index), int(index)

    def next_cell_coords(self, coords):
        """Returns the next cell's coordinates"""
        if coords.col == self.n - 1:  # last col. reset to next row
            return Coords(coords.row + 1, 0,
                          self.get_square_index(coords.row + 1, 0))
        return Coords(coords.row, coords.col + 1,
                      self.get_square_index(coords.row, coords.col + 1))

    def get_square_index(self, row, col):
        """Returns the square index of a cell"""
        sqrt_n = self.sqrt_n
        result = int(((row // sqrt_n) * sqrt_n) + (col // sqrt_n))
        return result

    def get_square_starting_coords(self, square_index):
        """Returns the starting coordinates of a square"""
        row = (square_index // self.sqrt_n) * self.sqrt_n
        col = (square_index % self.sqrt_n) * self.sqrt_n
        return row, col

    def print_board(self):
        """Prints the board"""
        for row in self.board:
            print(row)
        print("")
