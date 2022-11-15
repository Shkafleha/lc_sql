import pandas as pd
import duckdb

Stocks = {'stock_name':["Leetcode", "Corona Masks", "Leetcode", "Handbags", "Corona Masks", "Corona Masks", "Corona Masks", "Corona Masks", "Handbags", "Corona Masks"],
               'operation':["Buy", "Buy","Sell", "Buy","Sell", "Buy", "Sell", "Buy", "Sell", "Sell"],
               'operation_day': [1, 2, 5, 17, 3, 4, 5, 6, 29, 10],
               'price': [1000, 10, 9000, 30000, 1010, 1000, 500, 1000, 7000, 10000]}

                
df = pd.DataFrame(data)

qy = """select *
        from df"""
      
print(duckdb.query(qy).df())
