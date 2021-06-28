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
outputDataFileRR43 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR43'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["RR43{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["RR43"+str(i)])):
        distance["RR43"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['RR431'])
print('YES')
print(distance['RR432'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZRR43.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZRR43.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZRR43.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZRR43.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceRR43 = np.zeros(len(df1))
saturnDistanceRR43 = np.zeros(len(df2))
uranusDistanceRR43 = np.zeros(len(df3))
neptuneDistanceRR43 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

RR431Distance = np.zeros(len(distance['RR431']))
RR432Distance = np.zeros(len(distance['RR432']))
RR433Distance = np.zeros(len(distance['RR433']))
RR434Distance = np.zeros(len(distance['RR434']))
RR435Distance = np.zeros(len(distance['RR435']))
RR436Distance = np.zeros(len(distance['RR436']))
RR437Distance = np.zeros(len(distance['RR437']))
RR438Distance = np.zeros(len(distance['RR438']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceRR43[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceRR43[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceRR43[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceRR43[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceRR43[i]
    finalGGData[i,1] = saturnDistanceRR43[i]
    finalGGData[i,2] = uranusDistanceRR43[i]
    finalGGData[i,3] = neptuneDistanceRR43[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['RR431'])):
    RR431Distance[i] = distance['RR431'][i]
    
for i in range(len(distance['RR432'])):
    RR432Distance[i] = distance['RR432'][i]

for i in range(len(distance['RR433'])):
    RR433Distance[i] = distance['RR433'][i]

for i in range(len(distance['RR434'])):
    RR434Distance[i] = distance['RR434'][i]

for i in range(len(distance['RR435'])):
    RR435Distance[i] = distance['RR435'][i]

for i in range(len(distance['RR436'])):
    RR436Distance[i] = distance['RR436'][i]

for i in range(len(distance['RR437'])):
    RR437Distance[i] = distance['RR437'][i]
    
for i in range(len(distance['RR438'])):
    RR438Distance[i] = distance['RR438'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("RR431Distance.csv", RR431Distance, delimiter=",")
df = pd.read_csv('RR431Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR431Distance.csv', index=False) 

np.savetxt("RR432Distance.csv", RR432Distance, delimiter=",")
df = pd.read_csv('RR432Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR432Distance.csv', index=False)

np.savetxt("RR433Distance.csv", RR433Distance, delimiter=",")
df = pd.read_csv('RR433Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR433Distance.csv', index=False)

np.savetxt("RR434Distance.csv", RR434Distance, delimiter=",")
df = pd.read_csv('RR434Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR434Distance.csv', index=False)

np.savetxt("RR435Distance.csv", RR435Distance, delimiter=",")
df = pd.read_csv('RR435Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR435Distance.csv', index=False)

np.savetxt("RR436Distance.csv", RR436Distance, delimiter=",")
df = pd.read_csv('RR436Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR436Distance.csv', index=False)

np.savetxt("RR437Distance.csv", RR437Distance, delimiter=",")
df = pd.read_csv('RR437Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR437Distance.csv', index=False)

np.savetxt("RR438Distance.csv", RR438Distance, delimiter=",")
df = pd.read_csv('RR438Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('RR438Distance.csv', index=False)

np.savetxt("FinalGGDataRR43.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataRR43.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataRR43.csv', index=False)      
print('Complete 1')
print('Complete 1')


