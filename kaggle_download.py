
#!/usr/bin/env python3
import kaggle
import os

class KaggleDatasetDownloader():
    # TODO: export these to a YAML based config
    KAGGLE_COMPETITION_NAME = "titanic"
    DOWNLOAD_DIR_RELATIVE_PATH = "data"

    def __init__(self):
        kaggle.api.authenticate()

    def download(self, dataFileName, downloadDirPath):
        try:
            # Setting force = True with override the files in DOWNLOAD_DIR_RELATIVE_PATH by default.
            kaggle.api.competition_download_file(KaggleDatasetDownloader.KAGGLE_COMPETITION_NAME,
                                                 file_name = dataFileName,
                                                 path = downloadDirPath,
                                                 force = True,
                                                 quiet = False)
        except Exception:
            traceback.print_exc()

    def downloadAll(self):
        downloadDirPath = os.path.join(os.getcwd(), KaggleDatasetDownloader.DOWNLOAD_DIR_RELATIVE_PATH)
        
        try:
            # List all the files under a competition and download one by one
            for dataFile in kaggle.api.competition_list_files(KaggleDatasetDownloader.KAGGLE_COMPETITION_NAME):
                dataFileName = str(dataFile)
                print("==== Downloading " + dataFileName + "from competition dataset to " + downloadDirPath + " ... ====")
                self.download(dataFileName, downloadDirPath)
        except Exception:
            traceback.print_exc()

if __name__ == '__main__':
    kaggleDatasetDownloader = KaggleDatasetDownloader()
    kaggleDatasetDownloader.downloadAll()