import pandas as pd
import duckdb

student = {'student_id':[1, 2, 3],
               'student_name':["Jack", "Jane", "Mark"],
               'gender': ["M", "F", "M"],
               'dept_id': [1, 1, 2]}

department = {'dept_id':[1, 2, 3],
               'dept_name':["Engineering", "Science", "Law"]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
