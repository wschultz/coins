# coins.py

** This is a short script that totals up all your USD from LTC/ETH/BTC from your GDAX account. **

This relies on the gdax library located here: https://github.com/danpaquin/gdax-python

You'll need to do the following, keep in mine credentials.py doesn't exist and needs to be created with your api info:

```
pip install gdax
git clone https://github.com/wschultz/coins.git
cd coins
touch private/credentials.py
```

Edit private/credentials.py to looks like this, except with your keys:

```
key        = 'abcdefghijklmnopqrustuvwxyz012345'
b64secret  = 'abcdefghijklmnopqrustuvwxyz01234567890abcdefghijklmnopqrustuvwxyz01234567890abcdefghijkl'
passphrase = 'abcdefhijkl'
```

The key, b64secret and passphrase are what you are presented when you create an API key in GDAX https://www.gdax.com/settings/api

.gitignore disallows private/credentials.py and .pyc so you don't upload your API info to github, because that would be awesome.

Output is the current date, current time, current value in USD.
