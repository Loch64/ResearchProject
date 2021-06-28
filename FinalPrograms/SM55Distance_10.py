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
outputDataFileSM55 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM55'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["SM55{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["SM55"+str(i)])):
        distance["SM55"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['SM551'])
print('YES')
print(distance['SM552'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZSM55.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZSM55.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZSM55.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZSM55.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceSM55 = np.zeros(len(df1))
saturnDistanceSM55 = np.zeros(len(df2))
uranusDistanceSM55 = np.zeros(len(df3))
neptuneDistanceSM55 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

SM551Distance = np.zeros(len(distance['SM551']))
SM552Distance = np.zeros(len(distance['SM552']))
SM553Distance = np.zeros(len(distance['SM553']))
SM554Distance = np.zeros(len(distance['SM554']))
SM555Distance = np.zeros(len(distance['SM555']))
SM556Distance = np.zeros(len(distance['SM556']))
SM557Distance = np.zeros(len(distance['SM557']))
SM558Distance = np.zeros(len(distance['SM558']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceSM55[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceSM55[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceSM55[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceSM55[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceSM55[i]
    finalGGData[i,1] = saturnDistanceSM55[i]
    finalGGData[i,2] = uranusDistanceSM55[i]
    finalGGData[i,3] = neptuneDistanceSM55[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['SM551'])):
    SM551Distance[i] = distance['SM551'][i]
    
for i in range(len(distance['SM552'])):
    SM552Distance[i] = distance['SM552'][i]

for i in range(len(distance['SM553'])):
    SM553Distance[i] = distance['SM553'][i]

for i in range(len(distance['SM554'])):
    SM554Distance[i] = distance['SM554'][i]

for i in range(len(distance['SM555'])):
    SM555Distance[i] = distance['SM555'][i]

for i in range(len(distance['SM556'])):
    SM556Distance[i] = distance['SM556'][i]

for i in range(len(distance['SM557'])):
    SM557Distance[i] = distance['SM557'][i]
    
for i in range(len(distance['SM558'])):
    SM558Distance[i] = distance['SM558'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("SM551Distance.csv", SM551Distance, delimiter=",")
df = pd.read_csv('SM551Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM551Distance.csv', index=False) 

np.savetxt("SM552Distance.csv", SM552Distance, delimiter=",")
df = pd.read_csv('SM552Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM552Distance.csv', index=False)

np.savetxt("SM553Distance.csv", SM553Distance, delimiter=",")
df = pd.read_csv('SM553Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM553Distance.csv', index=False)

np.savetxt("SM554Distance.csv", SM554Distance, delimiter=",")
df = pd.read_csv('SM554Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM554Distance.csv', index=False)

np.savetxt("SM555Distance.csv", SM555Distance, delimiter=",")
df = pd.read_csv('SM555Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM555Distance.csv', index=False)

np.savetxt("SM556Distance.csv", SM556Distance, delimiter=",")
df = pd.read_csv('SM556Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM556Distance.csv', index=False)

np.savetxt("SM557Distance.csv", SM557Distance, delimiter=",")
df = pd.read_csv('SM557Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM557Distance.csv', index=False)

np.savetxt("SM558Distance.csv", SM558Distance, delimiter=",")
df = pd.read_csv('SM558Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('SM558Distance.csv', index=False)

np.savetxt("FinalGGDataSM55.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataSM55.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataSM55.csv', index=False)      
print('Complete 1')
print('Complete 1')


