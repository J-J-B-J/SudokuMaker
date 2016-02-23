# make.py

from base import Sudoku
from helper import Constraints, Coords

from random import randint
from copy import deepcopy


class MakeSudoku(Sudoku):

    def __init__(self, sqrt_n):
        Sudoku.__init__(self, sqrt_n)
        self.make_board()

    def make_board(self):
        """
        Initialize blank board.
        Create default constraints (all possible values for blank board).
        Recurse for solution.
        """

        self.board = [[0] * self.n for x in range(self.n)]
        row = [set(range(1, self.n+1)) for x in range(self.n)]
        col, square = deepcopy(row), deepcopy(row)

        constraints = Constraints(row, col, square)
        start = Coords(row=0, col=0, square=0)
        self.recurse(start, constraints)

    def recurse(self, coords, constraints):
        """
        Dfs and backtrack for solution.

        for choice in constraints: copy constraints, remove choice, recurse

        self.board does not reflect current recursion state of board (constraints do)
        but will have final solution when constraints are empty
        """

        if coords.row == self.n and coords.col == 0:
            return True

        choices = list(
        constraints.row[coords.row] &
        constraints.col[coords.col] &
        constraints.square[coords.square])

        if not choices: # backtrack
            return False

        while choices:

            num_assigned = choices.pop()
            self.board[coords.row][coords.col] = num_assigned

            cc = Constraints.copy(constraints)
            cc.row[coords.row].remove(num_assigned)
            cc.col[coords.col].remove(num_assigned)
            cc.square[coords.square].remove(num_assigned)

            next_coords = self.next_cell_coords(coords)
            result = self.recurse(next_coords, cc)

            if result:
                return True

        return False

    def get_puzzle(self):
        """
        Remove numbers from generated solution and return puzzle board.
        """

        print('solution')
        self.print_board()
        self.is_valid_board()
        b = deepcopy(self.board)
        nums = set()
        nums_to_remove = self.n + 1 # easy mode

        while len(nums) < nums_to_remove:
            num = randint(1, self.n**2)
            nums.add(num-1) if num not in nums else 0

        for num in nums:
            r, c = self.num_to_coords(num)
            b[r][c] = 0

        return b
