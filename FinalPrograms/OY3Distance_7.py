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
outputDataFileOY3 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY3'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["OY3{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["OY3"+str(i)])):
        distance["OY3"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['OY31'])
print('YES')
print(distance['OY32'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZOY3.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZOY3.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZOY3.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZOY3.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceOY3 = np.zeros(len(df1))
saturnDistanceOY3 = np.zeros(len(df2))
uranusDistanceOY3 = np.zeros(len(df3))
neptuneDistanceOY3 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

OY31Distance = np.zeros(len(distance['OY31']))
OY32Distance = np.zeros(len(distance['OY32']))
OY33Distance = np.zeros(len(distance['OY33']))
OY34Distance = np.zeros(len(distance['OY34']))
OY35Distance = np.zeros(len(distance['OY35']))
OY36Distance = np.zeros(len(distance['OY36']))
OY37Distance = np.zeros(len(distance['OY37']))
OY38Distance = np.zeros(len(distance['OY38']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceOY3[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceOY3[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceOY3[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceOY3[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceOY3[i]
    finalGGData[i,1] = saturnDistanceOY3[i]
    finalGGData[i,2] = uranusDistanceOY3[i]
    finalGGData[i,3] = neptuneDistanceOY3[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['OY31'])):
    OY31Distance[i] = distance['OY31'][i]
    
for i in range(len(distance['OY32'])):
    OY32Distance[i] = distance['OY32'][i]

for i in range(len(distance['OY33'])):
    OY33Distance[i] = distance['OY33'][i]

for i in range(len(distance['OY34'])):
    OY34Distance[i] = distance['OY34'][i]

for i in range(len(distance['OY35'])):
    OY35Distance[i] = distance['OY35'][i]

for i in range(len(distance['OY36'])):
    OY36Distance[i] = distance['OY36'][i]

for i in range(len(distance['OY37'])):
    OY37Distance[i] = distance['OY37'][i]
    
for i in range(len(distance['OY38'])):
    OY38Distance[i] = distance['OY38'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("OY31Distance.csv", OY31Distance, delimiter=",")
df = pd.read_csv('OY31Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY31Distance.csv', index=False) 

np.savetxt("OY32Distance.csv", OY32Distance, delimiter=",")
df = pd.read_csv('OY32Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY32Distance.csv', index=False)

np.savetxt("OY33Distance.csv", OY33Distance, delimiter=",")
df = pd.read_csv('OY33Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY33Distance.csv', index=False)

np.savetxt("OY34Distance.csv", OY34Distance, delimiter=",")
df = pd.read_csv('OY34Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY34Distance.csv', index=False)

np.savetxt("OY35Distance.csv", OY35Distance, delimiter=",")
df = pd.read_csv('OY35Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY35Distance.csv', index=False)

np.savetxt("OY36Distance.csv", OY36Distance, delimiter=",")
df = pd.read_csv('OY36Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY36Distance.csv', index=False)

np.savetxt("OY37Distance.csv", OY37Distance, delimiter=",")
df = pd.read_csv('OY37Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY37Distance.csv', index=False)

np.savetxt("OY38Distance.csv", OY38Distance, delimiter=",")
df = pd.read_csv('OY38Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('OY38Distance.csv', index=False)

np.savetxt("FinalGGDataOY3.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataOY3.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataOY3.csv', index=False)      
print('Complete 1')
print('Complete 1')


