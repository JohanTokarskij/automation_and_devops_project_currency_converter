from dotenv import load_dotenv
import os

from flask import Flask, render_template, request
import requests


load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv('FREE_CURRECY_API_KEY')
API_URL = 'https://api.freecurrencyapi.com/v1/latest'


CURRENCIES = [
    'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY',
    'HKD', 'NZD', 'SEK', 'KRW', 'SGD', 'NOK', 'MXN', 'INR',
    'RUB', 'ZAR', 'TRY', 'BRL', 'TWD', 'DKK', 'PLN', 'THB',
    'IDR', 'HUF', 'CZK', 'ILS', 'CLP', 'PHP', 'AED', 'COP',
    'SAR', 'MYR', 'RON'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    selected_from = 'EUR'  # Default selection
    selected_to = 'USD'    # Default selection

    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')

        if from_currency:
            selected_from = from_currency
        if to_currency:
            selected_to = to_currency

        if selected_from == selected_to:
            error = "Please select two different currencies."
        else:
            params = {
                'apikey': API_KEY,
                'base_currency': selected_from,
                'currencies': selected_to
            }
            try:
                response = requests.get(API_URL, params=params)
                response.raise_for_status()
                data = response.json()
                if 'data' in data and selected_to in data['data']:
                    rate = data['data'][selected_to]
                    result = f"1 {selected_from} = {rate} {selected_to}"
                else:
                    error = "Error fetching data. Please try again."
            except requests.exceptions.RequestException as e:
                error = f"An error occurred: {str(e)}"

    return render_template(
        'index.html',
        currencies=CURRENCIES,
        result=result,
        error=error,
        selected_from=selected_from,
        selected_to=selected_to
    )

if __name__ == '__main__':
    app.run(debug=True)
