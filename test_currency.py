from unittest import TestCase
from app import app
from currency import build_conversion, validate_amount, validate_curr_symbol

class CurrencyOperationsTestCase(TestCase):
    def test_build_conversion(self):
        with app.test_client() as client:
            self.assertEqual(build_conversion("USD", "USD", 1), ('1.0', 'US$'))

    def test_validate_amount(self):
        with app.test_client() as client:
            self.assertEqual(validate_amount(5), True)                

    def test_validate_curr_symbol(self):
        with app.test_client() as client:
            self.assertIs(validate_curr_symbol('USD'), True)