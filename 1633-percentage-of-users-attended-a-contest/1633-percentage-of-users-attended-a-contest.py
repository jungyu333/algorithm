import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    
    total_users = len(users)

    df = register.groupby('contest_id').agg(
        cnt = ('user_id', 'count')
    ).reset_index()

    df['percentage'] = round((df['cnt'] / total_users * 100), 2)

    return df[['contest_id', 'percentage']].sort_values(
        by=['percentage', 'contest_id'],
        ascending=[False, True]
    )
