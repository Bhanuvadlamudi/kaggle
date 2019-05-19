

import pandas as pd

def get_columns():
	data = pd.read_csv('train.csv')
	return data	


def get_columns_reverse():
	data = get_columns()
	columns = data.columns.tolist()
	#print columns
	columns.reverse()
	data = data[columns]
	return data

def get_columns_alternate():
	data = get_columns()
	columns = data.columns.tolist()
	r_columns = []
	for i in range(len(columns)):
		if (i % 2 == 0):
			r_columns.append(columns[i])
	data = data[r_columns]
	return data
	#print columns
	#print r_columns

if __name__ == "__main__": 
	#print get_columns()
	#print get_columns_reverse()
	#print get_columns_alternate()
	data = get_columns()
	obj = data.to_json(orient='records')
	print obj



