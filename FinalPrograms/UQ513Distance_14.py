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
outputDataFileUQ513 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ513'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["UQ513{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["UQ513"+str(i)])):
        distance["UQ513"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['UQ5131'])
print('YES')
print(distance['UQ5132'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZUQ513.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZUQ513.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZUQ513.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZUQ513.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceUQ513 = np.zeros(len(df1))
saturnDistanceUQ513 = np.zeros(len(df2))
uranusDistanceUQ513 = np.zeros(len(df3))
neptuneDistanceUQ513 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

UQ5131Distance = np.zeros(len(distance['UQ5131']))
UQ5132Distance = np.zeros(len(distance['UQ5132']))
UQ5133Distance = np.zeros(len(distance['UQ5133']))
UQ5134Distance = np.zeros(len(distance['UQ5134']))
UQ5135Distance = np.zeros(len(distance['UQ5135']))
UQ5136Distance = np.zeros(len(distance['UQ5136']))
UQ5137Distance = np.zeros(len(distance['UQ5137']))
UQ5138Distance = np.zeros(len(distance['UQ5138']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceUQ513[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceUQ513[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceUQ513[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceUQ513[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceUQ513[i]
    finalGGData[i,1] = saturnDistanceUQ513[i]
    finalGGData[i,2] = uranusDistanceUQ513[i]
    finalGGData[i,3] = neptuneDistanceUQ513[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['UQ5131'])):
    UQ5131Distance[i] = distance['UQ5131'][i]
    
for i in range(len(distance['UQ5132'])):
    UQ5132Distance[i] = distance['UQ5132'][i]

for i in range(len(distance['UQ5133'])):
    UQ5133Distance[i] = distance['UQ5133'][i]

for i in range(len(distance['UQ5134'])):
    UQ5134Distance[i] = distance['UQ5134'][i]

for i in range(len(distance['UQ5135'])):
    UQ5135Distance[i] = distance['UQ5135'][i]

for i in range(len(distance['UQ5136'])):
    UQ5136Distance[i] = distance['UQ5136'][i]

for i in range(len(distance['UQ5137'])):
    UQ5137Distance[i] = distance['UQ5137'][i]
    
for i in range(len(distance['UQ5138'])):
    UQ5138Distance[i] = distance['UQ5138'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("UQ5131Distance.csv", UQ5131Distance, delimiter=",")
df = pd.read_csv('UQ5131Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5131Distance.csv', index=False) 

np.savetxt("UQ5132Distance.csv", UQ5132Distance, delimiter=",")
df = pd.read_csv('UQ5132Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5132Distance.csv', index=False)

np.savetxt("UQ5133Distance.csv", UQ5133Distance, delimiter=",")
df = pd.read_csv('UQ5133Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5133Distance.csv', index=False)

np.savetxt("UQ5134Distance.csv", UQ5134Distance, delimiter=",")
df = pd.read_csv('UQ5134Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5134Distance.csv', index=False)

np.savetxt("UQ5135Distance.csv", UQ5135Distance, delimiter=",")
df = pd.read_csv('UQ5135Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5135Distance.csv', index=False)

np.savetxt("UQ5136Distance.csv", UQ5136Distance, delimiter=",")
df = pd.read_csv('UQ5136Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5136Distance.csv', index=False)

np.savetxt("UQ5137Distance.csv", UQ5137Distance, delimiter=",")
df = pd.read_csv('UQ5137Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5137Distance.csv', index=False)

np.savetxt("UQ5138Distance.csv", UQ5138Distance, delimiter=",")
df = pd.read_csv('UQ5138Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UQ5138Distance.csv', index=False)

np.savetxt("FinalGGDataUQ513.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataUQ513.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataUQ513.csv', index=False)      
print('Complete 1')
print('Complete 1')


