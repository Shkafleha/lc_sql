import pandas as pd
import duckdb

request_accepted = {'requester_id':[1, 1, 2, 3],
               'accepter_id':[2, 3, 3, 4],
               'accept_date':['2016_06-03', '2016-06-08', '2016-06-08', '2016-06-09'],
               'accept_date_num':[1, 2, 2, 3]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
