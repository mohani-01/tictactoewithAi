"""
Tic Tac Toe Player
"""
from util import Node
import math
from copy import copy

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
    """
    x_value = 0
    o_value = 0
    for row in board:
        for column in row:
            # print(column == X)
            if column == X:
                
                x_value += 1
            elif column == O:
                o_value += 1
   
    
    if x_value == 0 and o_value == 0:
        return "X"
    elif x_value > o_value:
        return "O"
    elif x_value == o_value:
        return "X"


    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i, row in enumerate(board) :
        for j, column in enumerate(row) :
            if column is None:
                available.add((i, j))
            
    return available
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i , j = action
    

    changeboard = copy(board)

    if changeboard[i][j] != None:
        raise ValueError("This play have already have a value") 
     
    changeboard[i][j] = player(changeboard)
    return changeboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wins = [[(0,0 ), (0, 1), (0, 2)], 
            [(1,0 ), (1, 1), (1, 2)], 
            [(2,0 ), (2, 1), (2, 2)], 
            [(0,0 ), (1, 0), (2, 0)], 
            [(0,1 ), (1, 1), (2, 1)], 
            [(0,2 ), (1, 2), (2, 2)],
            [(0,0 ), (1, 1), (2, 2)], 
            [(0, 2), (1,1 ), (2, 0)]]
        
    for win in wins:
        firstx, firsty = win[0]
        secondx, secondy = win[1]
        thirdx, thirdy = win[2]

        if board[firstx][firsty] == board[secondx][secondy] == board[thirdx][thirdy] and board[thirdx][thirdy] != EMPTY:
            print(board[firstx][firsty] == board[secondx][secondy] == board[thirdx][thirdy] and board[thirdx][thirdy] != EMPTY)
            return board[firstx][firsty]
    else:
        return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for rows in board:
        for column in rows:
            if column == EMPTY:
                return False

    return True
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    wins = winner(board)
    if  wins == "X":
        return 1
    elif wins == "O":
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # nNode(state=board, action=None, parent=None)
    if player(board) == "X":
        for action in actions(board): 
            # print(result(board, action), "HI")
            max_value(board)
    else:
        for action in actions(board):
            min_value(board)
    

    # raise NotImplementedError

def max_value(state):
    if terminal(state):
        # print(state)
        return utility(state)
    
    v = float('-inf')

    for action in actions(state):
        v = max(v, min_value(result(state, action)))
        # print(v)
        # print(state)

    return v


def min_value(state):
    if terminal(state):
        return utility(state)

    v = float("inf")
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
        # print()
        # print(v, "vvvvvv")
    return v



minimax(initial_state())