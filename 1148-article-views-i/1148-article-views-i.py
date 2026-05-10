import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    mask = views['author_id'] == views['viewer_id']

    filter_df = views[mask][['author_id']]

    rename = filter_df.rename(columns={'author_id': 'id'})

    sorted = rename.sort_values('id')

    result =sorted.drop_duplicates('id')

    return result