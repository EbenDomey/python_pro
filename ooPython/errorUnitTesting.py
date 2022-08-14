import unittest
import capLizer

class TestCapLizer(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        result= capLizer.cap_text(text)
        self.assertEqual(result, "Python")
    def test_words(self):
        text = "i love candy"
        result=capLizer.cap_text(text)
        self.assertEqual(result, "I Love Candy")
if __name__ == "__main__":
    unittest.main()