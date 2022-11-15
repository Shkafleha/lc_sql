import pandas as pd
import duckdb

Activity = {'player_id':[1, 1, 1, 3, 3],
               'device_id':[2, 2, 3, 1, 4],
               'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
               'games_played': [5, 6, 1, 0, 5],
	       'event_date_num': [1, 3, 4, 2, 5]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
