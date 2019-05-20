# Kaggle Dataset Downloader


## About
A `Python` utility that reads a config file and downloads the data for a given competition.


## Getting Started

### 1. Setup Kaggle credentials

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

### 2. Install requirements

* Install Kaggle API:
  ```shell
  pip3 install -r requirements.txt
  ```

### 3. Run

* Give executable permissions
  ```shell
  chmod +x kaggle_dowload.py
  ```
* Execute:
```shell
./kaggle_download.py
```

## Demo

```shell
KaggleDatasetDownloader git:(master) ✗ ./kaggle_download.py
==== Downloading train.csvfrom competition dataset to /home/pseudoaj/github-workspace/KaggleDatasetDownloader/data ... ====
Downloading train.csv to /home/pseudoaj/github-workspace/KaggleDatasetDownloader/data
0%|                                                | 0.00/59.8k [00:00<?, ?B/s]
100%|████████████████████████████████████████| 59.8k/59.8k [00:00<00:00, 719kB/s]
==== Downloading test.csvfrom competition dataset to /home/pseudoaj/github-workspace/KaggleDatasetDownloader/data ... ====
Downloading test.csv to /home/pseudoaj/github-workspace/KaggleDatasetDownloader/data
0%|                                                | 0.00/28.0k [00:00<?, ?B/s]
100%|████████████████████████████████████████| 28.0k/28.0k [00:00<00:00, 785kB/s]
==== Downloading gender_submission.csvfrom competition dataset to /home/pseudoaj/github-workspace/KaggleDatasetDownloader/data ... ====
Downloading gender_submission.csv to /home/pseudoaj/github-workspace/KaggleDatasetDownloader/data
0%|                                                | 0.00/3.18k [00:00<?, ?B/s]
100%|████████████████████████████████████████| 3.18k/3.18k [00:00<00:00, 709kB/s]
```
# Kaggle Dataset process

## About

`pandas` are python package. Pandas Dataframes make manipulation of data easy, from selecting or replacing. In our case Reading file from kaggle_download and write it out reversing the columns and and createa file that contains every other columns.


### Understand the kaggle_procee.py.

Invoke the data from kaggle_download by using pandas function `read_csv()`


# Python flask server 

## About 

Implementing titanic data set in flask server, which performs actions to show file with reverse columns data and every other columns data. 

### Execute 

```shell

python app.py
```

### Demo 

- View at http://localhost:5000   

 Full Data

![Screenshot from 2019-05-20 10-53-50](https://user-images.githubusercontent.com/20710319/58032615-f7d23900-7af0-11e9-86ee-74a63c3527e6.png)

- View at http://localhost:5000/alternate

 Every Other columns Data

![Screenshot from 2019-05-20 10-54-01](https://user-images.githubusercontent.com/20710319/58032781-53042b80-7af1-11e9-9d77-822189d3187d.png)

- View at http://localhost:5000/reverse

 Reverse Data

![Screenshot from 2019-05-20 10-54-20](https://user-images.githubusercontent.com/20710319/58032848-6dd6a000-7af1-11e9-8276-d7b34ed44756.png)


# Yahoo Finance API

## About 

Create a python script that pulls data from the ‘Yahoo Finance API’ calling market get
movers API and creates a xlsx file that you can open in excel.

## Reference

https://blog.rapidapi.com/how-to-use-the-yahoo-finance-api/#python

## Getting Started

### Set up the Account:

- From above refernce link Go to `connect to API`. Sign up to access to Header parameters for Host and key values. 

```shell 
headers={
    		"X-RapidAPI-Host": "put your host",
    		"X-RapidAPI-Key": "put your key",
```


### Execute 

``` shell

python main.py
```

### Demo

In yahoo directory, there are two files that can open in excel. 

![Screenshot from 2019-05-20 11-42-01](https://user-images.githubusercontent.com/20710319/58034380-77153c00-7af4-11e9-9dbc-d87c21de4613.png)




