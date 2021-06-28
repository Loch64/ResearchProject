#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

TX3001 = np.loadtxt('./distanceData/TX3001Distance.csv', skiprows=1) #open('./distanceData/TX3001Distance.csv').read().split('\n')
TX3001Distance = []
count1 = 0
nrows1 = 0
for i in range(len(TX3001)):
    if float(TX3001[i])!=0 and float(TX3001[i])<100 and count1==0:
        TX3001Distance.append(float(TX3001[i]))
        nrows1 += 1
    elif float(TX3001[i])>100 and count1==0:
        TX3001Distance.append(float(TX3001[i]))
        count1 += 1
        nrows1 += 1
        break
if len(TX3001Distance)>maxValue:
    maxValue = len(TX3001Distance)

TX3002 = np.loadtxt('./distanceData/TX3002Distance.csv', skiprows=1)
TX3002Distance = []
count2 = 0
nrows2 = 0
for i in range(len(TX3002)):
    if float(TX3002[i])!=0 and float(TX3002[i])<100 and count2==0:
        TX3002Distance.append(float(TX3002[i]))
        nrows2 += 1
    elif float(TX3002[i])>100 and count2==0:
        TX3002Distance.append(float(TX3002[i]))
        count2 += 1
        nrows2 += 1
        break
if len(TX3002Distance)>maxValue:
    maxValue = len(TX3002Distance)
        
TX3003 = np.loadtxt('./distanceData/TX3003Distance.csv', skiprows=1)
TX3003Distance = []
count3 = 0
nrows3 = 0
for i in range(len(TX3003)):
    if float(TX3003[i])!=0 and float(TX3003[i])<100 and count3==0:
        TX3003Distance.append(float(TX3003[i]))
        nrows3 += 1
    elif float(TX3003[i])>100 and count3==0:
        TX3003Distance.append(float(TX3003[i]))
        count3 += 1
        nrows3 += 1
        break
if len(TX3003Distance)>maxValue:
    maxValue = len(TX3003Distance)
        
TX3004 = np.loadtxt('./distanceData/TX3004Distance.csv', skiprows=1)
TX3004Distance = []
count4 = 0
nrows4 = 0
for i in range(len(TX3004)):
    if float(TX3004[i])!=0 and float(TX3004[i])<100 and count4==0:
        TX3004Distance.append(float(TX3004[i]))
        nrows4 += 1
    elif float(TX3004[i])>100 and count4==0:
        TX3004Distance.append(float(TX3004[i]))
        count4 += 1
        nrows4 += 1
        break
if len(TX3004Distance)>maxValue:
    maxValue = len(TX3004Distance)
        
TX3005 = np.loadtxt('./distanceData/TX3005Distance.csv', skiprows=1)
TX3005Distance = []
count5 = 0
nrows5 = 0
for i in range(len(TX3005)):
    if float(TX3005[i])!=0 and float(TX3005[i])<100 and count5==0:
        TX3005Distance.append(float(TX3005[i]))
        nrows5 += 1
    elif float(TX3005[i])>100 and count5==0:
        TX3005Distance.append(float(TX3005[i]))
        count5 += 1
        nrows5 += 1
        break
if len(TX3005Distance)>maxValue:
    maxValue = len(TX3005Distance)
        
TX3006 = np.loadtxt('./distanceData/TX3006Distance.csv', skiprows=1)
TX3006Distance = []
count6 = 0
nrows6 = 0
for i in range(len(TX3006)):
    if float(TX3006[i])!=0 and float(TX3006[i])<100 and count6==0:
        TX3006Distance.append(float(TX3006[i]))
        nrows6 += 1
    elif float(TX3006[i])>100 and count6==0:
        TX3006Distance.append(float(TX3006[i]))
        count6 += 1
        nrows6 += 1
        break
if len(TX3006Distance)>maxValue:
    maxValue = len(TX3006Distance)
        
TX3007 = np.loadtxt('./distanceData/TX3007Distance.csv', skiprows=1)
TX3007Distance = []
count7 = 0
nrows7 = 0
for i in range(len(TX3007)):
    if float(TX3007[i])!=0 and float(TX3007[i])<100 and count7==0:
        TX3007Distance.append(float(TX3007[i]))
        nrows7 += 1
    elif float(TX3007[i])>100 and count7==0:
        TX3007Distance.append(float(TX3007[i]))
        count7 += 1
        nrows7 += 1
        break
if len(TX3007Distance)>maxValue:
    maxValue = len(TX3007Distance)
        
TX3008 = np.loadtxt('./distanceData/TX3008Distance.csv', skiprows=1)
TX3008Distance = []
count8 = 0
nrows8 = 0
for i in range(len(TX3008)):
    if float(TX3008[i])!=0 and float(TX3008[i])<100 and count8==0:
        TX3008Distance.append(float(TX3008[i]))
        nrows8 += 1
    elif float(TX3008[i])>100 and count8==0:
        TX3008Distance.append(float(TX3008[i]))
        count8 += 1
        nrows8 += 1
        break
if len(TX3008Distance)>maxValue:
    maxValue = len(TX3008Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataTX300.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataTX300.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataTX300.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataTX300.csv', usecols=['Neptune'], nrows=maxValue)

TX3001e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3001.csv', usecols=['e'], nrows=nrows1)
TX3002e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3002.csv', usecols=['e'], nrows=nrows2)
TX3003e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3003.csv', usecols=['e'], nrows=nrows3)
TX3004e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3004.csv', usecols=['e'], nrows=nrows4)
TX3005e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3005.csv', usecols=['e'], nrows=nrows5)
TX3006e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3006.csv', usecols=['e'], nrows=nrows6)
TX3007e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3007.csv', usecols=['e'], nrows=nrows7)
TX3008e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3008.csv', usecols=['e'], nrows=nrows8)

TX3001i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3001.csv', usecols=['i'], nrows=nrows1)
TX3002i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3002.csv', usecols=['i'], nrows=nrows2)
TX3003i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3003.csv', usecols=['i'], nrows=nrows3)
TX3004i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3004.csv', usecols=['i'], nrows=nrows4)
TX3005i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3005.csv', usecols=['i'], nrows=nrows5)
TX3006i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3006.csv', usecols=['i'], nrows=nrows6)
TX3007i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3007.csv', usecols=['i'], nrows=nrows7)
TX3008i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TX3008.csv', usecols=['i'], nrows=nrows8)

TX3001iDeg = []
TX3002iDeg = []
TX3003iDeg = []
TX3004iDeg = []
TX3005iDeg = []
TX3006iDeg = []
TX3007iDeg = []
TX3008iDeg = []

for j in range(nrows1):
    z = TX3001i.values[j]
    rad = math.degrees(z)
    TX3001iDeg.append(float(rad))
for j in range(nrows2):
    z = TX3002i.values[j]
    rad = math.degrees(z)
    TX3002iDeg.append(float(rad))
for j in range(nrows3):
    z = TX3003i.values[j]
    rad = math.degrees(z)
    TX3003iDeg.append(float(rad))
for j in range(nrows4):
    z = TX3004i.values[j]
    rad = math.degrees(z)
    TX3004iDeg.append(float(rad))
for j in range(nrows5):
    z = TX3005i.values[j]
    rad = math.degrees(z)
    TX3005iDeg.append(float(rad))
for j in range(nrows6):
    z = TX3006i.values[j]
    rad = math.degrees(z)
    TX3006iDeg.append(float(rad))
for j in range(nrows7):
    z = TX3007i.values[j]
    rad = math.degrees(z)
    TX3007iDeg.append(float(rad))
for j in range(nrows8):
    z = TX3008i.values[j]
    rad = math.degrees(z)
    TX3008iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(TX3001Distance, color='blue', label='Clone 1')
ax1.plot(TX3002Distance, color='green', label='Clone 2')
ax1.plot(TX3003Distance, color='red', label='Clone 3')
ax1.plot(TX3004Distance, color='brown', label='Clone 4')
ax1.plot(TX3005Distance, color='purple', label='Clone 5')
ax1.plot(TX3006Distance, color='orange', label='Clone 6')
ax1.plot(TX3007Distance, color='grey', label='Clone 7')
ax1.plot(TX3008Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(TX3001e, color='blue', label='Clone 1')
ax2.plot(TX3002e, color='green', label='Clone 2')
ax2.plot(TX3003e, color='red', label='Clone 3')
ax2.plot(TX3004e, color='brown', label='Clone 4')
ax2.plot(TX3005e, color='purple', label='Clone 5')
ax2.plot(TX3006e, color='orange', label='Clone 6')
ax2.plot(TX3007e, color='grey', label='Clone 7')
ax2.plot(TX3008e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.1,0.16)

ax3.plot(TX3001iDeg, color='blue', label='Clone 1')
ax3.plot(TX3002iDeg, color='green', label='Clone 2')
ax3.plot(TX3003iDeg, color='red', label='Clone 3')
ax3.plot(TX3004iDeg, color='brown', label='Clone 4')
ax3.plot(TX3005iDeg, color='purple', label='Clone 5')
ax3.plot(TX3006iDeg, color='orange', label='Clone 6')
ax3.plot(TX3007iDeg, color='grey', label='Clone 7')
ax3.plot(TX3008iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('TX300')
fig = plt.savefig('./TX300Figure.png', bbox_inches='tight')

