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



#***************************************************************************
#                       PREPARING THE DATA
#***************************************************************************

#Analyzing the missing data in BITSTAMP.CSV
print(bitstamp.isnull().sum())

#Due to equal quantity of missing data in each column, it can be just removed from the spreadsheet
#Dropping missing data
bitstamp = bitstamp.dropna()
print(bitstamp.isnull().sum())

#Removing $sign symbol from data 
bitstamp.loc[:, 'Close'] = bitstamp.loc[:, 'Close'].str.replace('$', '')

#Converting text data type in column "Close" to float
bitstamp.loc[:, "Close"] = bitstamp.loc[:, "Close"].astype("float")

#Check the data for duplicated values
print(bitstamp.duplicated().sum())           #no duplicated values found

#but just in case
bitstamp = bitstamp.drop_duplicates()


#Analyzing the missing data in COINBASE.CSV
print(coinbase.isnull().sum())

#Due to equal quantity of missing data in each column, it can be just removed from the spreadsheet
#Dropping missing data
coinbase = bitstamp.dropna()
print(coinbase.isnull().sum())


#print(coinbase.dtypes)
#Converting float data type in column "Close" to string, because we need to remove the $sign
coinbase.loc[:, "Close"] = coinbase.loc[:, "Close"].astype("string")

#Removing $sign symbol from data 
coinbase.loc[:, 'Close'] = coinbase.loc[:, 'Close'].str.replace('$', '')

#Converting text data type in column "Close" to float
coinbase.loc[:, "Close"] = coinbase.loc[:, "Close"].astype("float")

#Check the data for duplicated values
print(coinbase.duplicated().sum())           #no duplicated values found

#but just in case
coinbase = coinbase.drop_duplicates()






