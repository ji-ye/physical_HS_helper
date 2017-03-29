# Functions to import json file to database

import json
import pandas
import re


def json_to_df(filepath):
    '''
    Create a pandas dataframe for sql import from a cards json file.
    If the card is not collectible, mark its collectible column with value zero.

    Input:
        filepath: (string) json file path

    Return:
        df: (pandas dataframe object)
    '''
    df = pandas.read_json(filepath)
    df.collectible = df.collectible.fillna(value=0)
    return df

def create_csv_name(filepath):
    '''
    Create the csv output filename from cards json path.

    Input: (string) json file path

    Return: (string)
    '''
    pattern = '[\w-]+\.'
    csv_name = re.findall(pattern, filepath)[0] + 'csv'
    return csv_name




if __name__ == "__main__":
    cards_enUS_path = "./cards_json_v17994/cards_enUS.json"
    cards_zhCN_path = "./cards_json_v17994/cards_zhCN.json"

    df_en = json_to_df(cards_enUS_path)
    df_zh = json_to_df(cards_zhCN_path)

    csv_name_enUS = create_csv_name(cards_enUS_path)
    csv_name_zhCN = create_csv_name(cards_zhCN_path)

    # output pandas dataframe to csv
    df_en.to_csv(csv_name_enUS, header=False)
    df_zh.to_csv(csv_name_zhCN, header=False)
