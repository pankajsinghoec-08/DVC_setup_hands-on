## read params to fetch data from
## process data
## return dataframe

import os
import yaml
import pandas as pd
import argparse                         # To pass the argument from the command prompt

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
        return config

def get_data(config_path):              # function to get the data
    config = read_params(config_path)   # read configuration from the configuration path
    # print (config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=',', encoding='utf-8')
    #print(df.head())
    return df
    
# Creating main which is an entrance point for this project
if __name__=="__main__":
    # importing ArgumentParser class from the argparse package
    args = argparse.ArgumentParser()
    # There are two arguments being paassed from the terminal
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)



