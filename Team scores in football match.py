import pandas as pd
import duckdb

Teams = {'team_id':[10, 20, 30, 40, 50],
               'team_name':["Leetcode FC", "NewYork FC", "Atlanta FC", "Chicago FC", "Toronto FC" ]}

Matches = {'match_id':[1, 2, 3, 4, 5],
               'host_team':[10, 30, 10, 20, 50],
	       'guest_team':[20, 10, 50, 30, 30],
               'host_goals':[3, 2, 5, 1, 1],
               'guest_goals':[0, 2, 1, 0, 0],

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
