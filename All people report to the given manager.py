import pandas as pd
import duckdb

Employees = {'employee_id':[1, 3, 2, 4, 7, 8, 9, 77],
                   'employee_name':["Boss", "Alice", "Bob", "Daniel", "Luis", "Jhon", "Angela", "Robert"],
                   'manager_id': [1, 3, 1, 2, 4, 3, 8, 1]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
