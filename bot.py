#Data Source
import yfinance as yf
import time
import random

print("Starting machine...")

total_profit = 0

bought = {"USDT": [],
          "DAI": [],
          "BUSD": [],
          "TUSD": [],
          "USDC": [],
          "UST": []}

while True:
    prices = {"USDT": yf.download(tickers='USDT-USD', period = '5h', interval = '1m', progress=False)["Close"][-1],
              "DAI": yf.download(tickers='DAI-USD', period = '5h', interval = '1m', progress=False)["Close"][-1],
              "BUSD": yf.download(tickers='BUSD-USD', period = '5h', interval = '1m', progress=False)["Close"][-1],
              "TUSD": yf.download(tickers='TUSD-USD', period = '5h', interval = '1m', progress=False)["Close"][-1],
              "USDC": yf.download(tickers='USDC-USD', period = '5h', interval = '1m', progress=False)["Close"][-1],
              "UST": yf.download(tickers='UST-USD', period = '5h', interval = '1m', progress=False)["Close"][-1]}

    buy_tick = min(prices, key=prices.get)

    _price = prices[buy_tick]

    if(_price < 1):
        bought[buy_tick].append(_price)
        print("Buying " + buy_tick + ": " + str(_price))

    for key, value in prices.items():
        _tick_profit = 0
        
        if(value >= 1):
            for _bought_tick in bought[key]:
                _tick_profit += value-_bought_tick
            if(len(bought[key]) > 0):
                print("Sold " + key + " for " + str(_tick_profit) + " profit!")
                total_profit += _tick_profit
                bought[key] = []
            
