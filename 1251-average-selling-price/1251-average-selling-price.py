import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    merged = prices.merge(units_sold, how='left', on='product_id')
    mask = (
        merged['purchase_date'].between(merged['start_date'], merged['end_date'])
        | merged['purchase_date'].isna()
    )
    df = merged.loc[mask].copy()
    df['revenue'] = df['price'] * df['units']

    result = df.groupby('product_id', as_index=False).agg(
        rev=('revenue', 'sum'),
        qty=('units', 'sum'),
    )

    result['average_price'] = np.where(
        result['qty'] > 0,
        (result['rev'] / result['qty']).round(2),
        0,
    )

    return result[['product_id', 'average_price']]