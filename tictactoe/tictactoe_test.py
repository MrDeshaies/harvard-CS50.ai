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

        


if __name__ == '__main__':
    unittest.main()