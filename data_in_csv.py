import pandas as pd
import matplotlib.pyplot as plt

def get_data(symbol):
       df = pd.read_csv("CSV/{}.csv".format(symbol))
       return df
def get_max_close(symbol):
    df = pd.read_csv("CSV/{}.csv".format(symbol))
    return df['Volume'].mean()

def plot_graph():
    df = get_data("AAPL")
    print df['Adj Close']
    df[['Close', 'Adj Close']].plot()
    plt.show()
    
def test_run():
#    for symbol in ['AAPL', 'IBM']:
#        print "Mean Volume"
#        print symbol, get_max_close(symbol)
    plot_graph()
        
if __name__ == "__main__":       
    test_run()
