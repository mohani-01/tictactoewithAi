from tictactoe import actions, result, winner, terminal, minimax
# import pytest 

EMPTY = None
board =  [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board2 =  [["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X",  "X"]]

def main():
    # test_action()
    # test_result()
    # test_terminal()
    test_minimax()

def test_action():
    print(actions(board))

def test_result():

   print(result(board, (2,1)))



def test_minimax():
    print(minimax(board))

    




def test_winner():
    winingboard =  [["O", "O", EMPTY],
            [EMPTY, "O", EMPTY],
            [EMPTY, "X", "O"]]

    print(winner(board2))

def test_terminal():
    print(terminal(board))
    print(terminal(board2))

main()

