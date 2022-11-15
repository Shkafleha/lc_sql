import pandas as pd
import duckdb

Users = {'user_id':[1, 2, 3, 4],
               'join_date':['2018-01-01', '2018-02-09', '2018-01-19', '2018-05-21'],
               'favorite_brand': ["Lenovo", "Samsung", "LG", "HP"],
               'join_date_num': [1, 3, 2, 4]}

Orders = {'order_id':[1, 2, 3, 4, 5, 6],
               'order_date':['2019-08-01', '2018-08-02', '2019-08-03', '2018-08-04', '2018-08-04', '2019-08-05'],
  	       'item_id':[4, 2, 3, 1, 1, 2],
               'buyer_id': [1, 1, 2, 4, 3, 2],
               'seller_id': [2, 3, 3, 2, 4, 4],
	       'order_date_num': [3, 1, 4, 2, 2, 5]}

Items table = {'item_id':[1, 2, 3, 4],
               'item_brand':["Samsung", "Lenovo", "LG", "HP"}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
