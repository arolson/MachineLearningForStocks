import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_data(df, title="Stock Prices", xlabel="Date",ylabel="Price"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def symbol_to_path(symbol, base_dir="CSV"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df_final = pd.DataFrame(index=dates)
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")

    for symbol in symbols:
        file_path = symbol_to_path(symbol)
        df_temp = pd.read_csv(file_path, parse_dates=True, index_col="Date",
            usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df_final = df_final.join(df_temp)
        if symbol == "SPY":  # drop dates SPY did not trade
            df_final = df_final.dropna(subset=["SPY"])

    return df_final

def compute_daily_returns(df):
    # Compute and return the daily returns
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns

def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY','AAPL', 'IBM']
    df = get_data(symbols, dates)
    # plot_data(df)
    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily Returns", ylabel="Daily returns")
    # Plot a histogram
    daily_returns.hist(bins=20)
    mean = daily_returns['SPY'].mean()
    std = daily_returns['SPY'].std()
    plt.axvline(mean, color="w",linestyle="dashed", linewidth=2)
    plt.axvline(std, color="r",linestyle="dashed", linewidth=2)
    plt.axvline(-std, color="r",linestyle="dashed", linewidth=2)
    # daily_returns['SPY'].hist(bins=20, label='SPY')
    # daily_returns['AAPL'].hist(bins=20, label='AAPL')

    daily_returns.plot(kind='scatter', x='SPY', y='AAPL')
    # Liner Regression, Scatter Plot
    beta_AAPL, alpha_AAPL = np.polyfit(daily_returns['SPY'], daily_returns['AAPL'], 1)
    plt.plot(daily_returns['SPY'], beta_AAPL*daily_returns['SPY'] + alpha_AAPL, '-', color='r')
    print "Beta-AAPL", beta_AAPL
    print "alpha_AAPL", alpha_AAPL
    
    plt.legend(loc='upper right')
    plt.show()

    print daily_returns.kurtosis()

if __name__ == "__main__":
    test_run()
