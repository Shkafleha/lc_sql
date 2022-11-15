import pandas as pd
import duckdb

Scores = {'player_name':["Aron", "Alice", "Bajrang", "Khali","Slaman", "Joe", "Jose", "Priya", "Priyanka"],
               'gender':["F", "F", "M", "M", "M", "M", "M", "F", "F"],
               'day': ['2020-01-01', '2020-01-07', '2020-01-07', '2019-12-25', '2019-12-30', '2019-12-31', '2019-12-18', '2019-12-31', '2019-12-30'],
               'score_points': [17, 23, 7, 11, 13, 3, 2, 23, 17],
	       'day_num': [5, 6, 6, 2, 3, 4, 1, 4, 3]}

df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
