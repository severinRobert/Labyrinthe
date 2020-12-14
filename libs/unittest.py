from rang import *
import unittest

class FracTestCase(unittest.TestCase):
    def test_init(self):
        """Test du __init__"""
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)

    def test_fraction_type(self):
        """Vérification du numerateur et denominateur de la fraction"""
        self.assertEqual(Fraction(88, 16).denominator, 16)
        self.assertEqual(Fraction(88, 16).numerator, 88)

    def test_str(self):
        """Vérification de la méthode __str__"""
        self.assertEqual(Fraction(88, 16).__str__(), "11/2")
        self.assertEqual(Fraction(-88, 16).__str__(), "-11/2")
        self.assertEqual(Fraction(0, 2).__str__(), "0/1")

    def test_mixed(self):
        """Vérification mixed number"""
        self.assertEqual(Fraction(88, 16).as_mixed_number(), "mixed = 5 1/2")
        self.assertEqual(Fraction(0, 2).as_mixed_number(), "mixed = 0")
        self.assertEqual(Fraction(47, 13).as_mixed_number(), "mixed = 3 8/13")