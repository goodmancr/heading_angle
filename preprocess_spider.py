import pandas as pd
import os


# update dataframe
def preprocess(filepath):
    base_name, _ = os.path.splitext(filepath)
    outfile = base_name + '_angles.csv'

    #load data into dataframe from CSV
    print('Loading ', filepath, "...")
    df = pd.read_csv(filepath, header=None, low_memory=False)
    
    #change header from 3 rows to just one
    new_header = df.iloc[1] +' ' + df.iloc[2]
    df = df[3:]
    df.columns = new_header
    
    #change column title of final row
    df.columns.values[63] = "Spider_Light"
    
    #Get rid of anything outside of 5 minutes (30fps*300seconds)
    df = df.loc[0:9003]
    
    #make it all data that is numeric
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
        
    return df, outfile
