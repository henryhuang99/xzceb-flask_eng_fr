import unittest
from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_en_to_fr1(self):
        self.assertEqual(english_to_french('Null'),'Null')
    def test_fr_to_en(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_fr_to_en1(self):
        self.assertEqual(french_to_english('Null'),'Null')
    

if __name__ == "__main__":
    unittest.main()