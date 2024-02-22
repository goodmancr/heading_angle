import pandas as pd
import os
from tqdm import tqdm
from calculate_angles import *
from preprocess_spider import *


def spider_mouse_heading():
    path_to_folder = input("Path to folder with DLC Excel files: ")
    os.chdir(path_to_folder)
    for filepath in os.listdir():
        if filepath.endswith('.csv'):
            
            # load and preprocess data
            df, outfile = preprocess(filepath)

            # calculate and update data
            df = calculating_angles(df)

            # save data to outfile
            df.to_csv(outfile)

if __name__ == '__main__':
    print("Make sure all DLC files are in one folder location")
    spider_mouse_heading()
