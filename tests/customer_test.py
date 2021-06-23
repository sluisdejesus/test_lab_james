import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 100.00)

    def test_has_customer_name(self):
        self.assertEqual("John", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)

    def test_custumer_buys_drink(self):
        drink = self.drink.Drink("Bacardi", 10.00)
        self.buy_drink(drink)
        self.assertEqual(90.00,self.buy_drink())
        