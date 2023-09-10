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
        df = pd.read_csv(filename, usecols=selector_rows)
    except FileNotFoundError as err:
        print(f'File {filename} not found: ', err)

    column_index = 0
    for values in selector_values:
        if len(values) > 0:
            data.append(df[df.iloc[:, column_index].isin(values)])
        column_index += 1

    return data



__name__ == '__main__'
data_1 = read_data("dataset_one.csv", ["id", "email", "country"], [[], [], ["United Kingdom", "Netherlands"]])
data_2 = read_data("dataset_two", ["id", "btc_a", "cc_t"], [data_1[0].id, [], []])