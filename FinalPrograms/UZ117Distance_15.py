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
outputDataFileUZ117 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ117'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["UZ117{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["UZ117"+str(i)])):
        distance["UZ117"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['UZ1171'])
print('YES')
print(distance['UZ1172'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZUZ117.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZUZ117.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZUZ117.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZUZ117.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceUZ117 = np.zeros(len(df1))
saturnDistanceUZ117 = np.zeros(len(df2))
uranusDistanceUZ117 = np.zeros(len(df3))
neptuneDistanceUZ117 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

UZ1171Distance = np.zeros(len(distance['UZ1171']))
UZ1172Distance = np.zeros(len(distance['UZ1172']))
UZ1173Distance = np.zeros(len(distance['UZ1173']))
UZ1174Distance = np.zeros(len(distance['UZ1174']))
UZ1175Distance = np.zeros(len(distance['UZ1175']))
UZ1176Distance = np.zeros(len(distance['UZ1176']))
UZ1177Distance = np.zeros(len(distance['UZ1177']))
UZ1178Distance = np.zeros(len(distance['UZ1178']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceUZ117[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceUZ117[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceUZ117[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceUZ117[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceUZ117[i]
    finalGGData[i,1] = saturnDistanceUZ117[i]
    finalGGData[i,2] = uranusDistanceUZ117[i]
    finalGGData[i,3] = neptuneDistanceUZ117[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['UZ1171'])):
    UZ1171Distance[i] = distance['UZ1171'][i]
    
for i in range(len(distance['UZ1172'])):
    UZ1172Distance[i] = distance['UZ1172'][i]

for i in range(len(distance['UZ1173'])):
    UZ1173Distance[i] = distance['UZ1173'][i]

for i in range(len(distance['UZ1174'])):
    UZ1174Distance[i] = distance['UZ1174'][i]

for i in range(len(distance['UZ1175'])):
    UZ1175Distance[i] = distance['UZ1175'][i]

for i in range(len(distance['UZ1176'])):
    UZ1176Distance[i] = distance['UZ1176'][i]

for i in range(len(distance['UZ1177'])):
    UZ1177Distance[i] = distance['UZ1177'][i]
    
for i in range(len(distance['UZ1178'])):
    UZ1178Distance[i] = distance['UZ1178'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("UZ1171Distance.csv", UZ1171Distance, delimiter=",")
df = pd.read_csv('UZ1171Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1171Distance.csv', index=False) 

np.savetxt("UZ1172Distance.csv", UZ1172Distance, delimiter=",")
df = pd.read_csv('UZ1172Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1172Distance.csv', index=False)

np.savetxt("UZ1173Distance.csv", UZ1173Distance, delimiter=",")
df = pd.read_csv('UZ1173Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1173Distance.csv', index=False)

np.savetxt("UZ1174Distance.csv", UZ1174Distance, delimiter=",")
df = pd.read_csv('UZ1174Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1174Distance.csv', index=False)

np.savetxt("UZ1175Distance.csv", UZ1175Distance, delimiter=",")
df = pd.read_csv('UZ1175Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1175Distance.csv', index=False)

np.savetxt("UZ1176Distance.csv", UZ1176Distance, delimiter=",")
df = pd.read_csv('UZ1176Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1176Distance.csv', index=False)

np.savetxt("UZ1177Distance.csv", UZ1177Distance, delimiter=",")
df = pd.read_csv('UZ1177Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1177Distance.csv', index=False)

np.savetxt("UZ1178Distance.csv", UZ1178Distance, delimiter=",")
df = pd.read_csv('UZ1178Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('UZ1178Distance.csv', index=False)

np.savetxt("FinalGGDataUZ117.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataUZ117.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataUZ117.csv', index=False)      
print('Complete 1')
print('Complete 1')


