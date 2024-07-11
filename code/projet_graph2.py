# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:25:01 2023

@author: yassi_4sf0njx
"""

import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
import pygrametl

pgconn = psycopg2.connect(dbname='covid', user='postgres', password='2223111452', port='5433')
connection = pygrametl.ConnectionWrapper(pgconn)
connection.setasdefault()
cursor = pgconn.cursor()
connection.execute('set search_path to "COVID"')
print('Connexion établie')

sql_query = """
    SELECT SUM(c.deaths) AS total_deces, p.continent
    FROM covid19 c
    JOIN pays p ON c.id_pays = p.id_pays
    GROUP BY p.continent
"""
covid_deaths_df = pd.read_sql(sql_query, pgconn)

cursor.close()
connection.close()
pgconn.close()

plt.figure(figsize=(12, 8))
plt.bar(covid_deaths_df['continent'], covid_deaths_df['total_deces'], color='skyblue')
plt.xlabel('Continents')
plt.ylabel('Nombre total de décès')
plt.title('Nombre total de décès par continent')
plt.xticks(rotation=45, ha='right')
plt.show()
