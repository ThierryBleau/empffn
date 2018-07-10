import json
import pandas as pd
import numpy as np
import main
import empyrical as emp
import ffn



if __name__ == '__main__':


    #data fetching
    data, name = main.get_data('digicor.json')
    #print(data.head(10))

    data = main.preop_formatting(data, name)
    #print(data.head(10))
    #print(list(data.columns))
    #functions
    tail_ratios = main.va_tail_ratio(data)
    map_ratios = main.df_map(emp.tail_ratio, data)
    print(tail_ratios)

    #is a series so .values returns list
    print(map_ratios.values)