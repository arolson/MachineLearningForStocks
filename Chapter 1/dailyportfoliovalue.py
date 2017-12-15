import history
import functions
import numpy as np

start_value = 1000000
start_date = "2009-01-01"
end_date = "2012-12-31"
symbols = ['SPY', 'XOM','GOOG', 'GLD']
allocations = np.array([0.4,0.4,0.1,0.1])

df = history.get_csv_data(symbol_list, start_date, end_date)
daily_returns = functions.compute_daily_returns(df)
normed = functions.compute_normed(df)

def position_values(normed, allocations):
    return normed * allocations
# print pos_values(normed, allocations)
port_values = position_values(normed, allocations).sum(axis= 1)
daily_returns = daily_returns[1:]
cumulative_returns = (port_values[-1] / port_values[1]) - 1
avg_daily_returns = daily_returns.mean()
std_daily_returns = daily_returns.std()
