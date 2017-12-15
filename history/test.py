import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo
import numpy as np
import history

df = history.get_googlefinance_history_data(['AAPL'])
print df
