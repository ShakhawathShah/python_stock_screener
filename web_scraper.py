import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

f = open("tickers_list.txt", "r")
lines = f.readlines()


def scrape_yahoo(stock):
    my_url = ('http://finance.yahoo.com/q/ks?s=' + stock)
    req = requests.get(my_url)
    soup = BeautifulSoup(req.text, "html.parser")

    stock_price = soup.findAll(
        "span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})

    ticker = soup.findAll("h1", {"class": "D(ib) Fz(18px)"})

    high_52_week = soup.findAll(
        "td", {"class": "Fw(500) Ta(end) Pstart(10px) Miw(60px)"})

    my_array = [str(ticker[0].text), str(stock_price[0].text),
                str(high_52_week[12].text), str(high_52_week[13].text)]

    return (my_array)
    # print("Name and Ticker: " + ticker[0].text)
    # print("Stock Price: " + stock_price[0].text)
    # print("52 Week High: " + high_52_week[12].text)
    # print("52 Week low: " + high_52_week[13].text)


# user_stock = input("Enter the ticker of the stock you would like to view: \n")
