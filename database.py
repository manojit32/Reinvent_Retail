# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:58:15 2017

@author: 1399869
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('Products.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE Products (
	product_id integer PRIMARY KEY AUTOINCREMENT,
	product_name text,
	price decimal,
	weight decimal,
	pack_time decimal,
	unit_type text,
	picture_url text,
	product_code integer,
	product_count integer,
	floor_no integer,
	section text,
	rack_no integer
	);''')
print "Table created successfully";



df = pd.read_sql("SELECT * from Products",con=conn)
df.to_csv("Products.csv")

conn.close()
