import pandas as pd
import duckdb

data = {'id':[1, 2, 3, 4, 5],
           'student':["Abbot", "Doris", "Emerson", "Green", "Jeames"]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
