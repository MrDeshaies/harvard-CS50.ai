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
        [0][0] = O
        b[1][0] = O
        self.assertEqual(winner(b), None)
        b[2][0] = O
        self.assertEqual(winner(b), O)


if __name__ == '__main__':
    unittest.main()