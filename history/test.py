import history
import functions
# results = history.get_googlefinance_history_data(['AAPL'], '01/01/2016','01/01/2017')
# print results
results = history.get_csv_data(['AAPL'], '01/01/2016','01/01/2017')
print results
