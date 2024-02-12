"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    flat_board = str(board)
    (countX, countO) = (flat_board.count(X), flat_board.count(O))
    if countO >= countX:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i,j) for j in range(3) for i in range(3) if board[i][j] == EMPTY]
    # actions = []
    # for (j,row) in enumerate(board):
    #     for (i,cell) in enumerate(row):
    #         if cell == None:
    #             actions.append((i,j))
    # return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If action is not a valid action for the board, your program should raise an exception.
    The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
    Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation.
        This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    """
    (i,j) = action
    assert 0 <= i <= 2 and 0 <= j <= 2, f"Invalid position {action}"
    assert board[i][j] == EMPTY, f"Position is not empty {action}"
    
    #clone the board to avoid modifying the original
    cloned_board = [row[:] for row in board]
    # make the next move, and return the result
    cloned_board[i][j] = player(board)
    return cloned_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
    If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    """
    win_positions = [[(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)], # horizontal
                     [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)], # vertical
                     [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]] # diagonal
    for symbol in (X,O):
        if symbol*3 in [''.join([board[p[0][0]][p[0][1]],board[p[1][0]][p[1][1]],board[p[2][0]][p[2][1]]]) for p in win_positions]:
            return symbol
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError