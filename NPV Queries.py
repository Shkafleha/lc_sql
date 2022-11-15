import pandas as pd
import duckdb

NPV = {'id':[1, 7, 13, 1, 2, 3, 11, 7],
               'year':['2018', '2020', '2019', '2019', '2008', '2009', '2020', '2019'],
               'npv': [100, 30, 40, 113, 121, 12, 99, 0],
               'year_num': [3, 5, 4, 4, 1, 2, 5, 4]}

Queries = {'id':[1, 2, 3, 7, 7, 7, 13],
               'year':['2019', '2008', '2009', '2018', '2019', '2020', '2019'],
	       'year_num':[4, 1, 2, 3, 4, 5, 4]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
