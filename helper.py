"""Classes for nice shorthand"""

from collections import namedtuple
from copy import deepcopy

Coords = namedtuple("Coords", "row col square")


class Constraints:
    """
    Possible values for all rows, columns, squares.
    Each member var is nxn array
    """

    def __init__(self, row_constraints, col_constraints, square_constraints):
        self.row = row_constraints
        self.col = col_constraints
        self.square = square_constraints

    def __str__(self):
        return str(self.row) + "\n" + str(self.col) + "\n" + str(self.square)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def copy(cls, other):
        """Create a copy of self"""
        return cls(deepcopy(other.row), deepcopy(other.col),
                   deepcopy(other.square))


class PriorityInfo:
    """
    Priority of blank cell.
    """

    def __init__(self, coords, row_count, col_count, square_count):
        self.coords = coords
        self.row_count = row_count  # number of zeros
        self.col_count = col_count
        self.square_count = square_count
        self.priority = min(row_count, col_count, square_count)

    def __str__(self):
        return str(self.coords)

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        return self.priority > other.priority
