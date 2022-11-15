import pandas as pd
import duckdb

Sample = {'PID':[1, 2, 3, 4],
               'TIV_2015':[10, 20, 10, 10],
               'TIV_2016': [5, 20, 30, 40],
               'LAT': [10, 20, 20, 40],
	       'LON': [10, 20, 20, 40]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
