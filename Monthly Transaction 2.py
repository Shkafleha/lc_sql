import pandas as pd
import duckdb

Transactions = {'id'[101, 102, 103, 104, 105],
               'country'["US", "US", "US", "US", "US"],
               'state' ["approved", "declined", "approved", "approved", "approved"],
               'amount' [1000, 2000, 3000, 4000, 5000],
	       'trans_date' ['2019-05-18', '2019-05-19', '2019-06-10', '2019-06-13', '2019-06-15'],
	       'trans_date_num' [1, 2, 3, 4, 5]}

Chargebacks = {'trans_id'[102, 101, 105],
               'trans_date'['2019-05-29', '2019-06-30', '2019-09-18'],
	       'trans_date_num'[1, 2, 3]}

df = pd.DataFrame(data)

qy = select 
        from df
      
print(duckdb.query(qy).df())
