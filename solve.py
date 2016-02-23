# solve_sudoku.py

import heapq
from copy import deepcopy
from itertools import starmap

from base import Sudoku
from helper import Constraints, Coords, PriorityInfo

class SolveSudoku(Sudoku):

    def __init__(self, sqrt_n, board):
        Sudoku.__init__(self, sqrt_n)
        self.board = board
        self.constraints = self.get_board_constraints()

    def get_board_constraints(self):
        """
        Traverse board for row, col, square constraints
        """

        rc = [set(range(1, self.n+1)) for x in range(self.n)]
        cc, sc = deepcopy(rc), deepcopy(rc)

        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):

                num = self.board[row_index][col_index]
                if num:
                    rc[row_index].remove(num)
                    cc[col_index].remove(num)
                    square_index = self.get_square_index(row_index, col_index)
                    sc[square_index].remove(num)

        return Constraints(rc, cc, sc)

    def solve_puzzle(self):
        """
        Fill in easiest blanks first (eliminate less choices for other unassigned var)
        """

        heap = self.sort_blanks_by_priority(self.get_blank_coords())
        self.recurse(deepcopy(heap), self.constraints)  # modifies self.board in place

    def recurse(self, heap, constraints):
        """
        Dfs and backtrack for solution.

        for item in heap: for choice in item constraints: copy constraints, remove choice, recurse

        self.board does not reflect current recursion state of board (constraints do)
        but will have final solution when constraints are empty
        """

        while heap:

            item = heapq.heappop(heap)
            coords = item.coords
            choices = list(constraints.row[coords.row]
            & constraints.col[coords.col]
            & constraints.square[coords.square])

            if not choices:
                # print('backtracking')
                return False

            for num in choices:

                self.board[item.coords.row][item.coords.col] = num

                cc = Constraints.copy(constraints)
                cc.row[coords.row].remove(num)
                cc.col[coords.col].remove(num)
                cc.square[coords.square].remove(num)

                #
                # print("heap", heap)
                # self.print_board()
                # print("constraints", cc)
                # print("\ncurrent", coords, "\nnext", next_coords, "\n")
                # import pdb; pdb.set_trace()

                result = self.recurse(deepcopy(heap), cc)  # recurse with new constraints
                if result:
                    return True

            return False

    def get_blank_priority(self, coords):
        """
        Assign cell priority based on lowest fellow blank cell count.
        Return PriorityInfo object for use in heap.
        """
        row_zero_count = sum(1 for zero in (filter(lambda x: x == 0, self.board[coords.row]) ))
        col_zero_count = sum(1 for zero in (filter(lambda x: x[ coords.col ] == 0, self.board) ))
        square_zero_count = 0
        s = self.square_num_to_coords(coords.square)
        for r in range(s[0], s[0] + self.sqrt_n-1):
            for c in range(s[1], s[1] + self.sqrt_n-1):
                try:
                    if self.board[r][c] == 0:
                        square_zero_count += 1
                except IndexError:
                    print("OMG INDEXERROR")
                    import pdb; pdb.set_trace()

        return PriorityInfo(coords, row_zero_count, col_zero_count, square_zero_count)

    def get_blank_coords(self):
        """
        Return list of blank cell coordinates in self.board
        """

        coords = [Coords(row=r, col=c, square=self.get_square_index(r, c))
        for c in range(self.n) for r in range(self.n) if self.board[r][c] == 0 ]

        # coords = starmap(lambda r, c: Coords(row=r, col=c, square=self.get_square_index(r, c)),
        # filter(lambda item: self.board[item[0]][item[1]] == 0,
        # ( (r, c) for c in range(self.n) for r in range(self.n) ) ) )
        return coords

    def sort_blanks_by_priority(self, coords):
        heap = []
        for c in list(coords):
            item = self.get_blank_priority(c)
            heapq.heappush(heap, item)
        return heap
