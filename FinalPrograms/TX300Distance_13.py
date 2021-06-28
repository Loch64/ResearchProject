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
outputDataFileTX300 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX300'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["TX300{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["TX300"+str(i)])):
        distance["TX300"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['TX3001'])
print('YES')
print(distance['TX3002'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZTX300.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZTX300.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZTX300.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZTX300.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceTX300 = np.zeros(len(df1))
saturnDistanceTX300 = np.zeros(len(df2))
uranusDistanceTX300 = np.zeros(len(df3))
neptuneDistanceTX300 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

TX3001Distance = np.zeros(len(distance['TX3001']))
TX3002Distance = np.zeros(len(distance['TX3002']))
TX3003Distance = np.zeros(len(distance['TX3003']))
TX3004Distance = np.zeros(len(distance['TX3004']))
TX3005Distance = np.zeros(len(distance['TX3005']))
TX3006Distance = np.zeros(len(distance['TX3006']))
TX3007Distance = np.zeros(len(distance['TX3007']))
TX3008Distance = np.zeros(len(distance['TX3008']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceTX300[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceTX300[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceTX300[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceTX300[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceTX300[i]
    finalGGData[i,1] = saturnDistanceTX300[i]
    finalGGData[i,2] = uranusDistanceTX300[i]
    finalGGData[i,3] = neptuneDistanceTX300[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['TX3001'])):
    TX3001Distance[i] = distance['TX3001'][i]
    
for i in range(len(distance['TX3002'])):
    TX3002Distance[i] = distance['TX3002'][i]

for i in range(len(distance['TX3003'])):
    TX3003Distance[i] = distance['TX3003'][i]

for i in range(len(distance['TX3004'])):
    TX3004Distance[i] = distance['TX3004'][i]

for i in range(len(distance['TX3005'])):
    TX3005Distance[i] = distance['TX3005'][i]

for i in range(len(distance['TX3006'])):
    TX3006Distance[i] = distance['TX3006'][i]

for i in range(len(distance['TX3007'])):
    TX3007Distance[i] = distance['TX3007'][i]
    
for i in range(len(distance['TX3008'])):
    TX3008Distance[i] = distance['TX3008'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("TX3001Distance.csv", TX3001Distance, delimiter=",")
df = pd.read_csv('TX3001Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3001Distance.csv', index=False) 

np.savetxt("TX3002Distance.csv", TX3002Distance, delimiter=",")
df = pd.read_csv('TX3002Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3002Distance.csv', index=False)

np.savetxt("TX3003Distance.csv", TX3003Distance, delimiter=",")
df = pd.read_csv('TX3003Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3003Distance.csv', index=False)

np.savetxt("TX3004Distance.csv", TX3004Distance, delimiter=",")
df = pd.read_csv('TX3004Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3004Distance.csv', index=False)

np.savetxt("TX3005Distance.csv", TX3005Distance, delimiter=",")
df = pd.read_csv('TX3005Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3005Distance.csv', index=False)

np.savetxt("TX3006Distance.csv", TX3006Distance, delimiter=",")
df = pd.read_csv('TX3006Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3006Distance.csv', index=False)

np.savetxt("TX3007Distance.csv", TX3007Distance, delimiter=",")
df = pd.read_csv('TX3007Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3007Distance.csv', index=False)

np.savetxt("TX3008Distance.csv", TX3008Distance, delimiter=",")
df = pd.read_csv('TX3008Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TX3008Distance.csv', index=False)

np.savetxt("FinalGGDataTX300.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataTX300.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataTX300.csv', index=False)      
print('Complete 1')
print('Complete 1')


