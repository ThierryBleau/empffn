import numpy as np
import pandas as pd
import ffn
import empyrical as emp
import sys
import os


def main():
    returns = ffn.get('aapl,msft,c,gs,ge', start='2010-01-01').to_returns().dropna()
    returns.calc_mean_var_weights().as_format('.2%')
    print(returns)

    returns2 = np.array([.01, .02, .03, -.4, -.06, -.02])
    benchmark_returns = np.array([.02, .02, .03, -.35, -.05, -.01])

    emp.max_drawdown(returns2)

    alpha, beta = emp.alpha_beta(returns2, benchmark_returns)
    print(alpha)
    print(beta)

main()