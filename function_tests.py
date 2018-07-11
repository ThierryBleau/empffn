import json
import pandas as pd
import numpy as np
import main
import empyrical as emp
import ffn



if __name__ == '__main__':


    #data fetching
    #data, name = main.get_data('digicor.json')
    #print(data.head(10))
    #print(data.info())
    #data = main.preop_formatting(data, name)

    #data = main.add_ticker(data,'digicor')
    tickers = ['digicor','digicor']
    data = main.get_tickers(tickers)
    #print(list(data.columns))
    #functions
    map_ratios = main.df_map(emp.tail_ratio, data)
    map_sharpe = main.df_map(emp.sharpe_ratio,data)
    kwargs = {'risk_free':1} 
    map_kwarg_sharpe = main.df_map(emp.sharpe_ratio,data,**kwargs)
    map_drawdown = main.df_map(ffn.calc_max_drawdown, data)
    map_drawdown_series = main.df_map(ffn.to_drawdown_series, data)
    #print(tail_ratios)

    #is a series so .values returns list
    print(map_ratios)
    print(map_sharpe)
    print(map_kwarg_sharpe)
    print(map_drawdown)
    print(map_drawdown_series.head(5))