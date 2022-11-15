import pandas as pd
import duckdb

Customers = {'customer_id':[1, 2, 3, 4],
               'customer_name':["Daniel", "Diana", "Elizabeth", "Jhon"]}

Orders = {'order_id':[10, 20, 30, 40, 50, 60, 70, 80, 90],
               'customer_id':[1, 1, 1, 1, 2, 3, 3, 3, 4],
               'product_name':["A", "B", "D", "C", "A", "A", "B", "D", "C",]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
