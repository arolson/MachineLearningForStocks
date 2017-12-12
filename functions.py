import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def fill_null_values(df):
    df.fillna(method='ffill', inplace='TRUE')
    df.fillna(method="bfill", inplace="TRUE")

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

def setup_plot(df,symbol):
    #set up plot
    ax = df[symbol].plot(title="Stock Data",label=symbol ,fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")

def get_rolling_mean(values, window=20):
    #return the rolling mean of given values
    return values.rolling(window=20,center=False).mean()

def get_rolling_std(values, window=20):
    #return the rolling standard deviation of given values
    return values.rolling(window=20,center=False).std()

def get_bollinger_bands(rm, rstd, num=2):
    upper_band = rm + rstd * num
    lower_band = rm - rstd * num
    return upper_band, lower_band

def compute_daily_returns(df):
    # Compute and return the daily returns
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns
