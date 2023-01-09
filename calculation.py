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