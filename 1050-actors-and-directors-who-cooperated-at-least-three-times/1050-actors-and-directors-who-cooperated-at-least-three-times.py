import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    group = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count') 
    
    result = group[group['count'] >= 3][['actor_id', 'director_id']]

    return result