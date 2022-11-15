import pandas as pd
import duckdb

request_accepted = {'customer_id':[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3],
               'name':["Jhon", "Daniel", "Jade", "Khaled", "Winston", "Elvis", "Anna", "Maria", "Jaze", "Jhon", "Jade"],
               'visited_on':['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08', '2019-01-09', '2019-01-10', '2019-01-10'],
               'amount':[100, 110, 120, 130, 110, 140, 150, 80, 110, 130, 150],
               'visited_on_num':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
