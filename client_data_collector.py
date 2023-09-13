import pandas as pd

__name__ == '__main__'
data_1 = pd.DataFrame
data_2 = pd.DataFrame
data_1.rename(columns={'id': 'client_identifier'})
data_2.rename(columns={'id': 'client_identifier', 'btc_a': 'bitcoin_address', 'cc_t': 'credit_card_type'})
df = pd.merge(data_1, data_2, on='client_identifier')
df.to_csv('results.csv', index=False)