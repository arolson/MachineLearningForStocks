import urllib, urllib2
import csv
import pandas as pd
# Historical data can only come in the format of a csv file
# ex: https://finance.google.com/finance/historical?q=AAPL&startdate=01/01/2017&enddate=01/06/2017&output=csv

# Get Google finance data
def get_googlefinance_history_data(symbols, start_date, end_date):
    if not symbols:
        return
    results = {}
    for symbol in symbols:
        data = url_client(symbol, start_date, end_date)
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
        word['Date'] = word.pop('\xef\xbb\xbfDate')
    return array

def get_csv_data(symbols, start_date, end_date):
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")
    dates = pd.date_range(start_date, end_date)
    df_final = pd.DataFrame(index=dates)

    results = {}
    for symbol in symbols:
        data = url_client(symbol, start_date, end_date)
        df_temp = pd.read_csv(data, parse_dates=True, index_col="Date",
                usecols=["Date", "Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Close": symbol})
        df_final = df_final.join(df_temp)
        if symbol == "SPY":  # drop dates SPY did not trade
            df_final = df_final.dropna(subset=["SPY"])
    return df_final

def url_client(symbol, start_date, end_date):
    base_url = "https://finance.google.com/finance/historical"
    query = {
        'q': '{symbol}'.format(**locals()),
        'startdate': '{start_date}'.format(**locals()),
        'enddate': '{end_date}'.format(**locals()),
        'output': 'csv'
    }
    url_options = urllib.urlencode(query)
    full_url = base_url + '?' + url_options
    try:data = urllib2.urlopen(full_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
    return data
