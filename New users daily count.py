import pandas as pd
import duckdb

Traffic = {'user_id':[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5],
               'activity':["login", "homepage", "logout", "login", "logout", "login", "jobs", "logout", "login", "groups", "logout", "login", "logout", "login", "logout",],
               'activity_date': ['2019-05-01', '2019-05-01', '2019-05-01', '2019-06-21', '2019-06-21', '2019-01-01', '2019-01-01', '2019-01-01', '2019-06-21', '2019-06-21', '2019-06-21', '2019-03-01', '2019-03-01', '2019-06-21', '2019-06-21',],
               'activity_date_num': [3, 3, 3, 4, 4, 1, 1, 1, 4, 4, 4, 2, 2, 4, 4]}



df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
