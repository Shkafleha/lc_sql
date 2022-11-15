import pandas as pd
import duckdb

UserActivity = {'username':["Alice", "Alice", "Alice", "Bob"],
               'activity':["Travel", "Dancing", "Travel", "Travel"],
               'startDate': ['2020-02-12', '2020-02-21', '2020-02-24', '2020-02-11'],
               'endDate': ['2020-02-20', '2020-02-23', '2020-02-28', '2020-02-18'],
	       'startDate_num': [1, 3, 4, 2],
	       'endDate_num': [1, 3, 4, 2]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
