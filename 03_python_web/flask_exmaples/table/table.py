import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    df=web.DataReader("^DJI", 'yahoo', datetime(2016,1,1))
    return df.to_html()

@app.route('/<symbol>')
def prices(symbol):
    df=web.DataReader(symbol, 'yahoo', datetime(2016,1,1))
    return df.to_html()
