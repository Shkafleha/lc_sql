import pandas as pd
import duckdb

Points = {'Id':[101, 102, 103, 104, 105, 106],
               'Name':["John", "Dan", "James", "Amy", "Anne", "Ron"],
               'Department':["A", "A", "A", "A", "A", "B"],
               'ManagerId':[null, 101, 101, 101, 101, 101]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
