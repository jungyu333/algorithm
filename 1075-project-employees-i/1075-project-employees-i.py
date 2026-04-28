import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
    merge_df = pd.merge(project, employee, on='employee_id', how='inner')

    result = merge_df.groupby('project_id', as_index=False)['experience_years'].mean()

    result = result.rename(columns={'experience_years': 'average_years'})

    result['average_years'] = result['average_years'].round(2)

    return result