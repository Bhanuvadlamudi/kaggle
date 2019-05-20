# Eclipse

  The folder [Eclipse](https://github.com/Bhanuvadlamudi/kaggle/tree/master/eclipse) contains different files

- HelloWorld.java : Simple java file which prints "Hello World" and invokes a set of methods upon execution
- Execution.png : shows the output in console when the program is run in eclipse.
- exception.png : shows the stack trace when an exception is throw during program execution
- debug.png   : shows how we can run program in debug mode in eclipse and how to use break points to pause the flow of execution 


#Yahoo

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



