import unittest
import random
from main import *


class TestPokerMethods(unittest.TestCase):

    def test_royal_flush(self):
        self.assertTrue(royal_flush([8, 9, 10, 11, 12], [1, 1, 1, 1]))
        self.assertFalse(royal_flush([8, 9, 10, 11, 12], [1, 1, 2, 1]))
        self.assertFalse(royal_flush([8, 9, 10, 11, 12], [1, 1, 1, 2]))

    def test_straight_flush(self):
        self.assertTrue(straight_flush([2, 3, 4, 5, 6], [1, 1, 1, 1]))
        self.assertFalse(straight_flush([2, 3, 4, 5, 7], [1, 1, 1, 1]))
        self.assertFalse(straight_flush([2, 3, 4, 5, 6], [1, 1, 2, 1]))

    def test_vierling(self):
        self.assertTrue(vierling([2, 2, 2, 2, 3]))
        self.assertTrue(vierling([2, 2, 3, 2, 2]))
        self.assertFalse(vierling([2, 3, 4, 5, 6]))

    def test_paar(self):
        self.assertTrue(paar([2, 3, 4, 4, 6]))  # Gültiges Paar
        self.assertFalse(paar([2, 3, 4, 5, 6]))

    def test_drilling(self):
        self.assertTrue(drilling([2, 2, 2, 3, 4]))  # Gültiger Drilling
        self.assertFalse(drilling([2, 3, 4, 5, 6]))

    def test_full_house(self):
        self.assertTrue(full_house([2, 2, 2, 3, 3]))  # Gültiges Full House
        self.assertFalse(full_house([2, 3, 4, 5, 6]))

    def test_flush(self):
        self.assertTrue(flush([1, 1, 1, 1]))  # Gültiger Flush
        self.assertFalse(flush([1, 1, 2, 1]))

    def test_strasse(self):
        self.assertTrue(strasse([2, 3, 4, 5, 6]))  # Gültige Straße
        self.assertFalse(strasse([2, 3, 4, 5]))

    def test_zwei_paare(self):
        self.assertTrue(zwei_paare([2, 2, 3, 3, 4]))  # Gültige Zwei Paare
        self.assertFalse(zwei_paare([2, 3, 4, 5, 6]))


if __name__ == '__main__':
    unittest.main()
