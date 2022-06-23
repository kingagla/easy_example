import mysql.connector
import pandas as pd
from SQL.settings import user, password

connection = mysql.connector.connect(host='localhost',
                                     database='sales',
                                     user=user,
                                     password=password)

print(connection.is_connected())

query = """select * from production.categories as c
LEFT JOIN production.products as p on c.category_id = p.category_id 
LEFT JOIN sales.order_items as s on s.product_id = p.product_id
UNION 
select * from production.categories as c
RIGHT JOIN production.products as p on c.category_id = p.category_id 
RIGHT JOIN sales.order_items as s on s.product_id = p.product_id
""" # Zawwsze najpierw należy się upewnić w SQL ze nasze zapytanie działa

df = pd.read_sql(query, connection)

connection.close() # zamykamy polaczenie z baza jak mamy juz to co chcemy

print(df)

