#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

SQ3171 = np.loadtxt('./distanceData/SQ3171Distance.csv', skiprows=1) #open('./distanceData/SQ3171Distance.csv').read().split('\n')
SQ3171Distance = []
count1 = 0
nrows1 = 0
for i in range(len(SQ3171)):
    if float(SQ3171[i])!=0 and float(SQ3171[i])<100 and count1==0:
        SQ3171Distance.append(float(SQ3171[i]))
        nrows1 += 1
    elif float(SQ3171[i])>100 and count1==0:
        SQ3171Distance.append(float(SQ3171[i]))
        count1 += 1
        nrows1 += 1
        break
if len(SQ3171Distance)>maxValue:
    maxValue = len(SQ3171Distance)

SQ3172 = np.loadtxt('./distanceData/SQ3172Distance.csv', skiprows=1)
SQ3172Distance = []
count2 = 0
nrows2 = 0
for i in range(len(SQ3172)):
    if float(SQ3172[i])!=0 and float(SQ3172[i])<100 and count2==0:
        SQ3172Distance.append(float(SQ3172[i]))
        nrows2 += 1
    elif float(SQ3172[i])>100 and count2==0:
        SQ3172Distance.append(float(SQ3172[i]))
        count2 += 1
        nrows2 += 1
        break
if len(SQ3172Distance)>maxValue:
    maxValue = len(SQ3172Distance)
        
SQ3173 = np.loadtxt('./distanceData/SQ3173Distance.csv', skiprows=1)
SQ3173Distance = []
count3 = 0
nrows3 = 0
for i in range(len(SQ3173)):
    if float(SQ3173[i])!=0 and float(SQ3173[i])<100 and count3==0:
        SQ3173Distance.append(float(SQ3173[i]))
        nrows3 += 1
    elif float(SQ3173[i])>100 and count3==0:
        SQ3173Distance.append(float(SQ3173[i]))
        count3 += 1
        nrows3 += 1
        break
if len(SQ3173Distance)>maxValue:
    maxValue = len(SQ3173Distance)
        
SQ3174 = np.loadtxt('./distanceData/SQ3174Distance.csv', skiprows=1)
SQ3174Distance = []
count4 = 0
nrows4 = 0
for i in range(len(SQ3174)):
    if float(SQ3174[i])!=0 and float(SQ3174[i])<100 and count4==0:
        SQ3174Distance.append(float(SQ3174[i]))
        nrows4 += 1
    elif float(SQ3174[i])>100 and count4==0:
        SQ3174Distance.append(float(SQ3174[i]))
        count4 += 1
        nrows4 += 1
        break
if len(SQ3174Distance)>maxValue:
    maxValue = len(SQ3174Distance)
        
SQ3175 = np.loadtxt('./distanceData/SQ3175Distance.csv', skiprows=1)
SQ3175Distance = []
count5 = 0
nrows5 = 0
for i in range(len(SQ3175)):
    if float(SQ3175[i])!=0 and float(SQ3175[i])<100 and count5==0:
        SQ3175Distance.append(float(SQ3175[i]))
        nrows5 += 1
    elif float(SQ3175[i])>100 and count5==0:
        SQ3175Distance.append(float(SQ3175[i]))
        count5 += 1
        nrows5 += 1
        break
if len(SQ3175Distance)>maxValue:
    maxValue = len(SQ3175Distance)
        
SQ3176 = np.loadtxt('./distanceData/SQ3176Distance.csv', skiprows=1)
SQ3176Distance = []
count6 = 0
nrows6 = 0
for i in range(len(SQ3176)):
    if float(SQ3176[i])!=0 and float(SQ3176[i])<100 and count6==0:
        SQ3176Distance.append(float(SQ3176[i]))
        nrows6 += 1
    elif float(SQ3176[i])>100 and count6==0:
        SQ3176Distance.append(float(SQ3176[i]))
        count6 += 1
        nrows6 += 1
        break
if len(SQ3176Distance)>maxValue:
    maxValue = len(SQ3176Distance)
        
SQ3177 = np.loadtxt('./distanceData/SQ3177Distance.csv', skiprows=1)
SQ3177Distance = []
count7 = 0
nrows7 = 0
for i in range(len(SQ3177)):
    if float(SQ3177[i])!=0 and float(SQ3177[i])<100 and count7==0:
        SQ3177Distance.append(float(SQ3177[i]))
        nrows7 += 1
    elif float(SQ3177[i])>100 and count7==0:
        SQ3177Distance.append(float(SQ3177[i]))
        count7 += 1
        nrows7 += 1
        break
if len(SQ3177Distance)>maxValue:
    maxValue = len(SQ3177Distance)
        
SQ3178 = np.loadtxt('./distanceData/SQ3178Distance.csv', skiprows=1)
SQ3178Distance = []
count8 = 0
nrows8 = 0
for i in range(len(SQ3178)):
    if float(SQ3178[i])!=0 and float(SQ3178[i])<100 and count8==0:
        SQ3178Distance.append(float(SQ3178[i]))
        nrows8 += 1
    elif float(SQ3178[i])>100 and count8==0:
        SQ3178Distance.append(float(SQ3178[i]))
        count8 += 1
        nrows8 += 1
        break
if len(SQ3178Distance)>maxValue:
    maxValue = len(SQ3178Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataSQ317.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataSQ317.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataSQ317.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataSQ317.csv', usecols=['Neptune'], nrows=maxValue)

SQ3171e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3171.csv', usecols=['e'], nrows=nrows1)
SQ3172e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3172.csv', usecols=['e'], nrows=nrows2)
SQ3173e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3173.csv', usecols=['e'], nrows=nrows3)
SQ3174e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3174.csv', usecols=['e'], nrows=nrows4)
SQ3175e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3175.csv', usecols=['e'], nrows=nrows5)
SQ3176e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3176.csv', usecols=['e'], nrows=nrows6)
SQ3177e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3177.csv', usecols=['e'], nrows=nrows7)
SQ3178e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3178.csv', usecols=['e'], nrows=nrows8)

SQ3171i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3171.csv', usecols=['i'], nrows=nrows1)
SQ3172i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3172.csv', usecols=['i'], nrows=nrows2)
SQ3173i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3173.csv', usecols=['i'], nrows=nrows3)
SQ3174i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3174.csv', usecols=['i'], nrows=nrows4)
SQ3175i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3175.csv', usecols=['i'], nrows=nrows5)
SQ3176i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3176.csv', usecols=['i'], nrows=nrows6)
SQ3177i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3177.csv', usecols=['i'], nrows=nrows7)
SQ3178i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SQ3178.csv', usecols=['i'], nrows=nrows8)

SQ3171iDeg = []
SQ3172iDeg = []
SQ3173iDeg = []
SQ3174iDeg = []
SQ3175iDeg = []
SQ3176iDeg = []
SQ3177iDeg = []
SQ3178iDeg = []

for j in range(nrows1):
    z = SQ3171i.values[j]
    rad = math.degrees(z)
    SQ3171iDeg.append(float(rad))
for j in range(nrows2):
    z = SQ3172i.values[j]
    rad = math.degrees(z)
    SQ3172iDeg.append(float(rad))
for j in range(nrows3):
    z = SQ3173i.values[j]
    rad = math.degrees(z)
    SQ3173iDeg.append(float(rad))
for j in range(nrows4):
    z = SQ3174i.values[j]
    rad = math.degrees(z)
    SQ3174iDeg.append(float(rad))
for j in range(nrows5):
    z = SQ3175i.values[j]
    rad = math.degrees(z)
    SQ3175iDeg.append(float(rad))
for j in range(nrows6):
    z = SQ3176i.values[j]
    rad = math.degrees(z)
    SQ3176iDeg.append(float(rad))
for j in range(nrows7):
    z = SQ3177i.values[j]
    rad = math.degrees(z)
    SQ3177iDeg.append(float(rad))
for j in range(nrows8):
    z = SQ3178i.values[j]
    rad = math.degrees(z)
    SQ3178iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(SQ3171Distance, color='blue', label='Clone 1')
ax1.plot(SQ3172Distance, color='green', label='Clone 2')
ax1.plot(SQ3173Distance, color='red', label='Clone 3')
ax1.plot(SQ3174Distance, color='brown', label='Clone 4')
ax1.plot(SQ3175Distance, color='purple', label='Clone 5')
ax1.plot(SQ3176Distance, color='orange', label='Clone 6')
ax1.plot(SQ3177Distance, color='grey', label='Clone 7')
ax1.plot(SQ3178Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(SQ3171e, color='blue', label='Clone 1')
ax2.plot(SQ3172e, color='green', label='Clone 2')
ax2.plot(SQ3173e, color='red', label='Clone 3')
ax2.plot(SQ3174e, color='brown', label='Clone 4')
ax2.plot(SQ3175e, color='purple', label='Clone 5')
ax2.plot(SQ3176e, color='orange', label='Clone 6')
ax2.plot(SQ3177e, color='grey', label='Clone 7')
ax2.plot(SQ3178e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.01,0.2)

ax3.plot(SQ3171iDeg, color='blue', label='Clone 1')
ax3.plot(SQ3172iDeg, color='green', label='Clone 2')
ax3.plot(SQ3173iDeg, color='red', label='Clone 3')
ax3.plot(SQ3174iDeg, color='brown', label='Clone 4')
ax3.plot(SQ3175iDeg, color='purple', label='Clone 5')
ax3.plot(SQ3176iDeg, color='orange', label='Clone 6')
ax3.plot(SQ3177iDeg, color='grey', label='Clone 7')
ax3.plot(SQ3178iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('SQ317')
fig = plt.savefig('./SQ317Figure.png', bbox_inches='tight')

