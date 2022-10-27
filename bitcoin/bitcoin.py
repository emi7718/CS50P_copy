import requests
import sys

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')
try:
    btc_qty = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')
else:
    response = (requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')).json()
    clean_response = (response['bpi']['USD']['rate']).replace(',', '')
    calculated_btcs= float(clean_response) * btc_qty
    print(f'${calculated_btcs:,.4f}')