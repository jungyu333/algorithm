import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    merge = visits.merge(transactions, how='left', on='visit_id')

    none_transactions = merge[merge['transaction_id'].isna()]

    result = none_transactions.groupby('customer_id').agg(
        count_no_trans=('visit_id', 'count')
    ).reset_index()

    return result