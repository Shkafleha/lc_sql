import pandas as pd
import duckdb

Project  = {'project_id':[1, 1, 1, 2, 2],
               'employee_id':[1, 2, 3, 1, 4]}

Employee = {'employee_id':[1, 2, 3, 4],
               'name':["Khalled", "Ali", "John", "Doe"],
	       'experience_years':[3, 2, 3, 2]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
