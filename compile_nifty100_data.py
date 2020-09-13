"""
What does this program do ?
-> It combines Adj Close data of all Nifty100 companies in one CSV file. This
    would then be used to find correlation between them.
"""
# Importing necessary libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt

def compile_data():
    main_df = pd.DataFrame()
    count = 0

    for fname in os.listdir('nifty100_data'):
        count += 1
        df = pd.read_csv('nifty100_data/{}'.format(fname))
        df.set_index('Date', inplace=True)
        ticker = fname.split('.')[0]

        df.rename(columns = {'Adj Close':ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'], axis=1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print("Done {} companies".format(count))

    print(main_df.head())
    main_df.to_csv('nifty100_joined_closes_2005_to_2020.csv')
    return

if __name__ == "__main__":
    compile_data()
