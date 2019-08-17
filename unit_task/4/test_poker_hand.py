import unittest
import poker_hand

class poker_hand_test(unittest.TestCase):


    def test_poker_hand(self):
        self.assertEqual(poker_hand.hand_score([1, 1, 1, 1, 1]), "five")
        self.assertEqual(poker_hand.hand_score([1, 1, 1, 1, 2]), "four")
        self.assertEqual(poker_hand.hand_score([1, 1, 1, 2, 3]), "three")
        self.assertEqual(poker_hand.hand_score([1, 1, 4, 2, 3]), "pair")
        self.assertEqual(poker_hand.hand_score([1, 1, 2, 2, 3]), "twopair")
        self.assertEqual(poker_hand.hand_score([1, 1, 1, 2, 2]), "fullhouse")
        self.assertEqual(poker_hand.hand_score([1, 3, 2, 5, 4]), "nothing")


if __name__ == "__main__":
    unittest.main()