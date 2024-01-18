from tictactoe import actions



def test_action():

    EMPTY = None
    board =  [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, "X", EMPTY]]
    print(actions(board))



test_action()