#!/usr/bin/env python3

from flask import Flask, render_template
from kaggle_process import kaggle_Process

app = Flask(__name__)
kaggle = kaggle_Process()
#https://stackoverflow.com/questions/49964340/getting-flask-json-response-as-an-html-table

@app.route('/', methods =['GET'])
def get_data():
	data = kaggle.get_columns()
	obj = data.to_dict('records')
	columnNames = data.columns.values
	return render_template('record.html', records=obj, colnames=columnNames)


@app.route('/alternate', methods =['GET'])
def get_alternate():
	data = kaggle.get_columns_alternate()
	obj = data.to_dict('records')
	columnNames = data.columns.values
	return render_template('record.html', records=obj, colnames=columnNames)

   

@app.route('/reverse', methods =['GET'])
def get_reverse():
	data = kaggle.get_columns_reverse()
	obj = data.to_dict('records')
	columnNames = data.columns.values
	return render_template('record.html', records=obj, colnames=columnNames)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask