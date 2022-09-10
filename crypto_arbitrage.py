import pandas as pd
from pathlib import Path

# ***COLLECTING THE DATA***
# Collect the data for the bitstamp.csv CSV file
bitstamp = pd.read_csv(
    Path('./Resources/bitstamp.csv'),
    index_col = "Timestamp",
    parse_dates = True,
    infer_datetime_format = True)

# View the DataFrame
print(bitstamp.head())

# Collect the data for the coinbase.csv CSV file
coinbase = pd.read_csv(
    Path('./Resources/coinbase.csv'),
    index_col = "Timestamp",
    parse_dates = True,
    infer_datetime_format = True)

# View the DataFrame
print(coinbase.head())



#***PREPARING THE DATA***
#Analyzing the missing data
print(bitstamp.isnull().sum())

#Due to equal quantity of missing data in each column, it can be just removed from the spreadsheet
#Dropping missing data
bitstamp.dropna()
print(bitstamp.isnull().sum())



