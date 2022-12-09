# Raw Package
import numpy as np
import pandas as pd
import ssl
#Data Source
import yfinance as yf
from flask import Flask,jsonify
import plotly.graph_objs as go


app = Flask(__name__)

#Print data
@app.route("/")
def hi():
  return "hello"
@app.route("/data")
def data():
  return str(yf.download(tickers='005930.KS', period='1d', interval='1m'))
@app.route("/삼성전자")
def samsung():
    #Data viz
    data = yf.download(tickers='005930.KS', period='1d', interval='1m')
# import plotly.graph_objs as go
    fig = go.Figure()
        #Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))
    # Add titles
    fig.update_layout(
    title='삼성전자 주식 차트',
    yaxis_title='삼성전자 주가')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    #Show
    return fig.show()


if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))