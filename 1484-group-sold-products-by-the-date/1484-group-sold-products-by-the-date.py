import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    
    df = activities.drop_duplicates(['sell_date', 'product'])
    df = df.sort_values('product')

    result = df.groupby('sell_date')['product'].agg(
        [('num_sold', 'count'),
         ('products', lambda x: ','.join(x))
        ] 
    ).reset_index()

    return result