import json
import numpy as np
import empyrical as e

def run():

	with open('digicor.json', 'r') as fp:
		raw = json.load(fp)['digicorew']

	data = np.array([[i['date'], i['chgDoD']] for i in raw])
	temp_ = e.cum_returns(data[:,1])
	print(data)
	print(data[:,1])

if __name__ == '__main__':
	run()

