# README
<h2>Machine Learning For Stocks</h2>
Course repo for my notes and experiments during the Machine Learning for Trading course with Udacity.

# How to retrieve Stock history
Add `history.py` to your active directory. And call either `get_csv_data(symbols)`(gets data in csv format, and returns it as a pandas data frame) or `get_googlefinance_history_data(symbols)`(returns the data as a hash). 
Each takes a list of symbols ex: `['AAPL','SPY']` and retrieves a twenty year history of price data on each respective stock.

This file uses the Alpha Vantage API. Be sure to add your api key to your local enviroment under the name `ALPHA_VANTAGE_API_KEY`.

# Licence 
by: Andrew Olson
