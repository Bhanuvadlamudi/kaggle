# Eclipse

The folder [Eclipse](https://github.com/Bhanuvadlamudi/kaggle/tree/master/eclipse) contains different files

- HelloWorld.java : Simple java file which prints "Hello World" and invokes a set of methods upon execution
- Execution.png : shows the output in console when the program is run in eclipse.
- exception.png : shows the stack trace when an exception is throw during program execution
- debug.png   : shows how we can run program in debug mode in eclipse and how to use break points to pause the flow of execution 


# Yahoo

## About 

In [Yahoo](https://github.com/Bhanuvadlamudi/kaggle/tree/master/yahoo) folder a python script that pulls data from the ‘Yahoo Finance API’ calling market get
movers API and creates a xlsx file that you can open in excel.

## Reference

https://blog.rapidapi.com/how-to-use-the-yahoo-finance-api/#python

## Getting Started

### Set up the Account:

- From above refernce link Go to `connect to API`. Sign up to access to Header parameters for Host and key values. 

- In [yahoo.py](https://github.com/Bhanuvadlamudi/kaggle/blob/master/yahoo/yahoo.py) add host and key values (line 12,13)

```shell 
headers={
    		"X-RapidAPI-Host": "put your host",
    		"X-RapidAPI-Key": "put your key",

```

### Execute 

By executing the program, `main.py`  it creates a excel file in yahoo directory which consits of markets and quotes response data 

``` shell

python main.py
```

![Screenshot from 2019-05-20 11-42-01](https://user-images.githubusercontent.com/20710319/58034380-77153c00-7af4-11e9-9dbc-d87c21de4613.png)



#Kaggle

## About

A python [script](https://github.com/Bhanuvadlamudi/kaggle/blob/master/kaggle_download)script that reads the titanic data set from kaggle and performs a [file](https://github.com/Bhanuvadlamudi/kaggle/blob/master/kaggle_process.py) that contains reverse coloumns, every other columns and implemented in flask server that hosts the data set in locally and dockerized the flask application and deployed docker container in AWS CentOs.  

### Getting started 

### Setup Kaggle credentials

* Go to kaggle account here: `https://www.kaggle.com/<YOUR_ALIAS>/account`
* Click on `Create New API Token` under `API`
* Move the file
  ```shell
  # Assuming you are in ~/Downloads
  mv kaggle.json ~/.kaggle/kaggle.json
  ```
* Set the permissions
  ```shell
  chmod 600 ~/.kaggle/kaggle.json
  ```
 - Install requirements

* Install Kaggle API:
  ```shell
  pip3 install -r requirements.txt
  ```

* Give executable permissions

  ```shell
  chmod +x kaggle_dowload.py
  ```
 

### Run the app

```shell
python app.py
```
we can see your `app.py` flask application running on http://localhost:5000/.

- View at http://localhost:5000   

 Full Data

![Screenshot from 2019-05-20 10-53-50](https://user-images.githubusercontent.com/20710319/58035725-64503680-7af7-11e9-8f76-b49c10dfbcb8.png)


- View at http://localhost:5000/alternate

 Every Other columns Data

![Screenshot from 2019-05-20 10-54-01](https://user-images.githubusercontent.com/20710319/58035664-4256b400-7af7-11e9-95f6-f7184800ce4e.png)

- View at http://localhost:5000/reverse

 Reverse Data

![Screenshot from 2019-05-20 10-54-20](https://user-images.githubusercontent.com/20710319/58035607-2521e580-7af7-11e9-818f-b565f8e3f9a8.png)



