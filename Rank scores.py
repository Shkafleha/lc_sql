import pandas as pd
import duckdb

ranks = {'Id':[1, 2, 3, 4 , 5, 6],
               'Score':[3.50, 3.65, 4.00, 3.85, 4.00, 3.65]}

report = {'score':[4.00, 4.00, 3.85, 3.65, 3.65, 3.50],
               'Rank': [1, 1, 2, 3, 3, 4]}
                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
