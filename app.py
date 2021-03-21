from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from currency import build_conversion, validate_amount, validate_curr_symbol

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a'

c = CurrencyRates()
cc= CurrencyCodes()


@app.route('/')
def homepage():
    # Renders the home page
    return render_template('home.html')

@app.route('/convert')
def convert():
    # Converts the input currency and amount and returns a page with the output currency amount
    # Gathers arguments
    input_curr, output_curr, amount= request.args.get("input-currency"), request.args.get("output-currency"), request.args.get("input-amount")
    
    # Validates arguments
    if not validate_curr_symbol(input_curr) or not validate_curr_symbol(output_curr) or not validate_amount(amount):
        return render_template('home.html')

    # Gets converted amount and the currency symbol
    conversion, symbol = build_conversion(input_curr, output_curr, amount)

    # Returns a response
    return render_template('result.html', conversion=conversion, symbol=symbol)