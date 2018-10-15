import pandas as pd
import numpy as np
#Reading data 
file=r'multipleChoiceResponses.csv'
data  = pd.read_csv(file,encoding = "ISO-8859-1",low_memory=False) #Reading the data file
#print (data.columns)   # to make sure data is loaded correctly



x = pd.DataFrame(0, index=np.arange(len(data)), columns=['label'])

idx = 0
for i in data.CurrentJobTitleSelect:
    
    if i==4:
        x.iloc[idx] = 1
    idx+=1

data['label']=x

data.to_csv('final.csv')