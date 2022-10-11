import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_en_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_en_bye(self):
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")

    def test_fr_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_fr_au_revoir(self):
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")

    def test_en_null(self):
        self.assertIsNotNone(english_to_french)

    def test_fr_null(self):
        self.assertIsNotNone(french_to_english)

if __name__ == '__main__':
    unittest.main()