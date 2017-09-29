import os
import os.path
import csv
import shutil

PROCESSED_FOLDER_NAME = "processed"
RAW_FOLDER_NAME = "raw"


def processed_csv(dates, detail):
    """  Function is used to write csv to processed folder """

    dirs = [PROCESSED_FOLDER_NAME]
    print (dates)
    print (detail)
    csv_name = dates + "-processed.csv"

    for files in dirs:
        path = os.path.join(files, csv_name)
        f_open = open(path, 'a')
        f_open.write(detail)
        f_open.write("\n")


def open_csv(file_name):
    """  Function to read csv from the raw folder    """

    reader = csv.DictReader(file_name, delimiter=',')
    for line in reader:
        dates = line["date"]
        detail = line["details"]
        processed_csv(dates, detail)


def delete_directory(folder_name):
    """  Function to delete directory  """
    if os.path.exists(os.path.join(os.getcwd(), folder_name)):
        shutil.rmtree(folder_name)


if __name__ == "__main__":
    print "process started"
    directory = [RAW_FOLDER_NAME]
    delete_directory(PROCESSED_FOLDER_NAME)
    os.mkdir(os.path.join(os.getcwd(), PROCESSED_FOLDER_NAME))
    for file in directory:
        for filename in os.listdir(file):
            print (filename)
            with open(os.path.join(file, filename)) as open_raw:
                open_csv(open_raw)
    print "process finished"