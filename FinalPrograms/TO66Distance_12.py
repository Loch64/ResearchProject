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
outputDataFileTO66 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO66'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["TO66{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["TO66"+str(i)])):
        distance["TO66"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['TO661'])
print('YES')
print(distance['TO662'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZTO66.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZTO66.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZTO66.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZTO66.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceTO66 = np.zeros(len(df1))
saturnDistanceTO66 = np.zeros(len(df2))
uranusDistanceTO66 = np.zeros(len(df3))
neptuneDistanceTO66 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

TO661Distance = np.zeros(len(distance['TO661']))
TO662Distance = np.zeros(len(distance['TO662']))
TO663Distance = np.zeros(len(distance['TO663']))
TO664Distance = np.zeros(len(distance['TO664']))
TO665Distance = np.zeros(len(distance['TO665']))
TO666Distance = np.zeros(len(distance['TO666']))
TO667Distance = np.zeros(len(distance['TO667']))
TO668Distance = np.zeros(len(distance['TO668']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceTO66[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceTO66[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceTO66[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceTO66[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceTO66[i]
    finalGGData[i,1] = saturnDistanceTO66[i]
    finalGGData[i,2] = uranusDistanceTO66[i]
    finalGGData[i,3] = neptuneDistanceTO66[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['TO661'])):
    TO661Distance[i] = distance['TO661'][i]
    
for i in range(len(distance['TO662'])):
    TO662Distance[i] = distance['TO662'][i]

for i in range(len(distance['TO663'])):
    TO663Distance[i] = distance['TO663'][i]

for i in range(len(distance['TO664'])):
    TO664Distance[i] = distance['TO664'][i]

for i in range(len(distance['TO665'])):
    TO665Distance[i] = distance['TO665'][i]

for i in range(len(distance['TO666'])):
    TO666Distance[i] = distance['TO666'][i]

for i in range(len(distance['TO667'])):
    TO667Distance[i] = distance['TO667'][i]
    
for i in range(len(distance['TO668'])):
    TO668Distance[i] = distance['TO668'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("TO661Distance.csv", TO661Distance, delimiter=",")
df = pd.read_csv('TO661Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO661Distance.csv', index=False) 

np.savetxt("TO662Distance.csv", TO662Distance, delimiter=",")
df = pd.read_csv('TO662Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO662Distance.csv', index=False)

np.savetxt("TO663Distance.csv", TO663Distance, delimiter=",")
df = pd.read_csv('TO663Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO663Distance.csv', index=False)

np.savetxt("TO664Distance.csv", TO664Distance, delimiter=",")
df = pd.read_csv('TO664Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO664Distance.csv', index=False)

np.savetxt("TO665Distance.csv", TO665Distance, delimiter=",")
df = pd.read_csv('TO665Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO665Distance.csv', index=False)

np.savetxt("TO666Distance.csv", TO666Distance, delimiter=",")
df = pd.read_csv('TO666Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO666Distance.csv', index=False)

np.savetxt("TO667Distance.csv", TO667Distance, delimiter=",")
df = pd.read_csv('TO667Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO667Distance.csv', index=False)

np.savetxt("TO668Distance.csv", TO668Distance, delimiter=",")
df = pd.read_csv('TO668Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('TO668Distance.csv', index=False)

np.savetxt("FinalGGDataTO66.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataTO66.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataTO66.csv', index=False)      
print('Complete 1')
print('Complete 1')


