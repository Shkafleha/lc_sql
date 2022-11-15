import pandas as pd
import duckdb

Books = {'book_id':[1, 2, 3, 4, 5],
               'student_name':["Kalila And Demna", "28 Letters", "The Hobbit", "13 Reasons Why", "The Hunger Games" ],
               'available_from': ['2010-01-01', '2012-05-12', '2019-06-10', '2019-06-01', '2008-09-21'],
               'available_from_num': [1, 2, 4, 3, 5]}

Orders = {'order_id':[1, 2, 3, 4, 5, 6, 7],
               'book_id':[1, 1, 3, 4, 4, 5, 5],
               'quantity': [2, 1, 8, 6, 5, 9, 8],
               'dispatch_date': ['2018-07-26', '2018-11-05', '2019-06-11', '2019-06-05', '2019-06-20', '2009-02-02', '2010-04-13'],
               'dispatch_date_num': [3, 4, 6, 5, 7, 1, 2]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
