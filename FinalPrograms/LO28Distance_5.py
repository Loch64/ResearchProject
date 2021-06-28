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
outputDataFileLO28 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO28'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["LO28{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["LO28"+str(i)])):
        distance["LO28"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['LO281'])
print('YES')
print(distance['LO282'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZLO28.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZLO28.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZLO28.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZLO28.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceLO28 = np.zeros(len(df1))
saturnDistanceLO28 = np.zeros(len(df2))
uranusDistanceLO28 = np.zeros(len(df3))
neptuneDistanceLO28 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

LO281Distance = np.zeros(len(distance['LO281']))
LO282Distance = np.zeros(len(distance['LO282']))
LO283Distance = np.zeros(len(distance['LO283']))
LO284Distance = np.zeros(len(distance['LO284']))
LO285Distance = np.zeros(len(distance['LO285']))
LO286Distance = np.zeros(len(distance['LO286']))
LO287Distance = np.zeros(len(distance['LO287']))
LO288Distance = np.zeros(len(distance['LO288']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceLO28[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceLO28[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceLO28[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceLO28[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceLO28[i]
    finalGGData[i,1] = saturnDistanceLO28[i]
    finalGGData[i,2] = uranusDistanceLO28[i]
    finalGGData[i,3] = neptuneDistanceLO28[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['LO281'])):
    LO281Distance[i] = distance['LO281'][i]
    
for i in range(len(distance['LO282'])):
    LO282Distance[i] = distance['LO282'][i]

for i in range(len(distance['LO283'])):
    LO283Distance[i] = distance['LO283'][i]

for i in range(len(distance['LO284'])):
    LO284Distance[i] = distance['LO284'][i]

for i in range(len(distance['LO285'])):
    LO285Distance[i] = distance['LO285'][i]

for i in range(len(distance['LO286'])):
    LO286Distance[i] = distance['LO286'][i]

for i in range(len(distance['LO287'])):
    LO287Distance[i] = distance['LO287'][i]
    
for i in range(len(distance['LO288'])):
    LO288Distance[i] = distance['LO288'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("LO281Distance.csv", LO281Distance, delimiter=",")
df = pd.read_csv('LO281Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO281Distance.csv', index=False) 

np.savetxt("LO282Distance.csv", LO282Distance, delimiter=",")
df = pd.read_csv('LO282Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO282Distance.csv', index=False)

np.savetxt("LO283Distance.csv", LO283Distance, delimiter=",")
df = pd.read_csv('LO283Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO283Distance.csv', index=False)

np.savetxt("LO284Distance.csv", LO284Distance, delimiter=",")
df = pd.read_csv('LO284Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO284Distance.csv', index=False)

np.savetxt("LO285Distance.csv", LO285Distance, delimiter=",")
df = pd.read_csv('LO285Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO285Distance.csv', index=False)

np.savetxt("LO286Distance.csv", LO286Distance, delimiter=",")
df = pd.read_csv('LO286Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO286Distance.csv', index=False)

np.savetxt("LO287Distance.csv", LO287Distance, delimiter=",")
df = pd.read_csv('LO287Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO287Distance.csv', index=False)

np.savetxt("LO288Distance.csv", LO288Distance, delimiter=",")
df = pd.read_csv('LO288Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('LO288Distance.csv', index=False)

np.savetxt("FinalGGDataLO28.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataLO28.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataLO28.csv', index=False)      
print('Complete 1')
print('Complete 1')

