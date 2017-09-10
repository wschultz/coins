# coins.py

** This is a short script that totals up all your USD from LTC/ETH/BTC from your GDAX account. **

You'll to do the following files:

```
git clone https://github.com/wschultz/coins.git
cd coins
touch private/credentials.py
```

Edit private/credentials.py to looks like this, except with your keys:

```
key        = '888888888888888888888888888888888'
b64secret  = '8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888'
passphrase = '88888888888'
```

The key, b64secret and passphrase are what you are presented when you create an API key in GDAX https://www.gdax.com/settings/api

.gitignore disallows private/* so you don't upload your API info to github, because that would be awesome.

Output is the current date, current time, current value in USD.
