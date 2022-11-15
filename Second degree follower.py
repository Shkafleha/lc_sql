import pandas as pd
import duckdb

followee = {'followee':["A", "B", "B", "D"],
               'follower':["B", "C", "D", "E"]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
