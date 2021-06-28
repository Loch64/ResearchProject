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
outputDataFileAP129 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP129'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["AP129{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["AP129"+str(i)])):
        distance["AP129"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['AP1291'])
print('YES')
print(distance['AP1292'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZAP129.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZAP129.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZAP129.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZAP129.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceAP129 = np.zeros(len(df1))
saturnDistanceAP129 = np.zeros(len(df2))
uranusDistanceAP129 = np.zeros(len(df3))
neptuneDistanceAP129 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

AP1291Distance = np.zeros(len(distance['AP1291']))
AP1292Distance = np.zeros(len(distance['AP1292']))
AP1293Distance = np.zeros(len(distance['AP1293']))
AP1294Distance = np.zeros(len(distance['AP1294']))
AP1295Distance = np.zeros(len(distance['AP1295']))
AP1296Distance = np.zeros(len(distance['AP1296']))
AP1297Distance = np.zeros(len(distance['AP1297']))
AP1298Distance = np.zeros(len(distance['AP1298']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceAP129[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceAP129[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceAP129[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceAP129[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceAP129[i]
    finalGGData[i,1] = saturnDistanceAP129[i]
    finalGGData[i,2] = uranusDistanceAP129[i]
    finalGGData[i,3] = neptuneDistanceAP129[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['AP1291'])):
    AP1291Distance[i] = distance['AP1291'][i]
    
for i in range(len(distance['AP1292'])):
    AP1292Distance[i] = distance['AP1292'][i]

for i in range(len(distance['AP1293'])):
    AP1293Distance[i] = distance['AP1293'][i]

for i in range(len(distance['AP1294'])):
    AP1294Distance[i] = distance['AP1294'][i]

for i in range(len(distance['AP1295'])):
    AP1295Distance[i] = distance['AP1295'][i]

for i in range(len(distance['AP1296'])):
    AP1296Distance[i] = distance['AP1296'][i]

for i in range(len(distance['AP1297'])):
    AP1297Distance[i] = distance['AP1297'][i]
    
for i in range(len(distance['AP1298'])):
    AP1298Distance[i] = distance['AP1298'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("AP1291Distance.csv", AP1291Distance, delimiter=",")
df = pd.read_csv('AP1291Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1291Distance.csv', index=False) 

np.savetxt("AP1292Distance.csv", AP1292Distance, delimiter=",")
df = pd.read_csv('AP1292Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1292Distance.csv', index=False)

np.savetxt("AP1293Distance.csv", AP1293Distance, delimiter=",")
df = pd.read_csv('AP1293Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1293Distance.csv', index=False)

np.savetxt("AP1294Distance.csv", AP1294Distance, delimiter=",")
df = pd.read_csv('AP1294Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1294Distance.csv', index=False)

np.savetxt("AP1295Distance.csv", AP1295Distance, delimiter=",")
df = pd.read_csv('AP1295Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1295Distance.csv', index=False)

np.savetxt("AP1296Distance.csv", AP1296Distance, delimiter=",")
df = pd.read_csv('AP1296Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1296Distance.csv', index=False)

np.savetxt("AP1297Distance.csv", AP1297Distance, delimiter=",")
df = pd.read_csv('AP1297Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1297Distance.csv', index=False)

np.savetxt("AP1298Distance.csv", AP1298Distance, delimiter=",")
df = pd.read_csv('AP1298Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AP1298Distance.csv', index=False)

np.savetxt("FinalGGDataAP129.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataAP129.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataAP129.csv', index=False)      
print('Complete 1')
print('Complete 1')

    

