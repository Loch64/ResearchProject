#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import os

PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest'

fileNames = os.listdir(PATH)

filenames = [file for file in fileNames if '.csv' in file]
num = 0

for file in fileNames:
    count = 0
    dataDeleted = 0
    newfile = open(PATH+'/'+file)
    print(PATH+'/'+file)
    data = np.loadtxt(newfile, delimiter=",", skiprows=1) #encoding="utf-8"
    newData = np.zeros(180000*7).reshape(180000, 7)
    for i in range(180000):
        if data[i,5]>1 and count==0 and dataDeleted==0:
            newData[i,0] = data[i,0]
            newData[i,1] = data[i,1]
            newData[i,2] = data[i,2]
            newData[i,3] = data[i,3]
            newData[i,4] = data[i,4]
            newData[i,5] = data[i,5]
            newData[i,6] = data[i,6]
            count += 1
        elif data[i,5]>1 and count!=0 and dataDeleted==0:
            newData = np.delete(newData, [i,179999], axis=0)
            dataDeleted += 1
            break
        elif count==0 and dataDeleted==0:
            newData[i,0] = data[i,0]
            newData[i,1] = data[i,1]
            newData[i,2] = data[i,2]
            newData[i,3] = data[i,3]
            newData[i,4] = data[i,4]
            newData[i,5] = data[i,5]
            newData[i,6] = data[i,6]
    np.savetxt(PATH+'/'+file, newData, delimiter=",")
    df = pd.read_csv(PATH+'/'+file, header=None)
    df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e', 6: 't'}, inplace=True)
    df['t'] = df['t'].astype(np.int)
    df.to_csv(PATH+'/'+file, index=False)
    num += 1
    print(num)

    
print("Finished")

