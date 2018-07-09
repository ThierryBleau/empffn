import json
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import empyrical as e

def run1():

	df = pd.read_json('digicor.json')
	print(df.head(3))
	df1 = json_normalize(df['digicorew'])
	print(df1.head(3))
	df2 = df1[['date', 'pctChgDoD']]
	df3 = pd.to_numeric(df2['pctChgDoD'], errors='coerce')
	print(df3.head(10))
	returns = e.cum_returns(df3)

	print(returns.tail(10))



def run2():

	with open('digicor.json', 'r') as fp:
		raw = json.load(fp)['digicorew']

	data = np.array([[i['date'], i['chgDoD']] for i in raw])
	temp_ = e.cum_returns(data[:,1])
	print(data)
	print(data[:,1])

if __name__ == '__main__':
	run1()
	#run2()
