import history
import functions
import matplotlib.pyplot as plt
import numpy as np
# List of symbols
symbols = ['AAPL']
# Create your data frame
df = history.get_csv_data(symbols, '01/01/2007','01/01/2017')
# Fill all null values
functions.fill_null_values(df)
# Get daily returns
daily_returns = functions.compute_daily_returns(df)
# Generate histogram
daily_returns.hist(bins=20)
mean_spy = daily_returns['SPY'].mean()
std_spy = daily_returns['SPY'].std()

plt.axvline(mean_spy, color="w",linestyle="dashed", linewidth=2)
plt.axvline(std_spy, color="r",linestyle="dashed", linewidth=2)
plt.axvline(-std_spy, color="r",linestyle="dashed", linewidth=2)

# mean_aapl = daily_returns['AAPL'].mean()
# std_aapl = daily_returns['AAPL'].std()
#
# plt.axvline(mean_aapl, color='w', linestyle='dashed', linewidth=2)
# plt.axvline(std_aapl, color='r', linestyle='dashed',linewidth=2)
# plt.axvline(-std_aapl, color='r', linestyle='dashed',linewidth=2)


daily_returns['SPY'].hist(bins=20, label='SPY')
daily_returns['AAPL'].hist(bins=20, label='AAPL')

daily_returns.plot(kind='scatter', x='SPY', y='AAPL')
beta_AAPL, alpha_AAPL = np.polyfit(daily_returns['SPY'], daily_returns['AAPL'], 1)
plt.plot(daily_returns['SPY'], beta_AAPL*daily_returns['SPY'] + alpha_AAPL, '-', color='r')
print "Beta-AAPL", beta_AAPL
print "alpha_AAPL", alpha_AAPL

plt.legend(loc='upper right')
plt.show()
