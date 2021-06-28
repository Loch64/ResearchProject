#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

LO281 = np.loadtxt('./distanceData/LO281Distance.csv', skiprows=1) #open('./distanceData/LO281Distance.csv').read().split('\n')
LO281Distance = []
count1 = 0
nrows1 = 0
for i in range(len(LO281)):
    if float(LO281[i])!=0 and float(LO281[i])<100 and count1==0:
        LO281Distance.append(float(LO281[i]))
        nrows1 += 1
    elif float(LO281[i])>100 and count1==0:
        LO281Distance.append(float(LO281[i]))
        count1 += 1
        nrows1 += 1
        break
if len(LO281Distance)>maxValue:
    maxValue = len(LO281Distance)

LO282 = np.loadtxt('./distanceData/LO282Distance.csv', skiprows=1)
LO282Distance = []
count2 = 0
nrows2 = 0
for i in range(len(LO282)):
    if float(LO282[i])!=0 and float(LO282[i])<100 and count2==0:
        LO282Distance.append(float(LO282[i]))
        nrows2 += 1
    elif float(LO282[i])>100 and count2==0:
        LO282Distance.append(float(LO282[i]))
        count2 += 1
        nrows2 += 1
        break
if len(LO282Distance)>maxValue:
    maxValue = len(LO282Distance)
        
LO283 = np.loadtxt('./distanceData/LO283Distance.csv', skiprows=1)
LO283Distance = []
count3 = 0
nrows3 = 0
for i in range(len(LO283)):
    if float(LO283[i])!=0 and float(LO283[i])<100 and count3==0:
        LO283Distance.append(float(LO283[i]))
        nrows3 += 1
    elif float(LO283[i])>100 and count3==0:
        LO283Distance.append(float(LO283[i]))
        count3 += 1
        nrows3 += 1
        break
if len(LO283Distance)>maxValue:
    maxValue = len(LO283Distance)
        
LO284 = np.loadtxt('./distanceData/LO284Distance.csv', skiprows=1)
LO284Distance = []
count4 = 0
nrows4 = 0
for i in range(len(LO284)):
    if float(LO284[i])!=0 and float(LO284[i])<100 and count4==0:
        LO284Distance.append(float(LO284[i]))
        nrows4 += 1
    elif float(LO284[i])>100 and count4==0:
        LO284Distance.append(float(LO284[i]))
        count4 += 1
        nrows4 += 1
        break
if len(LO284Distance)>maxValue:
    maxValue = len(LO284Distance)
        
LO285 = np.loadtxt('./distanceData/LO285Distance.csv', skiprows=1)
LO285Distance = []
count5 = 0
nrows5 = 0
for i in range(len(LO285)):
    if float(LO285[i])!=0 and float(LO285[i])<100 and count5==0:
        LO285Distance.append(float(LO285[i]))
        nrows5 += 1
    elif float(LO285[i])>100 and count5==0:
        LO285Distance.append(float(LO285[i]))
        count5 += 1
        nrows5 += 1
        break
if len(LO285Distance)>maxValue:
    maxValue = len(LO285Distance)
        
LO286 = np.loadtxt('./distanceData/LO286Distance.csv', skiprows=1)
LO286Distance = []
count6 = 0
nrows6 = 0
for i in range(len(LO286)):
    if float(LO286[i])!=0 and float(LO286[i])<100 and count6==0:
        LO286Distance.append(float(LO286[i]))
        nrows6 += 1
    elif float(LO286[i])>100 and count6==0:
        LO286Distance.append(float(LO286[i]))
        count6 += 1
        nrows6 += 1
        break
if len(LO286Distance)>maxValue:
    maxValue = len(LO286Distance)
        
LO287 = np.loadtxt('./distanceData/LO287Distance.csv', skiprows=1)
LO287Distance = []
count7 = 0
nrows7 = 0
for i in range(len(LO287)):
    if float(LO287[i])!=0 and float(LO287[i])<100 and count7==0:
        LO287Distance.append(float(LO287[i]))
        nrows7 += 1
    elif float(LO287[i])>100 and count7==0:
        LO287Distance.append(float(LO287[i]))
        count7 += 1
        nrows7 += 1
        break
if len(LO287Distance)>maxValue:
    maxValue = len(LO287Distance)
        
LO288 = np.loadtxt('./distanceData/LO288Distance.csv', skiprows=1)
LO288Distance = []
count8 = 0
nrows8 = 0
for i in range(len(LO288)):
    if float(LO288[i])!=0 and float(LO288[i])<100 and count8==0:
        LO288Distance.append(float(LO288[i]))
        nrows8 += 1
    elif float(LO288[i])>100 and count8==0:
        LO288Distance.append(float(LO288[i]))
        count8 += 1
        nrows8 += 1
        break
if len(LO288Distance)>maxValue:
    maxValue = len(LO288Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataLO28.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataLO28.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataLO28.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataLO28.csv', usecols=['Neptune'], nrows=maxValue)

LO281e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO281.csv', usecols=['e'], nrows=nrows1)
LO282e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO282.csv', usecols=['e'], nrows=nrows2)
LO283e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO283.csv', usecols=['e'], nrows=nrows3)
LO284e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO284.csv', usecols=['e'], nrows=nrows4)
LO285e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO285.csv', usecols=['e'], nrows=nrows5)
LO286e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO286.csv', usecols=['e'], nrows=nrows6)
LO287e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO287.csv', usecols=['e'], nrows=nrows7)
LO288e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO288.csv', usecols=['e'], nrows=nrows8)

LO281i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO281.csv', usecols=['i'], nrows=nrows1)
LO282i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO282.csv', usecols=['i'], nrows=nrows2)
LO283i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO283.csv', usecols=['i'], nrows=nrows3)
LO284i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO284.csv', usecols=['i'], nrows=nrows4)
LO285i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO285.csv', usecols=['i'], nrows=nrows5)
LO286i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO286.csv', usecols=['i'], nrows=nrows6)
LO287i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO287.csv', usecols=['i'], nrows=nrows7)
LO288i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/LO288.csv', usecols=['i'], nrows=nrows8)

LO281iDeg = []
LO282iDeg = []
LO283iDeg = []
LO284iDeg = []
LO285iDeg = []
LO286iDeg = []
LO287iDeg = []
LO288iDeg = []

for j in range(nrows1):
    z = LO281i.values[j]
    rad = math.degrees(z)
    LO281iDeg.append(float(rad))
for j in range(nrows2):
    z = LO282i.values[j]
    rad = math.degrees(z)
    LO282iDeg.append(float(rad))
for j in range(nrows3):
    z = LO283i.values[j]
    rad = math.degrees(z)
    LO283iDeg.append(float(rad))
for j in range(nrows4):
    z = LO284i.values[j]
    rad = math.degrees(z)
    LO284iDeg.append(float(rad))
for j in range(nrows5):
    z = LO285i.values[j]
    rad = math.degrees(z)
    LO285iDeg.append(float(rad))
for j in range(nrows6):
    z = LO286i.values[j]
    rad = math.degrees(z)
    LO286iDeg.append(float(rad))
for j in range(nrows7):
    z = LO287i.values[j]
    rad = math.degrees(z)
    LO287iDeg.append(float(rad))
for j in range(nrows8):
    z = LO288i.values[j]
    rad = math.degrees(z)
    LO288iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(LO281Distance, color='blue', label='Clone 1')
ax1.plot(LO282Distance, color='green', label='Clone 2')
ax1.plot(LO283Distance, color='red', label='Clone 3')
ax1.plot(LO284Distance, color='brown', label='Clone 4')
ax1.plot(LO285Distance, color='purple', label='Clone 5')
ax1.plot(LO286Distance, color='orange', label='Clone 6')
ax1.plot(LO287Distance, color='grey', label='Clone 7')
ax1.plot(LO288Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(LO281e, color='blue', label='Clone 1')
ax2.plot(LO282e, color='green', label='Clone 2')
ax2.plot(LO283e, color='red', label='Clone 3')
ax2.plot(LO284e, color='brown', label='Clone 4')
ax2.plot(LO285e, color='purple', label='Clone 5')
ax2.plot(LO286e, color='orange', label='Clone 6')
ax2.plot(LO287e, color='grey', label='Clone 7')
ax2.plot(LO288e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.09,0.135)

ax3.plot(LO281iDeg, color='blue', label='Clone 1')
ax3.plot(LO282iDeg, color='green', label='Clone 2')
ax3.plot(LO283iDeg, color='red', label='Clone 3')
ax3.plot(LO284iDeg, color='brown', label='Clone 4')
ax3.plot(LO285iDeg, color='purple', label='Clone 5')
ax3.plot(LO286iDeg, color='orange', label='Clone 6')
ax3.plot(LO287iDeg, color='grey', label='Clone 7')
ax3.plot(LO288iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('LO28')
fig = plt.savefig('./LO28Figure.png', bbox_inches='tight')

