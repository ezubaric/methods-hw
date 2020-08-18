
import unittest

from word_count import word_count

class TestWordCount(unittest.TestCase):
    def test_count(self):
        count = word_count("toy.txt")
        self.assertTrue("asdf" not in count)
        self.assertEqual(count.get("coffers", 0), 1)
        self.assertEqual(count.get("And", 0), 5)
        self.assertEqual(count.get("honourable", 0), 5)                
        self.assertEqual(count.get("Caesar", 0), 4)
        self.assertEqual(count.get("Caesar,", 0), 2)                
        
if __name__ == '__main__':
    unittest.main()
