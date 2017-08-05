#!/usr/bin/env python

""" 
    This is a short script that totals up all your USD from LTC/ETH/BTC from your GDAX account.

private is setup as:

[wschultz]$ find private
private
private/__init__.py
private/credentials.py

[wschultz]$ cat private/credentials.py
key        = '888888888888888888888888888888888'
b64secret  = '8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888'
passphrase = '88888888888'

"""

import private.credentials
import gdax, time

public_client = gdax.PublicClient()
auth_client = gdax.AuthenticatedClient(private.credentials.key, private.credentials.b64secret, private.credentials.passphrase)

def added_up():

  all_data = auth_client.get_accounts()

  coin_totals = dict()
  for i in all_data:
    coin_totals.update({i['currency']:i['balance']})

  coin_price = dict()
  for c in coin_totals.keys():
    if c == 'USD':
      coin_price.update({c: 1})
    else:
      d = "%s-USD" % c
      coin_price.update({c: public_client.get_product_order_book(d)['asks'][0][0]})

  result = 0
  for i in coin_totals.keys():
    result += float(coin_totals[i]) * float(coin_price[i])
  
  result = float(format(result, '.2f'))
  return(str(result))

print(time.strftime("%d%m%y %H%M") + " " + added_up())
