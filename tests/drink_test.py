import unittest
from src.drink import *

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Bacardi", 10.00)
        
    def test_drink_has_name(self):
        self.assertEqual("Bacardi", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(10.00, self.drink.price)
