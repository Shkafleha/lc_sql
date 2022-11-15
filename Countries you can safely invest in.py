import pandas as pd
import duckdb

Person = {'id':[3, 12, 1, 2, 7, 9],
               'name':["Jonathan", "Elvis", "Moncef", "Maroua", "Meir", "Rachel"],
               'phone_number': [051-1234567, 051-7654321, 212-1234567,'212-6523651, 972-1234567, 972-0011100]}

Country = {'name':["Peru", "Israil", "Morocco", "Germany", "Ethiopia"],
               'country_code':[051, 972, 212, 049, 251]}

Calls = {'caller_id':[1, 2, 1, 3, 3, 12, 7, 7, 9, 1],
               'callee_id':[9, 9, 2, 12, 12, 3, 9, 1, 7, 7],
               'duration': [33, 4, 59, 102, 330, 5, 13, 3, 1, 7]}

                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
