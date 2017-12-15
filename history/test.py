import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo
import numpy as np
import history

df = history.get_csv_data(['AAPL'])
# df['timestamp'] = pd.date_range('2000-1-1', periods=200, freq='D')

print df
