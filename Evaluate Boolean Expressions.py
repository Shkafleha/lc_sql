import pandas as pd
import duckdb

Variables = {'name':[x, y],
               'value':[66, 77]}

Expressions table = {'left_operand':[x, x, x, y, y, x],
               'operator':[>, <, =, >, <, =],
               'right_operand': [y, y, y, x, x, x]}

                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
