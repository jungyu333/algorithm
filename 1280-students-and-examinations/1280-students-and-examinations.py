import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    base = students.merge(subjects, how='cross')

    exam_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    result = base.merge(exam_count, how='left', on=['student_id', 'subject_name']).reset_index(drop=True)

    result['attended_exams'] = result['attended_exams'].fillna(0)

    result = result[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(['student_id', 'subject_name'])

    return result