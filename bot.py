#Data Source
import yfinance as yf
import time
import random

print("Starting machine...")

bought_prices = []
sold_sets = []

def calculate_total_profit():
    total_profit = 0
         
    for sets in sold_sets:
        total_profit += sets[2]

    return total_profit

while True:
    time.sleep(10)
    
    # Get Bitcoin data
    data = yf.download(tickers='USDC-USD', period = '10h', interval = '1m')["Close"]

    price = data[len(data)-1]

    if(price < 1):
        print("Buy: " + str(price))
        bought_prices.append(price)

    if(price >= 1):
        
        if(len(bought_prices) == 0):
            print("Nothing to sell: " + str(price))
            continue
        
        for to_sell in range(len(bought_prices)):
            _set = [bought_prices[to_sell], price, price-bought_prices[to_sell]]
            bought_prices.pop(to_sell)
            sold_sets.append(_set)
            
            print("Sell: " + str(_set))
            print("Total Profit: " + str(calculate_total_profit()))            

        
