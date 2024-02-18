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
        for p in win_positions:
            if symbol == board[p[0][0]][p[0][1]] and symbol == board[p[1][0]][p[1][1]] and symbol == board[p[2][0]][p[2][1]]:
                return symbol
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    Otherwise, the function should return False if the game is still in progress.
    """
    return winner(board) or not actions(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    """
    outcome = winner(board)
    if outcome == X:
        return 1
    elif outcome == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.
    """
    if terminal(board):
        return None
    current_player = player(board)

    result_action = None
    if current_player == X:
        value = -math.inf
        for action in actions(board):
            action_value = minimax_board_value(result(board, action), False)
            if action_value > value:
                value = action_value
                result_action = action
    else: #current_player is O
        value = math.inf
        for action in actions(board):
            action_value = minimax_board_value(result(board, action), True)
            if action_value < value:
                value = action_value
                result_action = action
    return result_action


def minimax_board_value(board, maximizing_player):
    if terminal(board):
        return utility(board)
    
    if maximizing_player:
        value = -math.inf
        for action in actions(board):
            value = max(value, minimax_board_value(result(board, action), False))
        return value
    else:
        value = math.inf
        for action in actions(board):
            value = min(value, minimax_board_value(result(board, action), True))
        return value
    
