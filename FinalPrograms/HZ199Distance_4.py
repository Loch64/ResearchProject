#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

objects = {}
orbits = {}
distance = {}
outputDataFileHZ199 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ199'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["HZ199{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["HZ199"+str(i)])):
        distance["HZ199"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['HZ1991'])
print('YES')
print(distance['HZ1992'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHZ199.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHZ199.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHZ199.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHZ199.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceHZ199 = np.zeros(len(df1))
saturnDistanceHZ199 = np.zeros(len(df2))
uranusDistanceHZ199 = np.zeros(len(df3))
neptuneDistanceHZ199 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

HZ1991Distance = np.zeros(len(distance['HZ1991']))
HZ1992Distance = np.zeros(len(distance['HZ1992']))
HZ1993Distance = np.zeros(len(distance['HZ1993']))
HZ1994Distance = np.zeros(len(distance['HZ1994']))
HZ1995Distance = np.zeros(len(distance['HZ1995']))
HZ1996Distance = np.zeros(len(distance['HZ1996']))
HZ1997Distance = np.zeros(len(distance['HZ1997']))
HZ1998Distance = np.zeros(len(distance['HZ1998']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceHZ199[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceHZ199[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceHZ199[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceHZ199[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceHZ199[i]
    finalGGData[i,1] = saturnDistanceHZ199[i]
    finalGGData[i,2] = uranusDistanceHZ199[i]
    finalGGData[i,3] = neptuneDistanceHZ199[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['HZ1991'])):
    HZ1991Distance[i] = distance['HZ1991'][i]
    
for i in range(len(distance['HZ1992'])):
    HZ1992Distance[i] = distance['HZ1992'][i]

for i in range(len(distance['HZ1993'])):
    HZ1993Distance[i] = distance['HZ1993'][i]

for i in range(len(distance['HZ1994'])):
    HZ1994Distance[i] = distance['HZ1994'][i]

for i in range(len(distance['HZ1995'])):
    HZ1995Distance[i] = distance['HZ1995'][i]

for i in range(len(distance['HZ1996'])):
    HZ1996Distance[i] = distance['HZ1996'][i]

for i in range(len(distance['HZ1997'])):
    HZ1997Distance[i] = distance['HZ1997'][i]
    
for i in range(len(distance['HZ1998'])):
    HZ1998Distance[i] = distance['HZ1998'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("HZ1991Distance.csv", HZ1991Distance, delimiter=",")
df = pd.read_csv('HZ1991Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1991Distance.csv', index=False) 

np.savetxt("HZ1992Distance.csv", HZ1992Distance, delimiter=",")
df = pd.read_csv('HZ1992Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1992Distance.csv', index=False)

np.savetxt("HZ1993Distance.csv", HZ1993Distance, delimiter=",")
df = pd.read_csv('HZ1993Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1993Distance.csv', index=False)

np.savetxt("HZ1994Distance.csv", HZ1994Distance, delimiter=",")
df = pd.read_csv('HZ1994Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1994Distance.csv', index=False)

np.savetxt("HZ1995Distance.csv", HZ1995Distance, delimiter=",")
df = pd.read_csv('HZ1995Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1995Distance.csv', index=False)

np.savetxt("HZ1996Distance.csv", HZ1996Distance, delimiter=",")
df = pd.read_csv('HZ1996Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1996Distance.csv', index=False)

np.savetxt("HZ1997Distance.csv", HZ1997Distance, delimiter=",")
df = pd.read_csv('HZ1997Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1997Distance.csv', index=False)

np.savetxt("HZ1998Distance.csv", HZ1998Distance, delimiter=",")
df = pd.read_csv('HZ1998Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('HZ1998Distance.csv', index=False)

np.savetxt("FinalGGDataHZ199.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataHZ199.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataHZ199.csv', index=False)      
print('Complete 1')
print('Complete 1')


