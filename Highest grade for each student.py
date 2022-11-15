import pandas as pd
import duckdb

Enrollments = {'student_id':[2, 2, 1, 1, 3, 3, 3,],
               'course_id':[2, 3, 1, 2, 1, 2, 3],
               'grade': [95, 95, 90, 99, 80, 75, 82]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
