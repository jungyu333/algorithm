import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    merge_df = orders.merge(products, how='inner', on=['product_id'])

    date_filter = merge_df['order_date'].between('2020-02-01', '2020-02-29')

    filtered_df = merge_df[date_filter]

    grouped_df = filtered_df.groupby(['product_id', 'product_name'])['unit'].sum().reset_index()

    result = grouped_df[grouped_df['unit'] >= 100]

    return result[['product_name', 'unit']]