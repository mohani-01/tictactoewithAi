from tictactoe import actions, result, winner, terminal


EMPTY = None
board =  [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, "X", EMPTY]]

board2 =  [["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X",  "X"]]

def test_action():

    
    print(actions(board))

def test_result():

   print(result(board, (2,1)))
    




def test_winner():
    winingboard =  [["O", "O", EMPTY],
            [EMPTY, "O", EMPTY],
            [EMPTY, "X", "O"]]

    print(winner(board2))

def test_terminal():
    print(terminal(board))
    print(terminal(board2))

test_terminal()

test_winner()