import urllib, urllib2
import csv
# Historical data can only come in the format of a csv file
# ex: https://finance.google.com/finance/historical?q=AAPL&startdate=01/01/2017&enddate=01/06/2017&output=csv

# Get Google finance data
def get_googlefinance_history_data(symbols, start_date, end_date):
    if not symbols:
        return
    base_url = "https://finance.google.com/finance/historical"
    query = {
        'q': '',
        'startdate': '{start_date}'.format(**locals()),
        'enddate': '{end_date}'.format(**locals()),
        'output': 'csv'
    }
    results = {}
    for symbol in symbols:
        query['q'] = symbol
        url_options = urllib.urlencode(query)
        full_url = base_url + '?' + url_options
        try:data = urllib2.urlopen(full_url)
        except urllib2.HTTPError as e:
            print e.code
            print e.read()
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
