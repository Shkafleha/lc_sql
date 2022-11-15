import pandas as pd
import duckdb

Friendship = {'user1_id':[1, 1, 1, 2, 2, 2, 6],
               'user2_id':[2, 3, 4, 3, 4, 5, 1]}

Likes = {'user_id':[1, 2, 3, 4, 5, 6, 2, 3, 6],
               'page_id':[88, 23, 24, 56, 11, 33, 77, 77, 88]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
