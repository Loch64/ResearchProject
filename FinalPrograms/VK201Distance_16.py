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
outputDataFileVK201 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK201'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["VK201{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["VK201"+str(i)])):
        distance["VK201"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['VK2011'])
print('YES')
print(distance['VK2012'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZVK201.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZVK201.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZVK201.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZVK201.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceVK201 = np.zeros(len(df1))
saturnDistanceVK201 = np.zeros(len(df2))
uranusDistanceVK201 = np.zeros(len(df3))
neptuneDistanceVK201 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

VK2011Distance = np.zeros(len(distance['VK2011']))
VK2012Distance = np.zeros(len(distance['VK2012']))
VK2013Distance = np.zeros(len(distance['VK2013']))
VK2014Distance = np.zeros(len(distance['VK2014']))
VK2015Distance = np.zeros(len(distance['VK2015']))
VK2016Distance = np.zeros(len(distance['VK2016']))
VK2017Distance = np.zeros(len(distance['VK2017']))
VK2018Distance = np.zeros(len(distance['VK2018']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceVK201[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceVK201[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceVK201[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceVK201[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceVK201[i]
    finalGGData[i,1] = saturnDistanceVK201[i]
    finalGGData[i,2] = uranusDistanceVK201[i]
    finalGGData[i,3] = neptuneDistanceVK201[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['VK2011'])):
    VK2011Distance[i] = distance['VK2011'][i]
    
for i in range(len(distance['VK2012'])):
    VK2012Distance[i] = distance['VK2012'][i]

for i in range(len(distance['VK2013'])):
    VK2013Distance[i] = distance['VK2013'][i]

for i in range(len(distance['VK2014'])):
    VK2014Distance[i] = distance['VK2014'][i]

for i in range(len(distance['VK2015'])):
    VK2015Distance[i] = distance['VK2015'][i]

for i in range(len(distance['VK2016'])):
    VK2016Distance[i] = distance['VK2016'][i]

for i in range(len(distance['VK2017'])):
    VK2017Distance[i] = distance['VK2017'][i]
    
for i in range(len(distance['VK2018'])):
    VK2018Distance[i] = distance['VK2018'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("VK2011Distance.csv", VK2011Distance, delimiter=",")
df = pd.read_csv('VK2011Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2011Distance.csv', index=False) 

np.savetxt("VK2012Distance.csv", VK2012Distance, delimiter=",")
df = pd.read_csv('VK2012Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2012Distance.csv', index=False)

np.savetxt("VK2013Distance.csv", VK2013Distance, delimiter=",")
df = pd.read_csv('VK2013Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2013Distance.csv', index=False)

np.savetxt("VK2014Distance.csv", VK2014Distance, delimiter=",")
df = pd.read_csv('VK2014Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2014Distance.csv', index=False)

np.savetxt("VK2015Distance.csv", VK2015Distance, delimiter=",")
df = pd.read_csv('VK2015Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2015Distance.csv', index=False)

np.savetxt("VK2016Distance.csv", VK2016Distance, delimiter=",")
df = pd.read_csv('VK2016Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2016Distance.csv', index=False)

np.savetxt("VK2017Distance.csv", VK2017Distance, delimiter=",")
df = pd.read_csv('VK2017Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2017Distance.csv', index=False)

np.savetxt("VK2018Distance.csv", VK2018Distance, delimiter=",")
df = pd.read_csv('VK2018Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('VK2018Distance.csv', index=False)

np.savetxt("FinalGGDataVK201.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataVK201.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataVK201.csv', index=False)      
print('Complete 1')
print('Complete 1')


