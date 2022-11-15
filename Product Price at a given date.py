import pandas as pd
import duckdb

Products = {'product_id':[1, 2, 1, 1, 2, 3],
               'new_price':[20, 50, 30, 35, 65, 20],
               'change_date': ['2019-08-14', '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-17', '2019-08-18'],
               'change_date_num': [1, 1, 2, 3, 4, 5]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
