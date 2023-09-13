import pandas as pd

def read_data(filename, selector_rows: list, selector_values: list):
    try:
        len(selector_rows) == len(selector_values)
    except ValueError as err:
        print(f'The number of selector rows ({len(selector_rows)}) does not match the number of selector values ({len(selector_values)}): ', err)
    
    data = pd.DataFrame(columns=selector_rows)
    if '.csv' not in filename:
        filename = filename + '.csv'

    try:
        df = pd.read_csv(filename, usecols=selector_rows)
    except FileNotFoundError as err:
        print(f'File {filename} not found: ', err)

    column_index = 0
    for values in selector_values:
        if len(values) > 0:
            data = pd.concat([data, df[df.iloc[:, column_index].isin(values)]])
        column_index += 1

    return data



__name__ == '__main__'
data_1 = read_data("dataset_one.csv", ["id", "email", "country"], [[], [], ["United Kingdom", "Netherlands"]])
data_2 = read_data("dataset_two", ["id", "btc_a", "cc_t"], [data_1['id'].tolist(), [], []])
data_1.rename(columns={'id': 'client_identifier'})
data_2.rename(columns={'id': 'client_identifier', 'btc_a': 'bitcoin_address', 'cc_t': 'credit_card_type'})
df = pd.merge(data_1, data_2, on='client_identifier')
df.to_csv('results.csv', index=False)
