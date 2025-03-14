import unittest
from pacman import eat_ghost, score, lose, win


class TestPacman(unittest.TestCase):
    def test_eat_ghost_no_power_pellet(self):
        actual_result = eat_ghost(False, True)
        error_message = ('Called eat_ghost(False, True).'
                         f'The function returned {actual_result}, but the'
                         f'test expected that the '
                         'ghost **does not** get eaten because'
                         'no power pellet was active')
        self.assertIs(actual_result, False, msg=error_message)
    
    def test_eat_ghost_no_touching_ghost(self):
        actual_result = eat_ghost(True, False)
        error_message = ('Called eat_ghost(True, False).'
                         f'The function returned {actual_result} but the test'
                         'expected that the'
                         'ghost **does not** get eaten because'
                         'the player was not touching the ghost')
        self.assertIs(actual_result, False, msg=error_message)

    def test_eat_ghost_power_pellet_active_and_touching__ghost(self):
        actual_result = eat_ghost(True, True)
        error_message = ('Called eat_ghost(True, True).'
                         f'the function returned {actual_result}, but the'
                         'tests expected that the ghost gets eaten (True).')
        self.assertIs(actual_result, True, msg=error_message)

    def test_score_not_touching_power_pellet_and_touching_dot(self):
        actual_result = score(False, False)
        error_message = ('Called score(False, False)'
                         f'the function returned {actual_result} but the test'
                         'expected that the '
                         'player **does not** score because they'
                         'were not touchin anything')
        self.assertIs(actual_result, False, msg=error_message)

    def test_score_touching_power_pellet(self):
        actual_result = score(True, False)
        error_message = ('Called score(True, False).'
                         f'the function returned {actual_result} but the '
                         'test expected the the'
                         'player scores because they were touchinng the power pellet')
        self.assertIs(actual_result, True, msg=error_message)

    def test_score_touching_dot(self):
        actual_result = score(False, True)
        error_message = ('Called score(True, False).'
                         f'The function returned {actual_result} but the'
                         'test expected that the'
                         'player scores because they were touching a dot')
        self.assertIs(actual_result, True, msg=error_message)

    def test_lose_power_pellet_active(self):
        actual_result = lose(True, True)
        error_message = ('Called lose(True, True)'
                         f'the function returned {actual_result} but the '
                         'test expected that the'
                         'player **does not** lose because when they touched a '
                         'a power pellet is active')
        self.assertIs(actual_result, False, msg=error_message)

    def test_lose_no_touching_ghost(self):
        actual_result = lose(True, False)
        error_message = ('Called lose(True, False)'
                         f'the fuction returned {actual_result} but the '
                         'test expected that the'
                         'player **does not** lose because they are not touchig the ghost')
        self.assertIs(actual_result, False, msg=error_message)

    def test_lose_no_power_pellet_and_touching_ghost(self):
        actual_result = lose(False, True)
        error_message = ('Called lose(False, True).'
                         f'function returned {actual_result} that the '
                         f'tests expected that the '
                        'player loses because they touched a '
                        'ghost without a power pellet activated.')
        self.assertIs(actual_result, True, msg=error_message)
    
    def test_wins_touch_ghost(self):
        actual_result = win(True, False, True)
        error_message = ('Called win(True, False, True).'
                        f'The function returned {actual_result}, but the '
                        f'tests expected that the '
                        'player **does not** win, because '
                        'the player was touching a ghost.')

        self.assertIs(actual_result, False, msg=error_message)
    
    def test_wins_not_all_dots_eaten(self):
        actual_result = win(False, True, True)
        error_message = ('Called win(False, True, True).'
                        f'The function returned {actual_result}, but the '
                        f'tests expected that the player **does not** win, '
                        f'because the player did not eat all of the dots.')

        self.assertIs(actual_result, False, msg=error_message)

    def test_win_dots_eaten_and_power_pellet_active(self):
        actual_result = win(True, True, True)
        error_message = ('Called win(True, True, True).'
                        f'The function returned {actual_result}, but the '
                        f'tests expected that the player wins, '
                        f'because a power pellet was active when they '
                        f'touched a ghost.')

        self.assertIs(actual_result, True, msg=error_message)

    def test_win_all_dots_eaten(self):
        actual_result = win(True, False, False)
        error_message = ('Called win(True, False, False).'
                        f'The function returned {actual_result}, but the '
                        f'tests expected that the '
                        'player wins because all the dots were eaten.')

        self.assertIs(actual_result, True, msg=error_message)

if __name__ == "__main__":
    unittest.main()