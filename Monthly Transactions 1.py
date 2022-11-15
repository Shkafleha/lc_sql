import pandas as pd
import duckdb

Transactions = {'id'[121, 122, 123, 124],
               'country'["US", "US", "US", "US", "DE"],
               'state' ["approved", "declined", "approved", "approved"],
               'amount' [1000, 2000, 2000, 2000],
	       'trans_date' ['2018-12-18', '2018-12-19', '2019-01-01', '2019-01-07'],
	       'trans_date_num' [1, 2, 3, 4]}


df = pd.DataFrame(data)

qy = select 
        from df
      
print(duckdb.query(qy).df())
