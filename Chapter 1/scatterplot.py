import history as h
import functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start_date = "2009-01-01"
end_date = "2012-12-31"

dates = pd.date_range(start_date, end_date)
symbols = ['SPY', 'XOM', 'GLD']
df = h.get_csv_data(symbols, start_date, end_date)
daily_returns = functions.compute_daily_returns(df)

# IF the beta value is greater that means that that stock is more reactive to the market.
# Scatter plot SPY vs XOM
daily_returns.plot(kind='scatter', x='SPY', y='XOM')
beta, alpha = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
plt.plot(daily_returns['SPY'], beta * daily_returns['SPY'] + alpha, '-',color='r')
print "XOM Alpha", alpha
print "XOM Beta", beta
plt.show()
# Scatter plot SPY vs GLD
daily_returns.plot(kind='scatter', x='SPY', y='GLD')
beta, alpha = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
plt.plot(daily_returns['SPY'], beta * daily_returns['SPY'] + alpha, '-',color='r')
print "GLD Alpha", alpha
print "GLD Beta", beta
plt.show()
# calculate correlation coefficient
print daily_returns.corr(method='pearson')
h = h.History(symbols=['AAPL'], start_date="2009-01-01", end_date="2012-12-31")
