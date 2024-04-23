#!/usr/bin/python3
"""Module that finds all possible solutions the N queens puzzle.
Attributes:
    N (int): base number of queens, and length of board side in piece positions
    candidates: list of all successful
        solutions for given amount of columns checked
"""
from sys import argv


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column_gen(board=[]):
    """Adds a column of zeroes to the right of any board about to be tested for
    queen arrangements in that column.
    Returns:
        2D list
    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """Sets "queen," or 1, to coordinates given in board
    """
    board[row][col] = 1


def new_queen_safe(board, row, col):
    """For the board given, checks that for a new queen placed in the rightmost
    column, there are no other "queen"s, or 1 values, in the martix to the
    left, and diagonally up-left and down-left.
    Returns:
        True if no left side conflicts found for new queen, or False if a
    conflict exists.
    """
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # check left
            if board[x][y - i]:
                return False
            # check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(candidates):
    """Converts a board (matrix of 1 and 0) into a series of row/column
    indicies of each queen/1.
    """
    coord = []
    for x, attempt in enumerate(candidates):
        coord.append([])
        for i, row in enumerate(attempt):
            coord[x].append([])
            for j, col in enumerate(row):
                if col:
                    coord[x][i].append(i)
                    coord[x][i].append(j)
    return coord


# init candidates list with first column of 0s
candidates = []
candidates.append(board_column_gen())

# proceed column by column, testing the rightmost
for col in range(N):
    # start a new generation of the candidate list for every round of testing
    new_candidates = []
    # test each candidate from previous round, at current column
    for matrix in candidates:
        # for every row in that candidate's rightmost column
        for row in range(N):
            # are there any conflicts in placing a queen at those coordinates?
            if new_queen_safe(matrix, row, col):
                # no? then create a "child" (copy) of that candidate
                temp = [line[:] for line in matrix]
                # place a queen in that position
                add_queen(temp, row, col)
                # and unless you're in the last round of testing,
                if col < N - 1:
                    # add a new column of 0s on the right for the next round
                    board_column_gen(temp)
                # add that new candidate to this round's list of successes
                new_candidates.append(temp)
    # when finished with the round, discard the "parent" candidates
    candidates = new_candidates

# format results to match assignment output
for item in coordinate_format(candidates):
    print(item)
