#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
import os

PATH = './USQHPCResultsAndPrograms/FINALGGDATA'

fileNames = os.listdir(PATH)

filenames = [file for file in fileNames if '.csv' in file]

for file in fileNames:
    newfile = open(PATH+'/'+file)
    data = np.loadtxt(newfile, delimiter=",", skiprows=1)
    newData = np.zeros(180000*4).reshape(180000, 4)
    for i in range(180000):
        newData[i,0] = data[i,0]
        newData[i,1] = data[i,1]
        newData[i,2] = data[i,2]
        newData[i,3] = (i+1)*25000
    np.savetxt(PATH+'/'+file, newData, delimiter=",")
    df = pd.read_csv(PATH+'/'+file, header=None)
    df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 't'}, inplace=True)
    df['t'] = df['t'].astype(np.int)
    df.to_csv(PATH+'/'+file, index=False)
    
print("Finished")

