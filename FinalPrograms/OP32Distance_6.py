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
outputDataFileOP32 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP32'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["OP32{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["OP32"+str(i)])):
        distance["OP32"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['OP321'])
print('YES')
print(distance['OP322'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZOP32.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZOP32.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZOP32.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZOP32.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceOP32 = np.zeros(len(df1))
saturnDistanceOP32 = np.zeros(len(df2))
uranusDistanceOP32 = np.zeros(len(df3))
neptuneDistanceOP32 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

OP321Distance = np.zeros(len(distance['OP321']))
OP322Distance = np.zeros(len(distance['OP322']))
OP323Distance = np.zeros(len(distance['OP323']))
OP324Distance = np.zeros(len(distance['OP324']))
OP325Distance = np.zeros(len(distance['OP325']))
OP326Distance = np.zeros(len(distance['OP326']))
OP327Distance = np.zeros(len(distance['OP327']))
OP328Distance = np.zeros(len(distance['OP328']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceOP32[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceOP32[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceOP32[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceOP32[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceOP32[i]
    finalGGData[i,1] = saturnDistanceOP32[i]
    finalGGData[i,2] = uranusDistanceOP32[i]
    finalGGData[i,3] = neptuneDistanceOP32[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['OP321'])):
    OP321Distance[i] = distance['OP321'][i]
    
for i in range(len(distance['OP322'])):
    OP322Distance[i] = distance['OP322'][i]

for i in range(len(distance['OP323'])):
    OP323Distance[i] = distance['OP323'][i]

for i in range(len(distance['OP324'])):
    OP324Distance[i] = distance['OP324'][i]

for i in range(len(distance['OP325'])):
    OP325Distance[i] = distance['OP325'][i]

for i in range(len(distance['OP326'])):
    OP326Distance[i] = distance['OP326'][i]

for i in range(len(distance['OP327'])):
    OP327Distance[i] = distance['OP327'][i]
    
for i in range(len(distance['OP328'])):
    OP328Distance[i] = distance['OP328'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("OP321Distance.csv", OP321Distance, delimiter=",")
df = pd.read_csv('OP321Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP321Distance.csv', index=False) 

np.savetxt("OP322Distance.csv", OP322Distance, delimiter=",")
df = pd.read_csv('OP322Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP322Distance.csv', index=False)

np.savetxt("OP323Distance.csv", OP323Distance, delimiter=",")
df = pd.read_csv('OP323Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP323Distance.csv', index=False)

np.savetxt("OP324Distance.csv", OP324Distance, delimiter=",")
df = pd.read_csv('OP324Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP324Distance.csv', index=False)

np.savetxt("OP325Distance.csv", OP325Distance, delimiter=",")
df = pd.read_csv('OP325Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP325Distance.csv', index=False)

np.savetxt("OP326Distance.csv", OP326Distance, delimiter=",")
df = pd.read_csv('OP326Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP326Distance.csv', index=False)

np.savetxt("OP327Distance.csv", OP327Distance, delimiter=",")
df = pd.read_csv('OP327Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP327Distance.csv', index=False)

np.savetxt("OP328Distance.csv", OP328Distance, delimiter=",")
df = pd.read_csv('OP328Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OP328Distance.csv', index=False)

np.savetxt("FinalGGDataOP32.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataOP32.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataOP32.csv', index=False)      
print('Complete 1')
print('Complete 1')


