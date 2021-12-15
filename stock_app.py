# imports
from flask import Flask, request, redirect, render_template
from web_scraper import scrape_yahoo
app = Flask(__name__)

# home of site
@app.route("/")
def home():

    f = open("tickers_list.txt", "r")
    lines = f.readlines()
    info_array = []
    for line in lines:
        info_array.append(scrape_yahoo(line))
    # info_array = scrape_yahoo("aapl")

    return render_template("index.html", info_array=info_array)

# debugger on
if __name__ == "__main__":
    app.run(debug=True)


