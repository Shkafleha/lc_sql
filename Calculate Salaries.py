rt pandas as pd
import duckdb

Salaries = {'company_id':[1, 1, 1, 2, 2, 2, 3, 3, 3, 3],
               'employee_id':[1, 2, 3, 1, 7, 9, 7, 2, 13, 15],
               'employee_name': ["Tony", "Pronub", "Tyrrox", "Pam", "Bassem", "Hermione", "Bocaben", "Ognjen", "Nyancat", "Morninngcat"],
               'salary': [2000, 21300, 100800, 300, 450, 700, 100, 2200, 3300, 1866]}
                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
