#series of tests for TicTacToe Board
import unittest
import board as b
import numpy as np
import minimax as ai


class TestTTT (unittest.TestCase):

    def test_winner(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[0,2] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1

        self.assertEqual(1, game.findWinner())  
    

    def test_game_over(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[0,2] = 1
        game.board[1,0] = 1
        game.board[1,1] = 1
        game.board[1,2] = -1
        game.board[2,0] = -1
        game.board[2,1] = -1
        game.board[2,2] = -1

        self.assertEqual(0, game.findWinner()) 
        self.assertEqual(True, game.isGameOver())      


    def test_game_over(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[0,2] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1

        self.assertEqual(True, game.isGameOver())           

    def test_User_Move_Choice(self):
        game = b.Board()
        for row in range(0,3):
            for col in range(0,3):
                test_a = game.copyThenPerformMove(row, col, 1)
                #print(test_a.board)

                test_b = game.copyThenPerformMove(row, col, 1)
                print(test_b.board)
                #print("Row: %s" % row)
                #print("col: %s" % col)
                
                self.assertEqual(np.array_equal(test_a.board, test_b.board), True)
       
    def test_whose_move(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[2,0] = -1
        self.assertEqual(game.whoseMove(), -1)
        print(game.whoseMove())
        game.board[2,1] = -1
        self.assertEqual(game.whoseMove(), 1)


    def test_second_move(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[0,2] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1

        print(game.whoseMove())
        top_move, score, count = ai.Optimal_Game_Strategy(game, 0)
        print(top_move)
        print(score)
        print(count)

        self.assertEqual(score, 1)

    def test_check_Win(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[0,2] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1

        self.assertEqual(game.findWinner(), 1)
        self.assertEqual(game.isGameOver(), True)


    def test_first_move(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1
        print(game.whoseMove())
        top_move, _, count = ai.Optimal_Game_Strategy(game, 0)
        print(top_move)
        print(_)
        print(count)

        self.assertEqual(top_move, (0,2)) 

         

if __name__ == '__main__':
    unittest.main()





