import pandas as pd
import duckdb

Input = {'Id':[1, 2, 3],
               'Salary':[100, 200, 300]}



df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
