import pandas as pd
import duckdb

department = {'Id':[1, 2, 3, 4 , 5],
               'Name':["Joe", "Jim","Henry", "Sam","Max"],
               'Salary': [70000, 90000, 80000, 60000, 90000],
               'DepartmentId': [1, 1, 2, 2, 1]}
company = {'Id':[1, 2],
               'DepartmentId': ["IT", "Sales"]}
                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
