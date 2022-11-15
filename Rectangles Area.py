import pandas as pd
import duckdb

Points = {'id':[1, 2, 3],
               'x_value':[2, 4, 2],
               'y_value':[8, 7, 10]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
