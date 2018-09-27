# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:07:00 2017

@author: 1399869
"""

import pandas as pd
import numpy as np
import random
#arbitrarily taking 3 queues for prototype design
#real-time queues will be passed using command line argument 
def generate():
    list1 = random.sample(range(1, 15), 5)
    list2 = random.sample(range(16, 28), 6)
    list3 = random.sample(range(28, 42), 5)
    
    
    df_products = pd.read_csv("Products.csv")
    df_user = pd.read_csv("groceries_2.csv")
    
    
    product1=list()
    product2 = list()
    product3 = list()
    
    
    for i in list1:
        
        product1 +=  df_user.loc[df_user['Person'] == i]["item"].tolist()
    
    for i in list2:
        
        product2 +=  df_user.loc[df_user['Person'] == i]["item"].tolist()
        
    for i in list3:
        
        product3 +=  df_user.loc[df_user['Person'] == i]["item"].tolist()
        
    pack_time1 = 0
    pack_time2 = 0
    pack_time3 = 0    
        
    for item in product1:
        pack_time1 += int(df_products.loc[df_products['product_name'] == item]["pack_time"].to_string(index = False))
       
    for item in product2:
        pack_time2 += int(df_products.loc[df_products['product_name'] == item]["pack_time"].to_string(index = False))
     
     
    for item in product3:
        pack_time3 += int(df_products.loc[df_products['product_name'] == item]["pack_time"].to_string(index = False))
     
    
    
    weight1 = len(product1) * pack_time1
    weight2 = len(product2) * pack_time2
    weight3 = len(product3) * pack_time3
    
    
    weight = np.array([weight1,weight2,weight3])


    
    #print("\nProducts in the first queue :\n")
    #print(product1)
    
    #print("\n\nProducts in the second queue :\n")
    #print(product2)
    
    #print("\n\nProducts in the 3rd queue :\n")
    #print(product3)
        
    
    #print("\n\nYour assigned fastest moving checkout queue is: ")
    print(np.argmin(weight)+1)    
