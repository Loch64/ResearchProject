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
outputDataFileAJ281 = np.zeros(24*3).reshape(24,3)
count1 = 0
count2 = 1
count3 = 2
for i in range(1,9):
    print(i)
    PATH = './USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ281'+str(i)+'.csv'
    objects["df{0}".format(i)] = pd.read_csv(PATH)
    distance["AJ281{0}".format(i)] = np.zeros(len(objects['df'+str(i)]))
    for j in range(len(distance["AJ281"+str(i)])):
        distance["AJ281"+str(i)][j] = math.sqrt((math.pow(objects['df'+str(i)].values[j,0],2))+(math.pow(objects['df'+str(i)].values[j,1],2))+(math.pow(objects['df'+str(i)].values[j,2],2)))

print(distance['AJ2811'])
print('YES')
print(distance['AJ2812'])

PATH1 = './USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZAJ281.csv'
PATH2 = './USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZAJ281.csv'
PATH3 = './USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZAJ281.csv'
PATH4 = './USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZAJ281.csv'
df1 = pd.read_csv(PATH1)
df2 = pd.read_csv(PATH2)
df3 = pd.read_csv(PATH3)
df4 = pd.read_csv(PATH4)

print('YES GG READ')
print('YES GG READ')

jupiterDistanceAJ281 = np.zeros(len(df1))
saturnDistanceAJ281 = np.zeros(len(df2))
uranusDistanceAJ281 = np.zeros(len(df3))
neptuneDistanceAJ281 = np.zeros(len(df4))

print('READ GG ARRAY')
print('READ GG ARRAY')

AJ2811Distance = np.zeros(len(distance['AJ2811']))
AJ2812Distance = np.zeros(len(distance['AJ2812']))
AJ2813Distance = np.zeros(len(distance['AJ2813']))
AJ2814Distance = np.zeros(len(distance['AJ2814']))
AJ2815Distance = np.zeros(len(distance['AJ2815']))
AJ2816Distance = np.zeros(len(distance['AJ2816']))
AJ2817Distance = np.zeros(len(distance['AJ2817']))
AJ2818Distance = np.zeros(len(distance['AJ2818']))

print('Dictionary items read into arrays')
print('Dictionary items read into arrays')

for i in range(len(df1)):
    jupiterDistanceAJ281[i] = math.sqrt((math.pow(df1.values[i,0],2))+(math.pow(df1.values[i,1],2))+(math.pow(df1.values[i,2],2)))
    saturnDistanceAJ281[i] = math.sqrt((math.pow(df2.values[i,0],2))+(math.pow(df2.values[i,1],2))+(math.pow(df2.values[i,2],2)))
    uranusDistanceAJ281[i] = math.sqrt((math.pow(df3.values[i,0],2))+(math.pow(df3.values[i,1],2))+(math.pow(df3.values[i,2],2)))
    neptuneDistanceAJ281[i] = math.sqrt((math.pow(df4.values[i,0],2))+(math.pow(df4.values[i,1],2))+(math.pow(df4.values[i,2],2)))

print('GG distance read into arrays')
print('GG distance read into arrays')

finalGGData = np.zeros(180000*4).reshape(180000,4)
for i in range(len(finalGGData)):
    finalGGData[i,0] = jupiterDistanceAJ281[i]
    finalGGData[i,1] = saturnDistanceAJ281[i]
    finalGGData[i,2] = uranusDistanceAJ281[i]
    finalGGData[i,3] = neptuneDistanceAJ281[i]

print('Final GG array made')
print('Final GG array made')

for i in range(len(distance['AJ2811'])):
    AJ2811Distance[i] = distance['AJ2811'][i]
    
for i in range(len(distance['AJ2812'])):
    AJ2812Distance[i] = distance['AJ2812'][i]

for i in range(len(distance['AJ2813'])):
    AJ2813Distance[i] = distance['AJ2813'][i]

for i in range(len(distance['AJ2814'])):
    AJ2814Distance[i] = distance['AJ2814'][i]

for i in range(len(distance['AJ2815'])):
    AJ2815Distance[i] = distance['AJ2815'][i]

for i in range(len(distance['AJ2816'])):
    AJ2816Distance[i] = distance['AJ2816'][i]

for i in range(len(distance['AJ2817'])):
    AJ2817Distance[i] = distance['AJ2817'][i]
    
for i in range(len(distance['AJ2818'])):
    AJ2818Distance[i] = distance['AJ2818'][i]

print('Clones added to their respective arrays')
print('Clones added to their respective arrays')

np.savetxt("AJ2811Distance.csv", AJ2811Distance, delimiter=",")
df = pd.read_csv('AJ2811Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2811Distance.csv', index=False) 

np.savetxt("AJ2812Distance.csv", AJ2812Distance, delimiter=",")
df = pd.read_csv('AJ2812Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2812Distance.csv', index=False)

np.savetxt("AJ2813Distance.csv", AJ2813Distance, delimiter=",")
df = pd.read_csv('AJ2813Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2813Distance.csv', index=False)

np.savetxt("AJ2814Distance.csv", AJ2814Distance, delimiter=",")
df = pd.read_csv('AJ2814Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2814Distance.csv', index=False)

np.savetxt("AJ2815Distance.csv", AJ2815Distance, delimiter=",")
df = pd.read_csv('AJ2815Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2815Distance.csv', index=False)

np.savetxt("AJ2816Distance.csv", AJ2816Distance, delimiter=",")
df = pd.read_csv('AJ2816Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2816Distance.csv', index=False)

np.savetxt("AJ2817Distance.csv", AJ2817Distance, delimiter=",")
df = pd.read_csv('AJ2817Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2817Distance.csv', index=False)

np.savetxt("AJ2818Distance.csv", AJ2818Distance, delimiter=",")
df = pd.read_csv('AJ2818Distance.csv', header=None)
df.rename(columns={0: 'Distance'}, inplace=True)
df.to_csv('AJ2818Distance.csv', index=False)

np.savetxt("FinalGGDataAJ281.csv", finalGGData, delimiter=",")
df = pd.read_csv('FinalGGDataAJ281.csv', header=None)
df.rename(columns={0: 'Jupiter', 1: 'Saturn', 2: 'Uranus', 3: 'Neptune'}, inplace=True)
df.to_csv('FinalGGDataAJ281.csv', index=False)      
print('Complete 1')
print('Complete 1')

