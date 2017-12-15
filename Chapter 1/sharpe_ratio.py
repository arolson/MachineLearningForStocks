import history
import functions
import numpy as np
import math

start_date = "2009-01-01"
end_date = "2012-12-31"
symbols = ['SPY', 'XOM', 'GOOG','GLD']
start_value = 1000000
allocations = np.array([0.4,0.4,0.1,0.1])

df = history.get_csv_data(symbols, start_date, end_date)
daily_returns = functions.compute_daily_returns(df)
normed = functions.compute_normed(df)

allocated = functions.position_values(normed, allocations)
position_values = np.array(allocated)
portfolio_values = position_values.sum(axis = 1)
daily_returns = daily_returns[1:]
cumulative_returns = (portfolio_values[-1] / portfolio_values[1]) - 1
avg_daily_returns = daily_returns.mean()
std_daily_returns = daily_returns.std()
k = math.sqrt(252)
sharpe_ratio = k * avg_daily_returns / std_daily_returns
print sharpe_ratio
