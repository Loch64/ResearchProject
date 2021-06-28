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
outputDataFileCB79 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB79'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["CB79{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["CB79"+str(i)])):
        distance["CB79"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['CB791'])
print('YES')
print(distance['CB792'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZCB79.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZCB79.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZCB79.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZCB79.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceCB79 = np.zeros(len(df1))
saturnDistanceCB79 = np.zeros(len(df2))
uranusDistanceCB79 = np.zeros(len(df3))
neptuneDistanceCB79 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

CB791Distance = np.zeros(len(distance['CB791']))
CB792Distance = np.zeros(len(distance['CB792']))
CB793Distance = np.zeros(len(distance['CB793']))
CB794Distance = np.zeros(len(distance['CB794']))
CB795Distance = np.zeros(len(distance['CB795']))
CB796Distance = np.zeros(len(distance['CB796']))
CB797Distance = np.zeros(len(distance['CB797']))
CB798Distance = np.zeros(len(distance['CB798']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceCB79[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceCB79[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceCB79[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceCB79[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(2000*4).reshape(2000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceCB79[i]
    finalGGData[i,1] = saturnDistanceCB79[i]
    finalGGData[i,2] = uranusDistanceCB79[i]
    finalGGData[i,3] = neptuneDistanceCB79[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['CB791'])):
    CB791Distance[i] = distance['CB791'][i]
    
for i in range(len(distance['CB792'])):
    CB792Distance[i] = distance['CB792'][i]

for i in range(len(distance['CB793'])):
    CB793Distance[i] = distance['CB793'][i]

for i in range(len(distance['CB794'])):
    CB794Distance[i] = distance['CB794'][i]

for i in range(len(distance['CB795'])):
    CB795Distance[i] = distance['CB795'][i]

for i in range(len(distance['CB796'])):
    CB796Distance[i] = distance['CB796'][i]

for i in range(len(distance['CB797'])):
    CB797Distance[i] = distance['CB797'][i]
    
for i in range(len(distance['CB798'])):
    CB798Distance[i] = distance['CB798'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("CB791Distance.csv", CB791Distance, delimiter=",")
df = pd.read_csv('CB791Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB791Distance.csv', index=False) 

np.savetxt("CB792Distance.csv", CB792Distance, delimiter=",")
df = pd.read_csv('CB792Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB792Distance.csv', index=False)

np.savetxt("CB793Distance.csv", CB793Distance, delimiter=",")
df = pd.read_csv('CB793Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB793Distance.csv', index=False)

np.savetxt("CB794Distance.csv", CB794Distance, delimiter=",")
df = pd.read_csv('CB794Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB794Distance.csv', index=False)

np.savetxt("CB795Distance.csv", CB795Distance, delimiter=",")
df = pd.read_csv('CB795Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB795Distance.csv', index=False)

np.savetxt("CB796Distance.csv", CB796Distance, delimiter=",")
df = pd.read_csv('CB796Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB796Distance.csv', index=False)

np.savetxt("CB797Distance.csv", CB797Distance, delimiter=",")
df = pd.read_csv('CB797Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB797Distance.csv', index=False)

np.savetxt("CB798Distance.csv", CB798Distance, delimiter=",")
df = pd.read_csv('CB798Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('CB798Distance.csv', index=False)

np.savetxt("FinalGGDataCB79.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataCB79.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataCB79.csv', index=False)      
print('Complete 1')
print('Complete 1')


