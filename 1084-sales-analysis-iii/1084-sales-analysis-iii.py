import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    merged = product.merge(sales, on='product_id', how='inner')

    grouped = merged.groupby('product_id').agg(
        product_name=('product_name', 'first'),
        min_date=('sale_date', 'min'),
        max_date=('sale_date', 'max'),
    ).reset_index()

    result = grouped[
        (grouped['min_date'] >= '2019-01-01') &
        (grouped['max_date'] <= '2019-03-31')
    ]

    return result[['product_id', 'product_name']]