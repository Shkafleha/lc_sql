import pandas as pd
import duckdb

data = {'id':[1, 2, 3, 4, 5, 6, 7],
               'Num':[1, 1, 1, 2, 1, 2, 2]}
               

                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
