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
outputDataFileQW441 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW441'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["QW441{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["QW441"+str(i)])):
        distance["QW441"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['QW4411'])
print('YES')
print(distance['QW4412'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZQW441.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZQW441.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZQW441.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZQW441.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceQW441 = np.zeros(len(df1))
saturnDistanceQW441 = np.zeros(len(df2))
uranusDistanceQW441 = np.zeros(len(df3))
neptuneDistanceQW441 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

QW4411Distance = np.zeros(len(distance['QW4411']))
QW4412Distance = np.zeros(len(distance['QW4412']))
QW4413Distance = np.zeros(len(distance['QW4413']))
QW4414Distance = np.zeros(len(distance['QW4414']))
QW4415Distance = np.zeros(len(distance['QW4415']))
QW4416Distance = np.zeros(len(distance['QW4416']))
QW4417Distance = np.zeros(len(distance['QW4417']))
QW4418Distance = np.zeros(len(distance['QW4418']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceQW441[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceQW441[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceQW441[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceQW441[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceQW441[i]
    finalGGData[i,1] = saturnDistanceQW441[i]
    finalGGData[i,2] = uranusDistanceQW441[i]
    finalGGData[i,3] = neptuneDistanceQW441[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['QW4411'])):
    QW4411Distance[i] = distance['QW4411'][i]
    
for i in range(len(distance['QW4412'])):
    QW4412Distance[i] = distance['QW4412'][i]

for i in range(len(distance['QW4413'])):
    QW4413Distance[i] = distance['QW4413'][i]

for i in range(len(distance['QW4414'])):
    QW4414Distance[i] = distance['QW4414'][i]

for i in range(len(distance['QW4415'])):
    QW4415Distance[i] = distance['QW4415'][i]

for i in range(len(distance['QW4416'])):
    QW4416Distance[i] = distance['QW4416'][i]

for i in range(len(distance['QW4417'])):
    QW4417Distance[i] = distance['QW4417'][i]
    
for i in range(len(distance['QW4418'])):
    QW4418Distance[i] = distance['QW4418'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("QW4411Distance.csv", QW4411Distance, delimiter=",")
df = pd.read_csv('QW4411Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4411Distance.csv', index=False) 

np.savetxt("QW4412Distance.csv", QW4412Distance, delimiter=",")
df = pd.read_csv('QW4412Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4412Distance.csv', index=False)

np.savetxt("QW4413Distance.csv", QW4413Distance, delimiter=",")
df = pd.read_csv('QW4413Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4413Distance.csv', index=False)

np.savetxt("QW4414Distance.csv", QW4414Distance, delimiter=",")
df = pd.read_csv('QW4414Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4414Distance.csv', index=False)

np.savetxt("QW4415Distance.csv", QW4415Distance, delimiter=",")
df = pd.read_csv('QW4415Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4415Distance.csv', index=False)

np.savetxt("QW4416Distance.csv", QW4416Distance, delimiter=",")
df = pd.read_csv('QW4416Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4416Distance.csv', index=False)

np.savetxt("QW4417Distance.csv", QW4417Distance, delimiter=",")
df = pd.read_csv('QW4417Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4417Distance.csv', index=False)

np.savetxt("QW4418Distance.csv", QW4418Distance, delimiter=",")
df = pd.read_csv('QW4418Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('QW4418Distance.csv', index=False)

np.savetxt("FinalGGDataQW441.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataQW441.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataQW441.csv', index=False)      
print('Complete 1')
print('Complete 1')


