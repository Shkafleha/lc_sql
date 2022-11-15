import pandas as pd
import duckdb

Delivery = {'delivery_id':[1, 2, 3, 4 ,5 ,6 7],
               'customer_id':[1, 2, 1, 3, 3, 2, 4],
               'order_date': ['2019-08-01', '2019-08-02', '2019-08-11', '2019-08-24', '2019-08-21', '2019-08-11', '2019-08-09'],
               'customer_pref_delivery_date': ['2019-08-02', '2019-08-02', '2019-08-12', '2019-08-24', '2019-08-22', '2019-08-13', '2019-08-09'],
               'order_date_num': [1, 2, 4, 6, 5, 4, 3],
               'customer_pref_delivery_date_num': [1, 1, 3, 6, 5, 4, 2]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
