import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    merge_df = users.merge(transactions, how='inner', on='account')

    agg_df = merge_df.groupby(['account','name']).agg(
        balance = ('amount', 'sum')
    ).reset_index()

    result = agg_df[agg_df['balance'] > 10000]

    return result[['name', 'balance']]