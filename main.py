import numpy as np
import pandas as pd
import ffn
import empyrical as emp
import sys
import os


def main():
    #returns = ffn.get('aapl,msft,c,gs,ge', start='2010-01-01').to_returns().dropna()
    #returns.calc_mean_var_weights().as_format('.2%')
    #print(returns)

    returns2 = np.array([.01, .02, .03, -.4, -.06, -.02])
    benchmark_returns = np.array([.02, .02, .03, -.35, -.05, -.01])

    emp.max_drawdown(returns2)

    dates = pd.date_range('20130101',periods = 6)
    df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

    alpha, beta = emp.alpha_beta(returns2, benchmark_returns)
    tratios = va_tail_ratio(df)
    print(tratios)
    print(alpha)
    print(beta)

def get_data(filename):
    df = json_normalize(pd.read_json(filename))
    coin_name = list(df)[0]
    return df, coin_name

def preop_formatting(raw,coin_name):
	df1 = raw['date']
	df2 = pd.to_numeric(raw['pctChgDoD'], errors='coerce')
    final = pd.concat([df2,df3], axis = 1)
    return final

def va_tail_ratio(returns):
    ratios = []
    for ticker in returns:
        ratios.append(emp.tail_ratio(returns[ticker]))
    return ratios


main()