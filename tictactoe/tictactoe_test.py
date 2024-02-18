import unittest
from tictactoe import *

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        pass

    def test_player(self):
        b = initial_state()
        self.assertEqual(player(b), X)

        b[0][0]=X
        self.assertEqual(player(b), O)

        b[0][0]=O
        self.assertEqual(player(b), X)

        b = initial_state()
        b[0][1]=X
        self.assertEqual(player(b), O)
    
    def test_actions(self):
        b = initial_state()
        self.assertEqual(len(actions(b)), 9)
        b[0][0] = X
        self.assertEqual(len(actions(b)), 8)
        b[1][1] = O
        self.assertEqual(len(actions(b)), 7)

    def test_winner(self):
        b = initial_state()
        self.assertEqual(winner(b), None)
        b[0][0] = X
        b[1][0] = X
        self.assertEqual(winner(b), None)
        b[2][0] = X
        self.assertEqual(winner(b), X)
        b[0][0] = O
        b[1][0] = O
        self.assertEqual(winner(b), None)
        b[2][0] = O
        self.assertEqual(winner(b), O)
    
    def test_terminal(self):
        b = initial_state()
        # empty not terminal
        self.assertFalse(terminal(b))
        # x win is terminal
        b[0][0] = X
        b[1][0] = X
        self.assertFalse(terminal(b))
        b[2][0] = X
        self.assertTrue(terminal(b))
        
        #filled board tie also terminal
        b = [[X,O,X],
             [O,X,O],
             [O,X,O]]
        self.assertEqual(winner(b), None)
        self.assertTrue(terminal(b))
    
    def test_utility(self):
        self.assertEqual(utility(initial_state()), 0)
        # tie
        b = [[X,O,X],
             [O,X,O],
             [O,X,O]]
        self.assertEqual(winner(b), None)
        self.assertEqual(utility(b), 0)
        
        # X win
        b = [[X,X,X],
             [O,X,O],
             [O,X,O]]
        self.assertEqual(winner(b), X)
        self.assertEqual(utility(b), 1)
        
        # O win
        b = [[O,O,X],
             [O,X,O],
             [O,X,O]]
        self.assertEqual(winner(b), O)
        self.assertEqual(utility(b), -1)
    

    def test_minimax_board_value_terminal(self):
        #
        # X win
        b = [[X,X,X],
             [O,X,O],
             [O,X,O]]
        self.assertTrue(terminal(b))
        self.assertEqual(minimax_board_value(b, True), utility(b))
        self.assertEqual(minimax_board_value(b, False), utility(b))

        # O win
        b = [[O,O,X],
             [O,X,O],
             [O,X,O]]
        self.assertTrue(terminal(b))
        self.assertEqual(minimax_board_value(b, True), utility(b))
        self.assertEqual(minimax_board_value(b, False), utility(b))
    

    def test_minimax_board_value(self):
        # X about to win
        b = [[X,X,EMPTY],
             [O,O,X],
             [X,O,O]]
        self.assertEqual(minimax_board_value(b,True), 1)
        self.assertEqual(minimax_board_value(b,False), 1)

        # O about to win, but X can still win of next move of O is 3,3 (dumb)
        b = [[X,X,EMPTY],
             [X,O,O],
             [O,X,EMPTY]]
        self.assertEqual(minimax_board_value(b,True), 1)
        self.assertEqual(minimax_board_value(b,False), -1)
    
    def test_minimax(self):
        # X about to win
        b = [[X,X,EMPTY],
             [O,O,X],
             [X,O,O]]
        self.assertEqual(minimax(b), (0,2))

        # O about to win, but X can still win of next move of O is 3,3 (dumb)
        b = [[X,X,EMPTY],
             [X,O,O],
             [O,X,EMPTY]]
        self.assertEqual(minimax(b), (0,2))

        # X's turn, right move is again 0,2
        b = [[X,EMPTY,EMPTY],
             [O,EMPTY,EMPTY],
             [X,EMPTY,O]]
        self.assertEqual(minimax(b), (0,2))

        # same scenario as above, but rotated
        b = [[O,EMPTY,X],
             [EMPTY,EMPTY,O],
             [EMPTY,EMPTY,X]]
        self.assertEqual(minimax(b), (2,0))

        


if __name__ == '__main__':
    unittest.main()