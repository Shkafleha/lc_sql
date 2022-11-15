import pandas as pd
import duckdb

Actions = {'user_id':[1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5],
               'post_id':[1, 1, 1, 2, 2, 4, 4, 3, 3, 2, 2, 5, 5],
               'action_date': ['2019-07-01', '2019-07-01', '2019-07-01', '2019-07-04', '2019-07-04', '2019-07-04', '2019-07-04', '2019-07-02', '2019-07-02', '2019-07-03', '2019-07-03', '2019-07-03', '2019-07-03'],
               'action': ["view", "like", "share", "view", "report", "view", "report", "view", "report", "view", "report", "view", "report"],
	       'extra': ["null", "null", "null", "null", "spam", "null", "spam", "null", "spam", "null", "racism", "null", "racism"],
	       'action_date_num': [1, 1, 1, 4, 4, 4, 4, 2, 2, 3, 3, 3, 3]}

Removals = {'post_idd':[2, 3],
               'remove_date':['2019-07-20', '2019-07-18'],
	       'remove_date':[2, 1]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
