# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:37:01 2017

@author: Manojit Chakraborty
"""

#Import libraries
import pandas as pd
from scipy.spatial.distance import cosine

#Helper function to get similarity scores
def getScore(history, similarities):
   return sum(history*similarities)/sum(similarities)

   

def item_based(data_neighbours,item):
    
                
    str = data_neighbours.loc[item][1:].head(5).to_string(index=False)
    str = str.replace('\n',' ')
    str =str.replace('    ','')
    str = str.replace(' ',', ')
    print("Now You can try these items : \n\n"+str)
    
    
    
    
def user_based(dataWide,data_neighbours,data_ibs,data_ib,userid):
    data_sims1 = dataWide.reset_index()
    # Create a place holder matrix for similarities, and fill in the user name column
    data_sims = pd.DataFrame(index=data_sims1.index,columns=data_sims1.columns)
    data_sims.ix[:,:1] = data_sims1.ix[:,:1]
    data_sims12 = data_sims1.iloc[:50,:]
    data_sims11 = data_sims.iloc[:50,:]
    for i in range(0,len(data_sims11.index)):
        for j in range(1,len(data_sims11.columns)):
            user = data_sims11.index[i]
            product = data_sims11.columns[j]
 
            if data_sims12.ix[i][j] == 1:
                data_sims11.ix[i][j] = 0
            else:
                product_top_names = data_neighbours.ix[product][1:10]
                product_top_sims = data_ibs.ix[product].sort_values(ascending=False)[1:10]
                user_purchases = data_ib.ix[user,product_top_names]
            
                #print (i)
                #print (j)
 
                data_sims11.ix[i][j] = getScore(user_purchases,product_top_sims)
                
    # Get the top products
    data_recommend = pd.DataFrame(index=data_sims.index, columns=['Person','1','2','3','4','5','6'])
    data_recommend.ix[0:,0] = data_sims.ix[:,0]
    # Instead of top product scores, we want to see names
    for i in range(0,len(data_sims.index)):
        data_recommend.ix[i,1:] = data_sims.ix[i,:].sort_values(ascending=False).ix[1:7,].index.transpose()
    # Print a sample
    print("Based on your previous shoppings, these are the items you can buy : \n\n")
    print(data_recommend.ix[userid-1:userid-1,:4].drop("Person",axis=1).to_string(index=False,header=False))


def main():
    
    data = pd.read_csv("groceries_2.csv")
    #Assume that for all items only one quantity was bought 
    data["Quantity"] = 1
    
    itemarray = pd.unique(data.item)
    #This particular view isn't very helpful for us for analysis.
    #This way of data being arranged is called LONG
    #We need it in wide format
    #Converting data from long to wide format
    dataWide = data.pivot("Person", "item", "Quantity")
    #Replace NA with 0 
    dataWide.fillna(0, inplace=True)
    #Drop the Person column
    data_ib = dataWide.copy()
    data_ib = data_ib.reset_index()
    #Drop the Person column
    #data_ib = data_ib.iloc[:,1:]
    data_ib = data_ib.drop("Person", axis=1)
    # Create a placeholder dataframe listing item vs. item
    data_ibs = pd.DataFrame(index=data_ib.columns, columns=data_ib.columns)
    for i in range(0,len(data_ibs.columns)) :
        # Loop through the columns for each column
        for j in range(0,len(data_ibs.columns)) :
            # Fill in placeholder with cosine similarities
            data_ibs.ix[i,j] = 1-cosine(data_ib.ix[:,i],data_ib.ix[:,j])
            
    data_neighbours = pd.DataFrame(index=data_ibs.columns,columns=range(1,11))
            
    # Loop through our similarity dataframe and fill in neighbouring item names
    for i in range(0,len(data_ibs.columns)):
            data_neighbours.ix[i,:10] = data_ibs.ix[0:,i].sort_values(ascending=False)[:10].index
    print("Hello, Welcome to ABCD Store\n\n")
    print("Here are some trending products ::\n\n")
    print(data['item'].value_counts().head(5))
    userid = input("Tell me your UserID : ")
    
    user_based(dataWide,data_neighbours,data_ibs,data_ib,int(userid))
    item = input("Give an item you want to add to the cart : ")
    item_based(data_neighbours,item)
    

if __name__ == "__main__":
    main()
    
                        