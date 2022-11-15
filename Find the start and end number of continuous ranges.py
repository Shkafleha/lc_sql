import pandas as pd
import duckdb

Logs = {'log_id':[1, 2, 3, 7, 8, 10]}

                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
