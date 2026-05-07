import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    
    mask = (activity['activity_date'] >= '2019-06-28') & (activity['activity_date'] <= '2019-07-27')

    df = activity[mask]

    df = df[['user_id', 'activity_date']].drop_duplicates()

    result = df.groupby('activity_date', as_index=False).agg(active_users=('user_id', 'count'))

    result = result.rename(columns={'activity_date':'day'})

    return result