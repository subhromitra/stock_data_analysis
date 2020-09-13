"""
What does this program do ?
-> It fetches Nifty100 data for the past 15 years from Yahoo Finance API.

What is Nifty100 ?
-> Nifty100 represents the top 100 companies on the basis of market
   capitalization listed in NSE. 
"""
# Importing necessary libraries
import os
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime as dt

# Reading CSV file from which we will get the company tickers
df = pd.read_csv('nifty100list.csv')
nifty100_tickers = list(df['Symbol'])

# Utility function to get Nifty100 data
def get_nifty_100_data():
    # Creating new folder if none exists
    if not os.path.exists('nifty100_data'):
        os.mkdir('nifty100_data')

    # Declaring start & end dates
    st = dt.datetime(2005,1,1)
    en = dt.datetime(2020,9,1)

    # For loop for fetching data for all companies
    for ticker in nifty100_tickers:
        if not os.path.exists('nifty100_data/{}.csv'.format(ticker)):
            ticker_ns = ticker + ".NS"
            df = web.DataReader(ticker_ns, 'yahoo', st, en)
            df.to_csv('nifty100_data/{}.csv'.format(ticker))
            print("{}'s data just got stored".format(ticker))
        else:
            print("Already have {}'s data".format(ticker))
    return

if __name__ == "__main__":
    print("Starting NIFTY100 data fetch ...\n")
    get_nifty_100_data()
    print("\nNIFTY100 data fetch complete !!!")

            
        
        
    
