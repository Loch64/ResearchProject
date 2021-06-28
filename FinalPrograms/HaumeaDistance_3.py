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
outputDataFileHaumea = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["Haumea{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["Haumea"+str(i)])):
        distance["Haumea"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['Haumea1'])
print('YES')
print(distance['Haumea2'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHaumea.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHaumea.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHaumea.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHaumea.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceHaumea = np.zeros(len(df1))
saturnDistanceHaumea = np.zeros(len(df2))
uranusDistanceHaumea = np.zeros(len(df3))
neptuneDistanceHaumea = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

Haumea1Distance = np.zeros(len(distance['Haumea1']))
Haumea2Distance = np.zeros(len(distance['Haumea2']))
Haumea3Distance = np.zeros(len(distance['Haumea3']))
Haumea4Distance = np.zeros(len(distance['Haumea4']))
Haumea5Distance = np.zeros(len(distance['Haumea5']))
Haumea6Distance = np.zeros(len(distance['Haumea6']))
Haumea7Distance = np.zeros(len(distance['Haumea7']))
Haumea8Distance = np.zeros(len(distance['Haumea8']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceHaumea[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceHaumea[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceHaumea[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceHaumea[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceHaumea[i]
    finalGGData[i,1] = saturnDistanceHaumea[i]
    finalGGData[i,2] = uranusDistanceHaumea[i]
    finalGGData[i,3] = neptuneDistanceHaumea[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['Haumea1'])):
    Haumea1Distance[i] = distance['Haumea1'][i]
    
for i in range(len(distance['Haumea2'])):
    Haumea2Distance[i] = distance['Haumea2'][i]

for i in range(len(distance['Haumea3'])):
    Haumea3Distance[i] = distance['Haumea3'][i]

for i in range(len(distance['Haumea4'])):
    Haumea4Distance[i] = distance['Haumea4'][i]

for i in range(len(distance['Haumea5'])):
    Haumea5Distance[i] = distance['Haumea5'][i]

for i in range(len(distance['Haumea6'])):
    Haumea6Distance[i] = distance['Haumea6'][i]

for i in range(len(distance['Haumea7'])):
    Haumea7Distance[i] = distance['Haumea7'][i]
    
for i in range(len(distance['Haumea8'])):
    Haumea8Distance[i] = distance['Haumea8'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("Haumea1Distance.csv", Haumea1Distance, delimiter=",")
df = pd.read_csv('Haumea1Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea1Distance.csv', index=False) 

np.savetxt("Haumea2Distance.csv", Haumea2Distance, delimiter=",")
df = pd.read_csv('Haumea2Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea2Distance.csv', index=False)

np.savetxt("Haumea3Distance.csv", Haumea3Distance, delimiter=",")
df = pd.read_csv('Haumea3Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea3Distance.csv', index=False)

np.savetxt("Haumea4Distance.csv", Haumea4Distance, delimiter=",")
df = pd.read_csv('Haumea4Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea4Distance.csv', index=False)

np.savetxt("Haumea5Distance.csv", Haumea5Distance, delimiter=",")
df = pd.read_csv('Haumea5Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea5Distance.csv', index=False)

np.savetxt("Haumea6Distance.csv", Haumea6Distance, delimiter=",")
df = pd.read_csv('Haumea6Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea6Distance.csv', index=False)

np.savetxt("Haumea7Distance.csv", Haumea7Distance, delimiter=",")
df = pd.read_csv('Haumea7Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea7Distance.csv', index=False)

np.savetxt("Haumea8Distance.csv", Haumea8Distance, delimiter=",")
df = pd.read_csv('Haumea8Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('Haumea8Distance.csv', index=False)

np.savetxt("FinalGGDataHaumea.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataHaumea.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataHaumea.csv', index=False)      
print('Complete 1')
print('Complete 1')


