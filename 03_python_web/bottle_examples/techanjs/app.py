import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
from bottle import route, run, template, get, static_file

# Static Routes
@get("/static/<filepath:re:.*\.csv>")
def csv(filepath):
    return static_file(filepath, root="static")

@route('/')
def index():
    df=web.DataReader("^DJI", 'yahoo', datetime(2016,1,1))
    df.sort_index(ascending=False)
    df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    return template('index', name="Dow Jones Index")

run(host='localhost', port='9999')