import pandas as pd
import duckdb

Sales = {'sale_date':['2020-05-01', '2020-05-01', '2020-05-02', '2020-05-02', '2020-05-03', '2020-05-03', '2020-05-04', '2020-05-04'],
               'fruit':["apples", "oranges", "apples", "oranges", "apples", "oranges", "apples", "oranges"],
               'sold_num': [10, 8, 15, 15, 20, 0, 15, 16],
               'sale_date_num': [1, 1, 2, 2, 3, 3, 4, 4],}
                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
