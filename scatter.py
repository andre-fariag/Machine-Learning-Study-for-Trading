#scatterplot of daily returns from stocks
#if alpha is grater then zero -> stock is on avarage performing better then another vs IBOV
#beta is related to the slope of line fitting scatter plot -> concept of average rate between stock vs IBOV
#correlation -> how tight the dots on scatter plots are

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data_frame
from plot import plot_data
from calculation import compute_daily_returns

def scatter_plot():
    
    #read stock and create data frame
    dates = pd.date_range('2019-01-01','2022-12-31') 
    symbols = ['IBOV','VALE3','BBDC4']
    df = get_data_frame(symbols,dates)

    #compute daily returns
    df_daily_return = compute_daily_returns(df)

    #scatter plot IBOV x VALE3
    df_daily_return.plot(kind='scatter',x='IBOV',y='VALE3')
    beta_VALE3, alpha_VALE3 = np.polyfit(df_daily_return['IBOV'],df_daily_return['VALE3'],1)
    plt.plot(df_daily_return['IBOV'], beta_VALE3*df_daily_return['IBOV'] + alpha_VALE3,'-',color='r')
    print("Beta VALE3: ",beta_VALE3)
    print("Alpha VALE3: ",alpha_VALE3)
    plt.grid()

    #scatter plot IBOV x BBDC4
    df_daily_return.plot(kind='scatter',x='IBOV',y='BBDC4')
    beta_BBDC4, alpha_BBDC4 = np.polyfit(df_daily_return['IBOV'],df_daily_return['BBDC4'],1)
    plt.plot(df_daily_return['IBOV'], beta_BBDC4*df_daily_return['IBOV'] + alpha_BBDC4,'-',color='r')
    print("Beta BBDC4: ",beta_BBDC4)
    print("Alpha BBDC4: ",alpha_BBDC4)
    plt.grid()
    
    plt.show()

    #print correlation of dataframe
    print (df_daily_return.corr(method='pearson'))

if __name__ == "__main__":
    scatter_plot()
    