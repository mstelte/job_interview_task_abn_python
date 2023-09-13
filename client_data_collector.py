import pandas as pd
import os
import argparse

def read_data(filename, selector_columns: list, selector_values: list):
    '''Take the name of a csv file, a list of columns to be selected, and a list with filter values for each selected column, and return the corresponding rows as a Pandas DataFrame.
    
    filename -- name of the file to be read
    selector_columns -- list of columns to be read
    selector_values -- list of filters to be applied on each read column (must be same length as selector_columns)
    '''
    try:
        len(selector_columns) == len(selector_values)
    except ValueError as err:
        print(f'The number of selector rows ({len(selector_columns)}) does not match the number of selector values ({len(selector_values)}): ', err)
    
    data = pd.DataFrame(columns=selector_columns)
    if '.csv' not in filename:
        filename = filename + '.csv'

    try:
        df = pd.read_csv(filename, usecols=selector_columns)
    except FileNotFoundError as err:
        print(f'File {filename} not found: ', err)

    column_index = 0
    for values in selector_values:
        if len(values) > 0:
            data = pd.concat([data, df[df.iloc[:, column_index].isin(values)]])
        column_index += 1

    return data

def get_params():
    '''Return the user's input parameters as a tuple (file 1, file 2, countries).'''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f1',
        '--file1',
        nargs=1,
        type=str,
        help='Name of the first file to be read.'
    )
    parser.add_argument(
        '-f2',
        '--file2',
        nargs=1,
        type=str,
        help='Name of the second file to be read.'
    )
    parser.add_argument(
        '-c',
        '--countries',
        nargs='*',
        type=str,
        help='List of the relevant countries. Country names with multiple names have to be written with underscore instead of space.'
    )
    args = parser.parse_args()

    countries = [c.replace('_', ' ') for c in args.c]
    return (args.f1[0], args.f2[0], countries)



__name__ == '__main__'
file_1, file_2, countries = get_params()

data_1 = read_data(file_1, ["id", "email", "country"], [[], [], countries])
data_2 = read_data(file_2, ["id", "btc_a", "cc_t"], [data_1['id'].tolist(), [], []])
data_1 = data_1.rename(columns={'id': 'client_identifier'})
data_2 = data_2.rename(columns={'id': 'client_identifier', 'btc_a': 'bitcoin_address', 'cc_t': 'credit_card_type'})
df = pd.merge(data_1, data_2, on='client_identifier')

if not os.path.exists('client_data'):
    os.mkdir('client_data')
df.to_csv('client_data/results.csv', index=False)
