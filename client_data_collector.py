import pandas as pd

def write_data(data_1, data_2, key, file_name):
    df = pd.merge(data_1, data_2, on=key)
    df.to_csv(file_name, index=False)

__name__ == '__main__'
data_1 = pd.DataFrame
data_2 = pd.DataFrame
data_1.rename(columns={'id': 'client_identifier'})
data_2.rename(columns={'id': 'client_identifier', 'btc_a': 'bitcoin_address', 'cc_t': 'credit_card_type'})
write_data(data_1, data_2, 'client_identifier', 'results.csv')