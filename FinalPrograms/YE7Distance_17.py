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
outputDataFileYE7 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE7'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["YE7{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["YE7"+str(i)])):
        distance["YE7"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['YE71'])
print('YES')
print(distance['YE72'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZYE7.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZYE7.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZYE7.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZYE7.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceYE7 = np.zeros(len(df1))
saturnDistanceYE7 = np.zeros(len(df2))
uranusDistanceYE7 = np.zeros(len(df3))
neptuneDistanceYE7 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

YE71Distance = np.zeros(len(distance['YE71']))
YE72Distance = np.zeros(len(distance['YE72']))
YE73Distance = np.zeros(len(distance['YE73']))
YE74Distance = np.zeros(len(distance['YE74']))
YE75Distance = np.zeros(len(distance['YE75']))
YE76Distance = np.zeros(len(distance['YE76']))
YE77Distance = np.zeros(len(distance['YE77']))
YE78Distance = np.zeros(len(distance['YE78']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceYE7[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceYE7[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceYE7[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceYE7[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceYE7[i]
    finalGGData[i,1] = saturnDistanceYE7[i]
    finalGGData[i,2] = uranusDistanceYE7[i]
    finalGGData[i,3] = neptuneDistanceYE7[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['YE71'])):
    YE71Distance[i] = distance['YE71'][i]
    
for i in range(len(distance['YE72'])):
    YE72Distance[i] = distance['YE72'][i]

for i in range(len(distance['YE73'])):
    YE73Distance[i] = distance['YE73'][i]

for i in range(len(distance['YE74'])):
    YE74Distance[i] = distance['YE74'][i]

for i in range(len(distance['YE75'])):
    YE75Distance[i] = distance['YE75'][i]

for i in range(len(distance['YE76'])):
    YE76Distance[i] = distance['YE76'][i]

for i in range(len(distance['YE77'])):
    YE77Distance[i] = distance['YE77'][i]
    
for i in range(len(distance['YE78'])):
    YE78Distance[i] = distance['YE78'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("YE71Distance.csv", YE71Distance, delimiter=",")
df = pd.read_csv('YE71Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE71Distance.csv', index=False) 

np.savetxt("YE72Distance.csv", YE72Distance, delimiter=",")
df = pd.read_csv('YE72Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE72Distance.csv', index=False)

np.savetxt("YE73Distance.csv", YE73Distance, delimiter=",")
df = pd.read_csv('YE73Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE73Distance.csv', index=False)

np.savetxt("YE74Distance.csv", YE74Distance, delimiter=",")
df = pd.read_csv('YE74Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE74Distance.csv', index=False)

np.savetxt("YE75Distance.csv", YE75Distance, delimiter=",")
df = pd.read_csv('YE75Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE75Distance.csv', index=False)

np.savetxt("YE76Distance.csv", YE76Distance, delimiter=",")
df = pd.read_csv('YE76Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE76Distance.csv', index=False)

np.savetxt("YE77Distance.csv", YE77Distance, delimiter=",")
df = pd.read_csv('YE77Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE77Distance.csv', index=False)

np.savetxt("YE78Distance.csv", YE78Distance, delimiter=",")
df = pd.read_csv('YE78Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('YE78Distance.csv', index=False)

np.savetxt("FinalGGDataYE7.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataYE7.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataYE7.csv', index=False)      
print('Complete 1')
print('Complete 1')


