import time
import pandas as pd
import configparser
import requests
import sys
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime

parser = configparser.ConfigParser()
config_file = "config.ini"
parser.read(config_file)
vantage_api_key = parser.get('vantage', 'api_key')
telegram_api_key = parser.get('telegram', 'api_key')
telegram_chat_id = parser.get('telegram', 'chat_id')
telegram_send_url = f'https://api.telegram.org/bot' + telegram_api_key + '/sendMessage'

ticker = 'MSFT'
tolerance = 0.004

i = 1
while i == 1:
    try:
        ts = TimeSeries(key=vantage_api_key, output_format='pandas')
        data, metadata = ts.get_intraday(symbol=ticker, interval='1min',
                                         outputsize='full')
        close_data = data['4. close']
        percent_change = close_data.pct_change()
        if abs(close_data[-1]) > tolerance:
            nowtime = datetime.now()
            message = str(ticker) + " met set tolerance of > " + str(tolerance) + " at closing " + str(nowtime)
            requests.post(telegram_send_url, json={'chat_id': telegram_chat_id,
                                                   'text': message})
            print("message sent @" + str(nowtime) + " to chatID "
                  + str(telegram_chat_id))
        time.sleep(60)

    except KeyboardInterrupt:
        print("Program stopped")
        sys.exit(1)
