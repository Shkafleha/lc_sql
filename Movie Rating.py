import pandas as pd
import duckdb

Movies = {'movie_id':[1, 2, 3],
               'title':["Avengers", "Frozen 2", "Joker"]}

Users = {'user_id':[1, 2, 3, 4],
               'dept_name':["Daniel", "Monica", "Maria", "James"]}

Movie_Rating = {'movie_id':[1, 1, 1, 1, 2, 2, 2, 3, 3],
               'user_id':[1, 2, 3, 4, 1, 2, 3, 1, 2],
               'rating': [3, 4, 2, 1, 5, 2, 2, 3, 4],
               'created_at': ['2020-01-12', '2020-02-11', '2020-02-12', '2020-01-01', '2020-02-17', '2020-02-01', '2020-03-01', '2020-02-22', '2020-02-25'],
	       'created_at_num': [2, 4, 5, 1, 6, 3, 9, 7, 8]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
