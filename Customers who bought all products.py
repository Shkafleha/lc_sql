import pandas as pd
import duckdb

Customer = {'customer_id':[1, 2, 3, 3, 1],
               'product_key':[5, 6, 5, 6, 6]}

Product = {'product_key':[5, 6]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
