import pandas as pd
from pathlib import Path

# ***********************************************************************
#                          COLLECTING THE DATA
#************************************************************************

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
coinbase = coinbase.dropna()
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


#************************************************************************
#                          ANALYZING THE DATA
#************************************************************************



#1. Choosing columns of data to focus analysys on

#Selecting `Timestamp (the index)` and `Close` from BITSTAMP DataFrame
bitstamp_sliced = bitstamp.loc[:, "Close"]
print(bitstamp_sliced.head())

#Selecting `Timestamp (the index)` and `Close` from COINBASE DataFrame
coinbase_sliced = coinbase.loc[:, "Close"]
print(coinbase_sliced.head())


#************************************************************************
#2. Extracting summary statistics and plotting the data

#The summary statistics for BITSTAMP DataFrame
print(bitstamp_sliced.describe())

#The summary statistics for COINBASE DataFrame
print(coinbase_sliced.describe())

#Creating a line plot for the BITSTAMP DataFrame
bitstamp_sliced.plot(figsize=(10,5), title = "Bitstamp Prices", color = "blue")

#Creating a line plot for the COINBASE DataFrame
bitstamp_sliced.plot(figsize=(10,5), title = "Coinbase Prices", color = "blue")

#Overlaying the visualizations for the bitstamp and coinbase DataFrames in one plot
bitstamp_sliced.plot(legend=True, figsize=(15, 10), title="Bitstamp v. Coinbase", color="blue", label="Bitstamp")
coinbase_sliced.plot(legend=True, figsize=(15, 10), color="orange", label="Coinbase")

#Overlaying the visualizations for the bitstamp and coinbase DataFrames in one plot (earlier 1-month period)
bitstamp_sliced.loc["2018-01-01":"2018-02-01"].plot(legend=True, figsize=(15, 10), title="Exchange Comparison (Earlier Time Period)", color="blue", label="Bitstamp")
coinbase_sliced.loc["2018-01-01":"2018-02-01"].plot(legend=True, figsize=(15, 10), color="orange", label="Coinbase")

#Overlaying the visualizations for the bitstamp and coinbase DataFrames in one plot (later 1-month period)
bitstamp_sliced.tail()
bitstamp_sliced.loc["2018-02-28":"2018-03-31"].plot(legend=True, figsize=(15, 10), title="Exchange Comparison (Later Time Period)", color="blue", label="Bitstamp")
coinbase_sliced.loc["2018-02-28":"2018-03-31"].plot(legend=True, figsize=(15, 10), color="orange", label="Coinbase")


#******************************************************************
#3. Specific dates analysis

#Overlaying the visualizations for the bitstamp and coinbase DataFrames in one plot (earlier 1-day period)
bitstamp_sliced.loc["2018-01-16"].plot(legend=True, figsize=(15, 10), title="Jan 16, 2018", color="blue", label="Bitstamp")
coinbase_sliced.loc["2018-01-16"].plot(legend=True, figsize=(15, 10), color="orange", label="Coinbase")

