import urllib, urllib2
import ConfigParser
import json
import time

config = ConfigParser.ConfigParser()
config.readfp(open("url.conf", "rb"))

eth_ticker_bter = config.get("eth_ticker", "bter")

ltc_ticker_btctrade = config.get("ltc_ticker", "btctrade")
print(ltc_ticker_btctrade)

def get_ticker_url(url):
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
    headers = {"User-agent" : agent}
    req = urllib2.Request(url, headers = headers)
    res = urllib2.urlopen(req)
    res = res.read()
    return res

def buy_or_sell(money, position, buy, sell, hold_price):
    price = 0
    if not position or not buy or not sell:
        print('error illegal input BUYORSELL')
        return
    if position == 0:
        price = buy
    else:
        price = sell
    if price == 0:
        print('error price = 0')
        return
    if position == 0 and can_buy():
        return 1
    if position != 0 and can_sell():
        return 2

def buy(money, price):
    if not money or not price or price == 0 or money == 0:
        print('error illegal input BUY')
        return -1
    return round(money / price, 2)

def sell(position, price):
    if not position or not price or position == 0 or price == 0:
        print('error illegal input SELL')
        return -1
    return round(position * price, 2)

    


money = 10000
position = 0
hold_price = 0

times = 0
while 1:
    print(times)
    times = times + 1
    py_data = json.loads(get_ticker_url(ltc_ticker_btctrade))
    buy_price = py_data.get('buy')
    sell_price = py_data.get('sell')
    print('current price = ' + str(py_data.get('last')) + ' . buy = ' + str(py_data.get('buy')) + ' . sell = ' + str(py_data.get('sell'))) 
    flag = buy_or_sell(money, position, buy_price, sell_price, hold_price)
    if flag != 0:
        if flag == 1: #buy
            position = buy(money, buy_price)
            hold_price = buy_price
            money = 0
        if flag == 2: #sell
            money = sell(position, sell_price)
            position = 0
        print('Current money = ' + str(money) + ' ,position = ' + str(position))

    time.sleep(10)

