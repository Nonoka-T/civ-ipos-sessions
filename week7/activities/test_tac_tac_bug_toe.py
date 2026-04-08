import unittest
from tac_tac_bug_toe import is_win, tally_wins

class TestTacTacBugToe(unittest.TestCase):
    def test_is_win(self):
        """
        check if is_win() properly returns True
        """
        board_X = [['X', 'O', 'O'], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(is_win('X', board_X))

        board_O = [['X', 'O', 'O'], ['X', 'O', ' '], ['O', 'X', ' ']]
        self.assertTrue(is_win('O', board_O))

        board_none = [['X', 'O', 'O'], [' ', ' ', ' '], [' ', 'X', ' ']]
        self.assertFalse(is_win('X', board_none))
        self.assertFalse(is_win('O', board_none))

    def test_tally_wins(self):
        """
        check if tally_wins() properly returns True
        """
        result = [True, True, False, True, False]
        self.assertEqual(tally_wins(result), 3)

if __name__ == '__main__':
    unittest.main()
