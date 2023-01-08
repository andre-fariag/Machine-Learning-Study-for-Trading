import os
import pandas as pd

df_directory = os.path.dirname(os.path.dirname(__file__)) + "/TradingAnalysis-ML/DataFrame/"

#input = symbol ; output = dataframe file of that symbol
def symbol_to_path(symbol,directory):
    return os.path.join(directory,"{}.csv".format(str(symbol)))

def get_data_frame(symbols,dates):
    df = pd.DataFrame(index=dates) #creates a blank data frame

    #Puts IBOV at 0 position -> it will be read first so its Dates is used as main REFERENCE
    if "IBOV" not in symbols:
        symbols.insert(0,"IBOV")

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol, df_directory), index_col="Date",
                            parse_dates=True, usecols=['Date','Adj Close'],
                            na_values=['nan'])
        
        #rename column Adj Close to stock name  
        df_temp = df_temp.rename(columns = {'Adj Close':symbol})
        
        df = df.join(df_temp)
        
        #removes every NaN value from the data frame IBOV only (REFERENCE)
        if symbol == "IBOV":
            df = df.dropna(subset=["IBOV"])
            
    return df