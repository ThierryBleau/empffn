import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import ffn
import empyrical as emp


def get_data(filename):
    df = pd.read_json(filename)
    coin_name = list(df)[0]
    df1 = json_normalize(df[coin_name])
    df1 = df1.iloc[::-1]
    return (df1, coin_name)

def get_csv(filename):
    df = pd.read_csv(filename)
    df = df.iloc[::-1]
    df.set_index('Date', inplace = True)
    return df.dropna()

def usd_formatting(raw, coin_name):
    df1 = raw['time (UTC)']
    df2 = pd.to_numeric(raw['pctChgDoD (USD)'], errors = 'coerce')
    final = pd.concat([df1,df2],axis=1)
    final.columns = ['time (UTC)', coin_name]
    final.set_index('time (UTC)', inplace = True)
    final.dropna(axis=1)
    return final

def btc_formatting(raw, coin_name):
    df1 = raw['time (UTC)']
    df2 = pd.to_numeric(raw['pctChgDoD (BTC)'], errors = 'coerce')
    final = pd.concat([df1,df2],axis=1)
    final.columns = ['time (UTC)', coin_name]
    final.set_index('time (UTC)', inplace = True)
    final.dropna(axis=1)
    return final

def add_ticker(main_df,tick_name):
    new, name = get_data(tick_name + '.json')
    new = preop_formatting(new, name)
    #what to do with date alignment?
    final = pd.concat([main_df,new], axis=1)
    return final

def get_tickers(args):
    first = str(args[0]) + '.json'
    new, name = get_data(first)
    new = preop_formatting(new, name)
    for ticker in args[1:]:
        new = add_ticker(new,ticker)
    return new

def func_name(func):
    name = str(func).split()
    return name[1]

#should return calcs
def df_map(func, df, **kwargs):
    result = df.apply(lambda x: func(x,**kwargs))
    df_result = pd.DataFrame(result)
    if df_result.shape[0] == 1:
        return df_result.iloc[0,0]
    else:
        if df_result.shape[1] == 1:
            df_result.columns = [func_name(func)]
        return df_result.dropna()
