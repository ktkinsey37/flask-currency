from unittest import TestCase
from app import app
from currency import build_conversion, validate_amount, validate_curr_symbol

class CurrencyConverterTestCase(TestCase):
    def test_homepage(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<label for="input-currrency"></label>Converting from:', html)

    def test_conversion_page(self):
        with app.test_client() as client:
            res = client.post('/convert', data={'input-currency': 'USD', 'output-currency': 'USD', 'input-amount': '1'})
            html = res.get_data(as_text=True)
            self.assertIn('US$ 1.0', html)
        
    def test_invalid_first_currency(self):
        with app.test_client() as client:
            res = client.post('/convert', data={"input-currency": "n/a", "output-currency": "USD", "input-amount": "1"})
            html = res.get_data(as_text=True)
            self.assertIn('Not a valid code: n/a', html)

    def test_invalid_second_currency(self):
        with app.test_client() as client:
            res = client.post('/convert', data={"input-currency": "USD", "output-currency": "n/a", "input-amount": "1"})
            html = res.get_data(as_text=True)
            self.assertIn('Not a valid code: n/a', html)

    def test_invalid_amount(self):
        with app.test_client() as client:
            res = client.post('/convert', data={"input-currency": "USD", "output-currency": "JPY", "input-amount": "cat"})
            html = res.get_data(as_text=True)
            self.assertIn('Not a valid int: cat', html)

    def test_invalid_amount_negative(self):
        with app.test_client() as client:
            res = client.post('/convert', data={"input-currency": "USD", "output-currency": "JPY", "input-amount": "-5"})
            html = res.get_data(as_text=True)
            self.assertIn('Not a valid, positive int: -5', html)