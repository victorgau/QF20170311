import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    df=web.DataReader("^DJI", 'yahoo', datetime(2016,1,1))
    df.sort_index(ascending=False)
    df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    return render_template('index.html', symbol="Dow Jones Index")

@app.route('/<symbol>')
def draw(symbol):
    df=web.DataReader(symbol, 'yahoo', datetime(2016,1,1))
    df.sort_index(ascending=False)
    df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    return render_template('index.html', symbol=symbol)
