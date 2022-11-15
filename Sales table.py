import pandas as pd
import duckdb

Sales = {'sale_id':[1, 2, 7],
               'product_id':[100, 100, 200],
               'year': ['2008', '2009', '2011'],
               'quantity': [10, 12, 15],
	       'price': [5000, 5000, 9000],
	       'year_num': [1, 2, 3]}

Product = {'product_id':[100, 200, 300],
               'product_name':["Nokia", "Apple", "Samsung"]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
