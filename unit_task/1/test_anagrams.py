import unittest
import anagrams

class anagrams_test(unittest.TestCase):
    
    
    def test_is_anagram(self):
        self.assertEqual(anagrams.is_anagram("listen", "silent"), True)
        self.assertEqual(anagrams.is_anagram("aabcd", "dabac"), True)
        self.assertEqual(anagrams.is_anagram("cat", "dog"), False)
        self.assertEqual(anagrams.is_anagram(115, 115), False)
        self.assertEqual(anagrams.is_anagram("lol115", "lol115"), False)

if __name__ == '__main__':
    unittest.main()