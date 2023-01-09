import pandas as pd

#input=data frame and a period window; output=df containing mean values of original data frame
def get_rolling_mean(df,window):
    return df.rolling(window).mean()

#input=data frame and a period window; output=df containing standard deviation values of original data frame
def get_rolling_std(df,window):
    return df.rolling(window).std()

#bollinger band = mean +- std * 2 (upper and lower bands)
def get_bollinger_bands(mean,std):
    upper_band = mean + std * 2
    lower_band = mean - std * 2
    return upper_band, lower_band

#Calculates daily returns -> (price_today/price_yesterday) - 1
def compute_daily_returns(df):
    df_daily_returns = df.copy()
    df_daily_returns = (df / df.shift(1)) - 1
    df_daily_returns.iloc[0,:] = 0 #for row 0 there is no daily return -> prior price doesn't exist
    return df_daily_returns

#Calculates cumulative returns - longar time frame
def compute_cumulative_returns(df):
    df_cmlative_returns = df.copy()
    df_cmlative_returns = (df / df_cmlative_returns.iloc[0,:]) - 1
    df_cmlative_returns.iloc[0,:] = 0
    return df_cmlative_returns

#normalize data for plotting
def normalize_data(df):
    return (df / df.iloc[0])
