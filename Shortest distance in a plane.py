import pandas as pd
import duckdb

points = {'x':[-1, 0, -1],
               'y':[-1, 0, -2]}
               

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
