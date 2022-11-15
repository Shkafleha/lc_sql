import pandas as pd
import duckdb

Candidate = {'id':[1, 2, 3, 4 , 5],
               'Name':["A", "B","C", "D","E"]}

Vote = {'id':[1, 2, 3, 4, 5],
               'CandidateId': [2, 4, 3, 2, 5]}
                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
