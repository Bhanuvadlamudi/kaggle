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

