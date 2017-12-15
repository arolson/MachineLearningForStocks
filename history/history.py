import urllib, urllib2
import csv
import pandas as pd
import os
# Historical data can only come in the format of a csv file if using google finance
# ex: https://finance.google.com/finance/historical?q=AAPL&startdate=01/01/2017&enddate=01/06/2017&output=csv
# TODO: using alpha vantage, add your apikey => to your ~/.bash_profile under key: ALPHA_VANTAGE_API_KEY
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo&datatype=csv
# Get Google finance data
def get_googlefinance_history_data(symbols):
    if not symbols:
        return
    results = {}
    for symbol in symbols:
        data = url_client(symbol)
        results[symbol] = to_array(data)
    return results
# Turn that data into a readable array
def to_array(data):
    reader = csv.DictReader(data)
    array = []
    for line in reader:
        array.append(line)
    # Fix CSV Weirdness
    for word in array:
        word['date'] = word.pop('timestamp')
    return array

def get_csv_data(symbols):
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")
    df_final = pd.DataFrame()

    for symbol in symbols:
        data = url_client(symbol)
        df_temp = pd.read_csv(data, parse_dates=True, index_col="timestamp",
                usecols=["timestamp", "close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"close": symbol})
        df_final = pd.concat([df_final,df_temp], axis=1)

        if symbol == "SPY":  # drop dates SPY did not trade
            df_final = df_final.dropna(subset=["SPY"])
    return df_final

def url_client(symbol):
    base_url = "https://www.alphavantage.co/query"
    query = {
        'symbol': '{symbol}'.format(**locals()),
        'function': 'TIME_SERIES_DAILY',
        'outputsize' : 'compact',
        'apikey': os.environ["ALPHA_VANTAGE_API_KEY"],
        'datatype': 'csv'
    }
    url_options = urllib.urlencode(query)
    full_url = base_url + '?' + url_options
    try:data = urllib2.urlopen(full_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
    return data
