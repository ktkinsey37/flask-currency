from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
cc= CurrencyCodes()

def build_conversion(input_curr, output_curr, amount):
    # Takes validated inputs and creates conversion and symbol
    rate = c.get_rate(input_curr, output_curr)
    conversion = rate * float(amount)
    conversion = str(round(conversion, 2))
    symbol = cc.get_symbol(output_curr)
    return (conversion, symbol)

def validate_curr_symbol(curr):
    # Validates currencies by trying to get their symbol
    curr_symbol = cc.get_symbol(curr)
    if curr_symbol is None:
        flash(f'Not a valid code: {curr}')
        return False
    return True
    
def validate_amount(amount):
    # Validates amount by seeing if it is "float"-able and >0
    try:
        if float(amount) > 0:
            return True
        flash(f'Not a valid, positive int: {amount}')
        return False
    except:
        flash(f'Not a valid int: {amount}')
        return False