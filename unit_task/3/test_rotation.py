import unittest
import rotation

class rotation_test(unittest.TestCase):
    

    def test_cyclic_rotation(self):
        self.assertEqual(rotation.cyclic_rotation('abcde', 2), 'deabc')
        self.assertEqual(rotation.cyclic_rotation('youarethebest', 0), 'youarethebest')
        self.assertEqual(rotation.cyclic_rotation('lószar', 3), 'zarlós')
        self.assertEqual(rotation.cyclic_rotation('felbasz', 4), 'baszfel')


if __name__ == "__main__":
    unittest.main()