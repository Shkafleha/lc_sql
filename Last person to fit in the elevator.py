import pandas as pd
import duckdb

student = {'person_id':[5, 3, 6, 2, 4, 1],
               'person_name':["George Washington", "John Adams", "Thomas Jefferson", "Will Johnliams", "Thomas Jefferson", "James Elephant"],
               'weight': [250, 350, 400, 200, 175, 500],
               'turn': [1, 2, 3, 4, 5 ,6]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
