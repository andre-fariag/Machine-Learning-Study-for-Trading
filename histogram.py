#plots histogram of daily returns from a stock

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data_frame
from calculation import compute_daily_returns

def plot_histogram():
    
    #1)gets desired data frame
    dates = pd.date_range('2019-01-01','2022-12-31') 
    symbols = ['IBOV']
    df = get_data_frame(symbols,dates)

    #2)compute daily returns
    df_daily_return = compute_daily_returns(df)

    #3)plot daily returns in histogram form
    df_daily_return.hist(bins=30)

    #4)plot mean and standar deviation as vertical lines for reference
    mean = df_daily_return.mean().item()
    std = df_daily_return.std().item()
    plt.axvline(mean,color='w',linestyle='dashed',linewidth = 2)
    plt.axvline(std,color='r',linestyle='dashed',linewidth = 2)
    plt.axvline(-std,color='r',linestyle='dashed',linewidth = 2)
    plt.show()

if __name__ == "__main__":
    plot_histogram()
