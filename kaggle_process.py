#!/usr/bin/env python3
import pandas as pd
from kaggle_download import KaggleDatasetDownloader

class kaggle_Process():

	def __init__(self):
		kaggleDatasetDownloader = KaggleDatasetDownloader()
		kaggleDatasetDownloader.downloadAll()

	def get_columns(self):
		data = pd.read_csv('data/train.csv')
		return data	


	def get_columns_reverse(self):
		data = self.get_columns()
		columns = data.columns.tolist()
		#print columns
		columns.reverse()
		data = data[columns]
		return data

	def get_columns_alternate(self):
		data = self.get_columns()
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
	process = kaggle_Process()
	data = process.get_columns()
	obj = data.to_json(orient='records')
	print (obj)



