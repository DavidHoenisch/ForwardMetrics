import pandas as pd
import plotly as px
import configparser
import requests
import sys
from alpha_vantage.timeseries import TimeSeries
import datetime
from prophet import Prophet
from prophet import plot
from flask import request
import os
from website import DOWNLOAD_FOLDER

date = datetime.datetime.now()
EXPORT_FILE = f'{str(date)}-predictive.csv'

def api_predict(ticker_symbol, api_key, frequency):
    try:
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, metadata = ts.get_intraday(symbol=ticker_symbol, interval=frequency,
                                             outputsize='full')
        close_data = data['date']['4. close']
    except:
        pass

def upload_predict(file, periods):

    df = pd.read_csv(file)
    formated = df.rename(columns = {'Date':'ds', 'Close':'y'})
    data_set = formated.sort_values(by="ds", ascending=True)[['ds', 'y']]

    test_size = 20

    df_train = data_set[:-test_size]
    df_test = data_set[-test_size:]

    df_train

    df_test

    prpht = Prophet(daily_seasonality = False)
    prpht.fit(df_train)

    future = prpht.make_future_dataframe(periods=periods)
    forecast = prpht.predict(future)

    fig1 = prpht.plot(forecast)


    outfile = forecast.to_csv(os.path.join(DOWNLOAD_FOLDER, EXPORT_FILE))
    json_data = forecast.to_json()

    print(json_data)

    return outfile
