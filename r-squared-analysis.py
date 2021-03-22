#! python3
"""
R-Squared Calculation Program

Objective: Calculate and find the highest R-squared of any two variables. Variables
    can be either a stock or index found on Yahoo Finance or an economic data 
    set found on the St. Louis Federal Reserve Economic Data site.

Inputs: Stock or Index tickers in yahootickers list (no limit), 
    FRED economic data ticker in fredtickers (no limit).

Output: The two tickers with the highest calculated R-squared 
    and the corresponding R-square value.

"""


import pandas as pd
from pandas_datareader import data as wb
from scipy import stats

# Insert stock or index ticker here
yahootickers = ['^GSPC', '^GDAXI', '^N225', '^BVSP']
data = pd.DataFrame()

# Pulls adjusted close info for each stock or index in yahootickers list
for ticker in yahootickers:
    data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='1980-1-1')['Adj Close']

# Insert Federal Reserve Economic Data ticker here
fredtickers = ['GDPC1', 'DGS10']

# Pulls FRED ticker data from fredtickers list
for ticker in fredtickers:
    data[ticker] = wb.DataReader(ticker, data_source='fred', start='1980-1-1')
   
data.head()

NanCountList = []
FilterList = []

# Loops through data and finds total number of Nan values in each column
for item in data:
    NanCountList.append(data[item].isna().sum())

NanCountList = sorted(NanCountList, key=abs, reverse=True)

for t in NanCountList:
    for j in data:
        if data[j].isna().sum() == t:
            FilterList.append(j)
            continue
        else:
            continue

# Filters out Nan values
for q in FilterList:
    data = data[data[q].notnull()]

data.tail()

# Creates % Change columns based on prior period using .shift(1)
for i in yahootickers:
    data[i + ' % change'] = (data[i] / data[i].shift(1)) - 1
for i in fredtickers:
    data[i + ' % change'] = (data[i] / data[i].shift(1)) - 1

data.tail()

# Calculates the R-squared for each possible combination and prints the two variables with the highest R-squared
for i in data:
    data2 = data.drop(i, 1)
    for t in data2:
        NEWX = data[i].iloc[1:]
        NEWY = data[t].iloc[1:]
        
        NEWslope, NEWintercept, NEWr_value, NEWp_value, NEWstd_err = stats.linregress(NEWX,NEWY)
        if data.columns.get_loc(i) == 0:
            slope, intercept, r_value, p_value, std_err = NEWslope, NEWintercept, NEWr_value, NEWp_value, NEWstd_err
            X, Y = NEWX, NEWY
        if NEWr_value ** 2 > r_value ** 2:
            slope, intercept, r_value, p_value, std_err = NEWslope, NEWintercept, NEWr_value, NEWp_value, NEWstd_err
            X, Y = NEWX, NEWY

print(X.name)

print(Y.name)

print(str(r_value ** 2))
