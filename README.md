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

$ python main.py
```

![Screenshot from 2019-05-20 11-42-01](https://user-images.githubusercontent.com/20710319/58034380-77153c00-7af4-11e9-9dbc-d87c21de4613.png)



# Kaggle

**Goal:** The goal of this project is to create an flask application which will read the "titanic" data set from kaggle site and expose three endpoints which renders the data in tabular form (entire data, data with alternate columns, data with columns in reverse order). There are three ways you can run the flask application:

### Getting started

 Three are the following procedures

1. **Running the flask app as a simple python program in local machine.**

- Install git 
```
$ apt-get install git
```
- clone git repository
```shell
$ git clone "https://github.com/Bhanuvadlamudi/kaggle"
```
- Setup Kaggle credentials:

* Go to kaggle account here: `https://www.kaggle.com/<YOUR_ALIAS>/account`
* Click on `Create New API Token` under `API`
* Move the file
  ```shell
  # Assuming you are in ~/Downloads
  mv kaggle.json ~/.kaggle/kaggle.json
  ```
* Set the permissions
  ```shell
  $ chmod 600 ~/.kaggle/kaggle.json
  ```

* Install Kaggle API:
  ```shell
  $ pip3 install -r requirements.txt
  ```

* Give executable permissions

  ```shell
  $ chmod +x kaggle_dowload.py
  ```
 
### Run the app

```shell
$ python app.py
```
we can see  `app.py` flask application running on http://localhost:5000/.

- View at http://localhost:5000   (Full Data)
 
![Screenshot from 2019-05-20 10-53-50](https://user-images.githubusercontent.com/20710319/58035725-64503680-7af7-11e9-8f76-b49c10dfbcb8.png)


- View at http://localhost:5000/alternate   (Every Other columns Data)

![Screenshot from 2019-05-20 10-54-01](https://user-images.githubusercontent.com/20710319/58035664-4256b400-7af7-11e9-95f6-f7184800ce4e.png)

- View at http://localhost:5000/reverse (Reverse Data)

![Screenshot from 2019-05-20 10-54-20](https://user-images.githubusercontent.com/20710319/58035607-2521e580-7af7-11e9-818f-b565f8e3f9a8.png)


2. **Running the flask app from Step#1 in a docker container. A second container with nginx serves as a reverse proxy. Both the docker containers are created using docker-compose and run on local machine.**

Configured nginx to reverse proxy to flask application.

- Run
``` shell
$ docker-compose up -d  

Creating flask ... done
Creating nginx ... done


$ docker ps -a    #shows the running containers 

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
2cf5febc3b87        nginx:latest        "nginx -g 'daemon of…"   5 minutes ago       Up 5 minutes        0.0.0.0:8080->80/tcp     nginx
3a7e695886c5        kaggle_flask        "./app.py"               5 minutes ago       Up 5 minutes        0.0.0.0:5000->5000/tcp   flask


```
- we can see our flask application on http://localhost:8080 

![Screenshot from 2019-05-20 16-10-21](https://user-images.githubusercontent.com/20710319/58049061-f23d1900-7b19-11e9-8eee-7d4727aa1496.png)

Note: since we listed flask as a dependency in nginx container, docker-compose first starts the flask container for us and then nginx. This works for a chain of such dependencies.


- Stop the running containers

```

$ docker stop nginx flask    # stops the running containers

bhanu@bhanu-Inspiron-15-7579:~/Documents/ezops/kaggle$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
2cf5febc3b87        nginx:latest        "nginx -g 'daemon of…"   18 minutes ago      Exited (0) 10 seconds ago                       nginx
3a7e695886c5        kaggle_flask        "./app.py"               18 minutes ago      Exited (0) 10 seconds ago                       flask


$ docker rm <containername>    #deletes the containers
```
- Handling errors:

while executing `docker-compose up -d` there might be a inetrnal errror 

solution : `service docker start`  or delete the old images by `docker images` #shows the docker images
`docker rmi -f image_name` # deletes the images



3. **Hosting the dockers created in step 2, in AWS EC2 CentOS server instead of local machine**

What you will need:

- AWS Account
- AWS Profile (Note: Do not forget to download csv file)
  * [Instructions](https://blog.gruntwork.io/authenticating-to-aws-with-the-credentials-file-d16c0fbcbf9e) for Authenticating to AWS with the Credentials File.
  
  ![screenshot from 2019-02-13 00-46-02 png](https://user-images.githubusercontent.com/20710319/52690135-a8e19a00-2f2a-11e9-8314-69bd1c7afbf1.png)

- Add Permissions to IAM user

  ![screenshot from 2019-02-05 21-03-58](https://user-images.githubusercontent.com/20710319/52316614-37ce3f80-298a-11e9-9884-073be47d64e3.png)


 - AWS keypairs "Go to EC2 instance - Network and security : keypairs - create a key pair - It downaloads as "example.pem" (make sure pem file is downloaded in the git clonned directory)
 ```
 $ chmod 400 example.pem
 
 ```

- [Instructions](https://aws.amazon.com/mp/centos/) To launch CentOS in AWS.
```shell
$ ssh -i example.pem centos@publicIP
```

- Clonning Git Repo 

``` shell

$ mkdir kaggle     #created a dicrectory

$ cd kaggle

$ sudo yum install git

$ git --version

$ git clone "https://github.com/Bhanuvadlamudi/kaggle"

```


- Install Docker

```shell
$ sudo yum install docker

$ sudo service docker start

```
Include the ec2-user on your docker set and execute the command without having to use sudo. You will need to log out then log in again for this process to apply.

```shell

$ sudo usermod -a -G docker ec2-user

$ exit

$ ssh -i example.pem centos@publicIP

$ docker info

```

- Install Docker-compose

```
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

$ sudo chmod +x /usr/local/bin/docker-compose

$ docker-compose --version
```

- Execute 

```shell
$ docker-compose up -d


$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
5f67e3000c89        nginx:latest        "nginx -g 'daemon ..."   41 minutes ago      Up 41 minutes       0.0.0.0:8080->80/tcp     nginx
03aa328eed34        kaggle_flask        "./app.py"               41 minutes ago      Up 41 minutes   

```
Finally, you visit your instance public DNS name:8080 in your browser, you should see something like this below 

![Screenshot from 2019-05-20 17-31-27](https://user-images.githubusercontent.com/20710319/58053539-d475b100-7b25-11e9-8784-73befd5cdf7c.png)

 - Handling errors:

 https://stackoverflow.com/questions/34532696/docker-compose-cant-connect-to-docker-daemon

 Reference:

 https://hackernoon.com/running-docker-on-aws-ec2-83a14b780c56

 https://www.matthealy.com.au/blog/post/deploying-flask-to-amazon-web-services-ec2/



