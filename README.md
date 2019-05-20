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

`Pandas` are python package. Pandas Dataframes make manipulation of data easy, from selecting or replacing. In our case Reading file from kaggle_download and write it out reversing the columns and and createa file that contains every other columns.


### Understand the kaggle_procee.py.

Invokes the data from kaggle_download by using pandas function `read_csv()`


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

![Screenshot from 2019-05-20 10-53-50](https://user-images.githubusercontent.com/20710319/58035725-64503680-7af7-11e9-8f76-b49c10dfbcb8.png)


- View at http://localhost:5000/alternate

 Every Other columns Data

![Screenshot from 2019-05-20 10-54-01](https://user-images.githubusercontent.com/20710319/58035664-4256b400-7af7-11e9-95f6-f7184800ce4e.png)

- View at http://localhost:5000/reverse

 Reverse Data

![Screenshot from 2019-05-20 10-54-20](https://user-images.githubusercontent.com/20710319/58035607-2521e580-7af7-11e9-818f-b565f8e3f9a8.png)


# Docker Container

# About

Created a Docker container for the flask server created for kaggle data set and deployed in AWS Centos server with Docker installed.

## Getting started 

## Requriments

What you will need:

- AWS Account
- AWS Profile (Note: Do not forget to download csv file)
  * [Instructions](https://blog.gruntwork.io/authenticating-to-aws-with-the-credentials-file-d16c0fbcbf9e) for Authenticating to AWS with the Credentials File.
  
  ![screenshot from 2019-02-13 00-46-02 png](https://user-images.githubusercontent.com/20710319/52690135-a8e19a00-2f2a-11e9-8314-69bd1c7afbf1.png)

- Add Permissions to IAM user

  ![screenshot from 2019-02-05 21-03-58](https://user-images.githubusercontent.com/20710319/52316614-37ce3f80-298a-11e9-9884-073be47d64e3.png)


 - AWS keypairs "Go to EC2 instance - Network and security : keypairs - create a key pair - It downaloads as "example.pem" (make sure pem file is downloaded in the git clonned directory)
 ```
 chmod 400 example.pem
 
 ```

- [Instructions](https://aws.amazon.com/mp/centos/) To launch CentOS in AWS.


## Clonning Git Repo 

``` shell

ssh -i example.pem centos@publicIP

mkdir kaggle     #created a dicrectory

cd kaggle

sudo yum install git

git --version

git clone "https://github.com/Bhanuvadlamudi/kaggle"

```


##Install Docker

```shell
sudo yum install docker

sudo service docker start

```
Include the ec2-user on your docker set and execute the command without having to use sudo. You will need to log out then log in again for this process to apply.

```shell

sudo usermod -a -G docker ec2-user

exit

ssh -i example.pem centos@publicIP

docker info

```


## Install Docker-compose

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version
```


## Execute 

```shell
docker-compose up -d

```





## Handling errors





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



### TODO : logging and error handling

#### Created a hello world application in java and set it up in Eclipse.

![Normal_exe](https://user-images.githubusercontent.com/20710319/58035184-3fa78f00-7af6-11e9-86e4-965619aa4449.png)


#### Force  it to throw and exception

![Exception](https://user-images.githubusercontent.com/20710319/58035293-72ea1e00-7af6-11e9-9bb0-d69c0cbc5b3f.png)

#### setting up a break point in eclipse

![Debug](https://user-images.githubusercontent.com/20710319/58035408-b2186f00-7af6-11e9-93e0-153c933f9ae8.png)





