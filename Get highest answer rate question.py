import pandas as pd
import duckdb

data = {'id':[123, 124, 125, 126],
           'action':["show", "answer", "show", "skip"],
           'question_id': [285, 285, 369, 369],
           'answer_id': [null, 124124, null, null],
	       'q_num': [1, 1, 2, 2],
           'timestamp': [5, 5, 5, 5]}


df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
