#!/usr/bin/env python
import os
import requests

currency = "https://api.coinmarketcap.com/v1/ticker/"

r = requests.get(currency)
results = r.json()

### START EDIT HERE ###
omg = 84.4215   # Bittrex
btc = 2.1435370 # GDAX
xrp = 6328.8837 # Bitstamp

myholdings = {"omg": omg, "btc": btc, "xrp": xrp}
#### END EDIT HERE ####

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

