# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:17:36 2023

@author: yassi_4sf0njx
"""

import psycopg2
import pygrametl
from pygrametl.datasources import CSVSource
from pygrametl.tables import Dimension, FactTable


pgconn = psycopg2.connect(dbname='covid',user='postgres', password='2223111452', port='5433')
connection = pygrametl.ConnectionWrapper(pgconn)
connection.setasdefault()
connection.execute('set search_path to "COVID"')
print('connection établie')

covid_file = open('covid_data.csv', 'r')
covid_source= CSVSource(covid_file, delimiter=',')
print('lecture du fichier réussi')

date_dimension = Dimension(
name='date',
key='id_date',
attributes=['annee','mois','jours'])

pays_dimension = Dimension(
name='pays',
key='id_pays',
attributes=['nom_pays','geold','code_pays','pays_pop','continent'])

covid19_Fact = FactTable(
name='covid19',
keyrefs=['id_pays','id_date'],
measures=['nb_cas','deaths','cum_num'])


for row in covid_source :
    row['id_pays']=row['continentExp']+row['countriesAndTerritories']
    row['nom_pays'] = row['countriesAndTerritories']
    row['geold'] = row['geoId']
    row['code_pays'] = row['countryterritoryCode']
    row['pays_pop'] = row['popData2019']
    row['continent'] =row['continentExp']
    row['id_pays'] = pays_dimension.ensure(row)


    row['id_date']=row['dateRep']
    row['annee'] = row['year']
    row['mois'] = row['month']
    row['jours'] = row['day']
    row['id_date'] = date_dimension.ensure(row)


    row['nb_cas']=pygrametl.getfloat(row['cases'])
    row['deaths']= pygrametl.getfloat(row['deaths'])
    row['cum_num']=pygrametl.getfloat(row['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'])
    covid19_Fact.ensure(row)

connection.commit()
connection.close()
print('ETL réalisé avec succès')

#Finally the connection to the sales database is closed
pgconn.close()
