import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stuff
import os

def compute_normed(df):
    normed = df.copy()
    normed[1:] = df[1:] / df[:-1].values
    normed.ix[0,:] = 0
    return normed

# Note to self probably should not plot multiple stocks this way
def test_run():
    allocs = [0.4,0.4,0.1,0.1]
    start_values = 1000000

    #Read the data
    symbol_list = ['AAPL']
    start_date = "2005-12-31"
    end_date = "2014-12-07"
    dates = pd.date_range(start_date, end_date)
    df = stuff.get_data(symbol_list, dates)
    #Fill gaps
    stuff.fill_null_values(df)

    for symbol in symbol_list:
    # Bollinger Bands
        # compute rolling mean
        rm = stuff.get_rolling_mean(df[symbol])
        # compute rolling standard deviation (std)
        rstd = stuff.get_rolling_std(df[symbol])
        # compute Bollinger Bands, default * 2
        upper_band, lower_band = stuff.get_bollinger_bands(rm, rstd)
        stuff.setup_plot(df, str(symbol))
        rm.plot(label="Rolling mean {}".format(str(symbol)))
        upper_band.plot(label="Upper band {}".format(str(symbol)))
        lower_band.plot(label="Lower band {}".format(str(symbol)))

    normed = compute_normed(df)
    for symbol in symbol_list:
        allocated = normed[symbol].values * allocs
        print "{}: ".format(symbol), allocated
    # print stuff.compute_daily_returns(df)
    #plt.show()
if __name__ == "__main__":
    test_run()
