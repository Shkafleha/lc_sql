import pandas as pd
import duckdb

identifier = {'id':[1, 2, 3, 4 , 5],
               'Name':[null, 1, 1, 2, 2]}

result = {'id':[1, 2, 3, 4, 5],
               'Type': ["Leaf", "Leaf", "Leaf", "Leaf", "Leaf"]}
                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
