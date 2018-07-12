import json
import pandas as pd
import numpy as np
import main
import empyrical as emp
import ffn
import time



if __name__ == '__main__':


    #data fetching
    #data, name = main.get_data('digicor.json')
    #print(data.head(10))
    #print(data.info())
    #data = main.preop_formatting(data, name)

    #data = main.add_ticker(data,'digicor')
    #tickers = ['digicor','digicor']
    #data = main.get_tickers(tickers)
    #print(list(data.columns))
    #functions
    #map_ratios = main.df_map(emp.tail_ratio, data)
    #map_sharpe = main.df_map(emp.sharpe_ratio,data)
    #kwargs = {'risk_free':1} 
    #map_kwarg_sharpe = main.df_map(emp.sharpe_ratio,data,**kwargs)
    #map_drawdown = main.df_map(ffn.calc_max_drawdown, data)
    #map_drawdown_series = main.df_map(ffn.to_drawdown_series, data)
    #print(tail_ratios)

    
    data, name = main.get_data('bletchley.json')
    btc = main.btc_formatting(data,name)
    usd = main.usd_formatting(data,name)

    start_usdsharpe = time.clock()
    print(start_usdsharpe)
    usd_sharpe = main.df_map(ffn.calc_sharpe,usd)
    end_usdsharpe = time.clock()
    print(end_usdsharpe)
    print('usd:' + str(usd_sharpe))
    usdtime = end_usdsharpe - start_usdsharpe
    print('time:'+ str(usdtime))

    start_btcsharpe = time.clock()
    btc_sharpe = main.df_map(ffn.calc_sharpe,btc)
    end_btcsharpe = time.clock()
    print('btc:' +str(btc_sharpe))
    btctime = end_btcsharpe - start_btcsharpe
    print('time:' + str(btctime))

    csv = main.get_csv('xps.csv')
    time_list = []
    sharpe_list = []
    arg1y = {'rf':1.44,'nperiods':1}
    arg6m = {'rf':1.745, 'nperiods':2}
    arg3m = {'rf':1.88, 'nperiods':4}
    argall1 = {'rf':1.088, 'nperiods':1}
    argall2 = {'rf':1.088, 'nperiods':2}
    argall3 = {'rf':1.088, 'nperiods':4}

    start = time.clock()
    sharpe = main.df_map(ffn.calc_sharpe,csv,**arg1y)
    end = time.clock()
    times = end - start
    sharpe_list.append(sharpe)
    time_list.append(times)
    print('sharpe year:' + str(sharpe) + ' ' + 'time:' + str(times))

    start1 = time.clock()
    sharpe = main.df_map(ffn.calc_sharpe,csv,**arg6m)
    end1 = time.clock()
    time1 = end1 - start1
    sharpe_list.append(sharpe)
    time_list.append(time1)
    print('sharpe 6m:' + str(sharpe) + ' ' + 'time:' + str(time1))

    start2 = time.clock()
    sharpe = main.df_map(ffn.calc_sharpe,csv,**arg3m)
    end2 = time.clock()
    time2 = end2 - start2
    sharpe_list.append(sharpe)
    time_list.append(time2)
    print('sharpe 3m:' + str(sharpe) + ' ' + 'time:' + str(time2))

    start3 = time.clock()
    sharpe = main.df_map(ffn.calc_sharpe,csv,**argall1)
    end3 = time.clock()
    time3 = end3 - start3
    sharpe_list.append(sharpe)
    time_list.append(time3)
    print('sharpe 3m:' + str(sharpe) + ' ' + 'time:' + str(time3))

    start4 = time.clock()
    sharpe = main.df_map(ffn.calc_sharpe,csv,**argall2)
    end4 = time.clock()
    time4 = end4 - start4
    sharpe_list.append(sharpe)
    time_list.append(time4)
    print('sharpe 3m:' + str(sharpe) + ' ' + 'time:' + str(time4))

    start5 = time.clock()
    sharpe = main.df_map(ffn.calc_sharpe,csv,**argall3)
    end5 = time.clock()
    time5 = end5 - start5
    sharpe_list.append(sharpe)
    time_list.append(time5)
    print('sharpe 3m:' + str(sharpe) + ' ' + 'time:' + str(time5))

    period = ['year','6months','3months','year','6months','3months']
    rfr = [1.44,1.745,1.88,1.088,1.088,1.088]
    results = pd.DataFrame({'period':period,'rfr':rfr,'sharpe_ratios' : sharpe_list, 'times': time_list})
    results.to_csv('results.csv')
    #is a series so .values returns list
    #print(map_ratios)
    #print(map_sharpe)
    #print(map_kwarg_sharpe)
    #print(map_drawdown)
    #print(map_drawdown_series.head(5))