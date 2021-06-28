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
outputDataFileSQ317 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ317'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["SQ317{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["SQ317"+str(i)])):
        distance["SQ317"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['SQ3171'])
print('YES')
print(distance['SQ3172'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZSQ317.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZSQ317.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZSQ317.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZSQ317.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceSQ317 = np.zeros(len(df1))
saturnDistanceSQ317 = np.zeros(len(df2))
uranusDistanceSQ317 = np.zeros(len(df3))
neptuneDistanceSQ317 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

SQ3171Distance = np.zeros(len(distance['SQ3171']))
SQ3172Distance = np.zeros(len(distance['SQ3172']))
SQ3173Distance = np.zeros(len(distance['SQ3173']))
SQ3174Distance = np.zeros(len(distance['SQ3174']))
SQ3175Distance = np.zeros(len(distance['SQ3175']))
SQ3176Distance = np.zeros(len(distance['SQ3176']))
SQ3177Distance = np.zeros(len(distance['SQ3177']))
SQ3178Distance = np.zeros(len(distance['SQ3178']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceSQ317[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceSQ317[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceSQ317[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceSQ317[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceSQ317[i]
    finalGGData[i,1] = saturnDistanceSQ317[i]
    finalGGData[i,2] = uranusDistanceSQ317[i]
    finalGGData[i,3] = neptuneDistanceSQ317[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['SQ3171'])):
    SQ3171Distance[i] = distance['SQ3171'][i]
    
for i in range(len(distance['SQ3172'])):
    SQ3172Distance[i] = distance['SQ3172'][i]

for i in range(len(distance['SQ3173'])):
    SQ3173Distance[i] = distance['SQ3173'][i]

for i in range(len(distance['SQ3174'])):
    SQ3174Distance[i] = distance['SQ3174'][i]

for i in range(len(distance['SQ3175'])):
    SQ3175Distance[i] = distance['SQ3175'][i]

for i in range(len(distance['SQ3176'])):
    SQ3176Distance[i] = distance['SQ3176'][i]

for i in range(len(distance['SQ3177'])):
    SQ3177Distance[i] = distance['SQ3177'][i]
    
for i in range(len(distance['SQ3178'])):
    SQ3178Distance[i] = distance['SQ3178'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("SQ3171Distance.csv", SQ3171Distance, delimiter=",")
df = pd.read_csv('SQ3171Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3171Distance.csv', index=False) 

np.savetxt("SQ3172Distance.csv", SQ3172Distance, delimiter=",")
df = pd.read_csv('SQ3172Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3172Distance.csv', index=False)

np.savetxt("SQ3173Distance.csv", SQ3173Distance, delimiter=",")
df = pd.read_csv('SQ3173Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3173Distance.csv', index=False)

np.savetxt("SQ3174Distance.csv", SQ3174Distance, delimiter=",")
df = pd.read_csv('SQ3174Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3174Distance.csv', index=False)

np.savetxt("SQ3175Distance.csv", SQ3175Distance, delimiter=",")
df = pd.read_csv('SQ3175Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3175Distance.csv', index=False)

np.savetxt("SQ3176Distance.csv", SQ3176Distance, delimiter=",")
df = pd.read_csv('SQ3176Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3176Distance.csv', index=False)

np.savetxt("SQ3177Distance.csv", SQ3177Distance, delimiter=",")
df = pd.read_csv('SQ3177Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3177Distance.csv', index=False)

np.savetxt("SQ3178Distance.csv", SQ3178Distance, delimiter=",")
df = pd.read_csv('SQ3178Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SQ3178Distance.csv', index=False)

np.savetxt("FinalGGDataSQ317.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataSQ317.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataSQ317.csv', index=False)      
print('Complete 1')
print('Complete 1')


