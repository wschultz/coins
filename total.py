#!/usr/bin/env python
import requests
import private.holdings

"""

    This is a short script that totals up all your holdings and outputs a total USD amount.

    Create private/holdings.py

    Example:
      $cat private/holdings.py
      class Holdings(object):
        omg = 100       # Bittrex
        btc = 6         # GDAX
        xrp = 1000      # Bitstamp

"""

currency = "https://api.coinmarketcap.com/v1/ticker/"

r = requests.get(currency)
results = r.json()

myholdings = {k:v for k, v in private.holdings.Holdings.__dict__.items() 
              if not (k.startswith('__'))}

totals = []
total = 0

for i in results:
  if str(i['symbol']).lower() in myholdings.keys():
    for k,v in myholdings.items():
      if k == str(i['symbol']).lower():
        totals.append(float(i['price_usd']) * v)

for t in totals:
  total += t

print(total)

