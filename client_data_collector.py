import pandas as pd

def read_data(filename, selector_rows: list, selector_values: list):
    try:
        len(selector_rows) == len(selector_values)
    except ValueError as err:
        print(f'The number of selector rows ({len(selector_rows)}) does not match the number of selector values ({len(selector_values)}): ', err)
    
    data = []

    if '.csv' not in filename:
        filename = filename + '.csv'

    try:
        file_data = pd.read_csv(filename)
    except FileNotFoundError as err:
        print(f'File {filename} not found: ', err)

    

    return data



__name__ == '__main__'
read_data("dataset_one.csv", [], [])