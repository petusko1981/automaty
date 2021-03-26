import unittest
import gamble_rebuild as g

test_data = [
    {"input": g.Input(win=5, cwin=5, count=0), "risky_bet": 0, "risky_win": 0},  # jednoducha hra bez risky
    {"input": g.Input(win=5, cwin=0, count=1), "risky_bet": 5, "risky_win": 0},  # jedno risky prehrate
    {"input": g.Input(win=5, cwin=10, count=1), "risky_bet": 5, "risky_win": 10},  # jedno risky vyhrate
    {"input": g.Input(win=5, cwin=0, count=2), "risky_bet": 15, "risky_win": 10},  # dve risky prehrate
    {"input": g.Input(win=5, cwin=20, count=2), "risky_bet": 15, "risky_win": 30},  # dve risky vyhrate
    # tu dalsie vsetky verzie ake chces testovat
]

class DefaultTestGambleCase(unittest.TestCase):

    def test_gamble(self):

       # for pre vsetky data
       for data in test_data:
           # vyratat
           result = data["input"].calculate()

           self.assertEqual(result.tbet, data["risky_bet"])
           self.assertEqual(result.twin, data["risky_win"])


if __name__ == '__main__':
    unittest.main()