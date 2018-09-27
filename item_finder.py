# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 12:39:55 2017

@author: 1399869
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\1399869\Desktop\Products.csv")

#finds an item in the store, returns floor, section, rack
def finder(item):
    
    print("Your item is located at\n")
    print("Floor No : "+df.loc[df['product_name'] == item]["floor_no"].to_string(index = False))
    print("\nSection : "+df.loc[df['product_name'] == item]["section"].to_string(index = False))
    print("\nRack No : "+df.loc[df['product_name'] == item]["rack_no"].to_string(index = False))

    
    
    