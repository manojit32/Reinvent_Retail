# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:57:59 2017

@author: 1399869
"""

import recomm
print("Hello, Welcome to ABCD Store\n\n")

import json
from pprint import pprint
with open('data.json') as data_file:    
    data = json.load(data_file)

    if(data["maps"][0]["id"]==1):
        recomm.trending()
        print("\n\n")
    elif(data["maps"][0]["id"]==2):
        item = input("enter item name :: ")
        recomm.item_based(data["maps"][0]["value"])
        print("\n\n")
    
    elif(data["maps"][0]["id"]==3) :
        userid=int(input("enter userid :: "))
        recomm.user_based(data["maps"][0]["value"])
        print("\n\n")
 