import unittest
import frequent

class frequent_test(unittest.TestCase):


    def test_most_frequent(self):
        self.assertEqual(frequent.most_frequent([3, 3, 3, 2, 2, 2, 4, 4]), 3)


if __name__ == "__main__":
    unittest.main()