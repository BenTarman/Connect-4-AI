import unittest
from minimax import MiniMax

class TestStringMethods(unittest.TestCase):

    def test_obvious_win(self):
        #player 1 should go for the win here
        gameArr = [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 2, 0, 0, 0, 0, 0],
                    [1, 2, 0, 0, 0, 0, 0],
                    [1, 2, 0, 0, 0, 0, 0]
                  ]
        m = MiniMax(gameArr)
        best_move = m.bestMove(5, gameArr, 1)

        self.assertEqual(best_move, 0)

    def test_block(self):
        #palyer 2 should block player 1 here
        gameArr = [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 2, 0, 0, 0, 1, 0],
                    [0, 2, 2, 1, 0, 1, 0]
                  ]
        m = MiniMax(gameArr)
        best_move = m.bestMove(5, gameArr, 2)

        self.assertEqual(best_move, 5)

    def test_diagnol_win(self):
        # player 1 has win on diagnol
        gameArr = [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 2, 0, 0, 0],
                    [0, 1, 1, 2, 0, 0, 0],
                    [1, 2, 2, 2, 1, 0, 0]
                  ]
        m = MiniMax(gameArr)
        best_move = m.bestMove(5, gameArr, 1)

        self.assertEqual(best_move, 3)

    def test_diagnol_win(self):
        # player 2 has win on diagnol
        gameArr = [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 2, 1, 0, 0, 0],
                    [0, 1, 1, 2, 0, 0, 0],
                    [0, 2, 1, 2, 2, 0, 0],
                    [1, 2, 2, 2, 1, 0, 0]
                  ]
        m = MiniMax(gameArr)
        best_move = m.bestMove(5, gameArr, 2)

        self.assertEqual(best_move, 1)

    def test_game_end_full(self):
        # player 2 has win on diagnol
        gameArr = [
                    [1, 2, 1, 2, 1, 2, 1],
                    [2, 1, 2, 1, 2, 1, 2],
                    [1, 1, 2, 2, 1, 1, 2],
                    [2, 2, 1, 1, 1, 2, 2],
                    [2, 1, 1, 2, 2, 1, 1],
                    [1, 2, 2, 2, 2, 2, 2]
                  ]
        m = MiniMax(gameArr)
        best_move = m.bestMove(5, gameArr, 2)

        self.assertEqual(best_move, None)

    def test_game_end_win(self):
        gameArr = [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0],
                    [0, 1, 2, 1, 0, 0, 0],
                    [0, 1, 1, 2, 0, 0, 0],
                    [0, 2, 1, 2, 2, 0, 0],
                    [1, 2, 2, 2, 1, 0, 0]
                  ]

        m = MiniMax(gameArr)
        best_move = m.bestMove(5, gameArr, 2)

        self.assertEqual(best_move, None)




if __name__ == '__main__':
    unittest.main()
