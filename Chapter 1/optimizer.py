import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo
import numpy as np
import history
def f(x):
    y = (x - 1.5)**2 + 0.5
    print 'X= {}, Y = {}'.format(x, y)
    return y
def test_run():
    xGuess = 2.0
    min_result = spo.minimize(f, xGuess, method='SLSQP', options={'disp' : True})
    print "Minima found at:"
    print 'X= {}, Y = {}'.format(min_result.x, min_result.fun)

    # Plot function values, mark Minima
    xPlot = np.linspace(0.5,2.5,21)
    yPlot = f(xPlot)
    plt.plot(xPlot,yPlot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.show()
if __name__ == "__main__":
        test_run()
