#plots histogram of daily returns from a stock

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data_frame
from calculation import compute_daily_returns

def plot_histogram(symbols):
    
    #gets desired data frame
    dates = pd.date_range('2019-01-01','2022-12-31') 
    df = get_data_frame(symbols,dates)

    #compute daily returns
    df_daily_return = compute_daily_returns(df)

    #plot daily returns in histogram form
    for symbol in symbols:
        df_daily_return[symbol].hist(bins=20,label=symbol)
    
    #plot mean and standar deviation as vertical lines for reference
    #mean = df_daily_return.mean().item()
    #std = df_daily_return.std().item()
    #print (df_daily_return.kurtosis())
    #plt.axvline(mean,color='w',linestyle='dashed',linewidth = 2)
    #plt.axvline(std,color='r',linestyle='dashed',linewidth = 2)
    #plt.axvline(-std,color='r',linestyle='dashed',linewidth = 2)

    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    symbols = ['IBOV','VALE3','BBDC4','XPML11']
    plot_histogram(symbols)
