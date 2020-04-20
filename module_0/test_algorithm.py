import unittest

from module_0.algorithm import steps_to_guess


class TestGuessSteps(unittest.TestCase):
    RANGE = (1, 127)
    MAX_STEPS = 7  # log2

    def test_max_steps(self):
        for secret in range(self.RANGE[0], self.RANGE[1] + 1):
            steps = steps_to_guess(secret, self.RANGE)
            self.assertGreaterEqual(self.MAX_STEPS, steps, "%d found by %d steps" % (secret, steps))

    def test_shortest_path(self):
        steps = steps_to_guess(64, self.RANGE)
        self.assertEqual(1, steps)

    def test_longest_path(self):
        steps = steps_to_guess(3, self.RANGE)
        self.assertEqual(self.MAX_STEPS, steps)
