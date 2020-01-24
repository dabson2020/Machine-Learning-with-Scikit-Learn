import psycopg2
import pandas as pd
import numpy as np

conn = psycopg2.connect(database = 'dvdrental', use = 'postgres',password = '********')
cur = conn.cursor()
cur.execute('SELECT table_name FROM information_schema.tables where table_schema = 'public';')
for table in cur.fetchall():
	print (table)

# To print the content of table above in a dataframe
for instance, we want to print the actor_info table
query = cur.execute(SELECT " FROM actor_info;")
data = cur.fetchall()
df = pd.DataFrame([i for i in data])
