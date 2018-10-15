'''
The final output should be the columns converted into codes.
For example if column contains one of three values: (Yes/No/Not Sure) for example,
this code should replace Yes->0 and No->1 and Not Sure->2 ... and so on.

The idea here is to find the unique items by passing through the column values
and next make an ID for each item, finally replace the value with its corresponding
ID.

'''

import pandas as pd
#Reading data 
file=r'multipleChoiceResponses.csv'

data  = pd.read_csv(file,encoding = "ISO-8859-1",low_memory=False) #Reading the data file
#print (data.columns)   # to make sure data is loaded correctly

#modified_data DataFrame should have the same structure of data DataFrame.
mod_data = pd.DataFrame().reindex_like(data)


#d_s = {}

for column in data:  #looping through columns
    q = data[column]  #data of that column in data DF
    x = mod_data[column] #data of that column in modified_data DF

    d={}  #Dictionary to hold IDs
    
    c=1  #counter
    #res=[]

    for i in q:  #passing through column values
        if pd.isnull(i):  #if Null -> do nothing
            continue
        if i not in d:  #If item is not added to unique items in the columns
            d[i]=c   #add it
            c+=1     #assign an ID
    #d_s[column] = d  

    # now passing through modified data to replace   
    idx=0
    clmn_idx=0
    for i in q:
        if i in d:
            x.iloc[idx] = d[i]
        idx+=1

#final data is here!! but not complete :( let's take a look at the next code to make labels!
mod_data.to_csv('final.csv')