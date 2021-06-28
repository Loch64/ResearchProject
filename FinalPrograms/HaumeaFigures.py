#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

Haumea1 = np.loadtxt('./distanceData/Haumea1Distance.csv', skiprows=1) #open('./distanceData/Haumea1Distance.csv').read().split('\n')
Haumea1Distance = []
count1 = 0
nrows1 = 0
for i in range(len(Haumea1)):
    if float(Haumea1[i])!=0 and float(Haumea1[i])<100 and count1==0:
        Haumea1Distance.append(float(Haumea1[i]))
        nrows1 += 1
    elif float(Haumea1[i])>100 and count1==0:
        Haumea1Distance.append(float(Haumea1[i]))
        count1 += 1
        nrows1 += 1
        break
if len(Haumea1Distance)>maxValue:
    maxValue = len(Haumea1Distance)

Haumea2 = np.loadtxt('./distanceData/Haumea2Distance.csv', skiprows=1)
Haumea2Distance = []
count2 = 0
nrows2 = 0
for i in range(len(Haumea2)):
    if float(Haumea2[i])!=0 and float(Haumea2[i])<100 and count2==0:
        Haumea2Distance.append(float(Haumea2[i]))
        nrows2 += 1
    elif float(Haumea2[i])>100 and count2==0:
        Haumea2Distance.append(float(Haumea2[i]))
        count2 += 1
        nrows2 += 1
        break
if len(Haumea2Distance)>maxValue:
    maxValue = len(Haumea2Distance)
        
Haumea3 = np.loadtxt('./distanceData/Haumea3Distance.csv', skiprows=1)
Haumea3Distance = []
count3 = 0
nrows3 = 0
for i in range(len(Haumea3)):
    if float(Haumea3[i])!=0 and float(Haumea3[i])<100 and count3==0:
        Haumea3Distance.append(float(Haumea3[i]))
        nrows3 += 1
    elif float(Haumea3[i])>100 and count3==0:
        Haumea3Distance.append(float(Haumea3[i]))
        count3 += 1
        nrows3 += 1
        break
if len(Haumea3Distance)>maxValue:
    maxValue = len(Haumea3Distance)
        
Haumea4 = np.loadtxt('./distanceData/Haumea4Distance.csv', skiprows=1)
Haumea4Distance = []
count4 = 0
nrows4 = 0
for i in range(len(Haumea4)):
    if float(Haumea4[i])!=0 and float(Haumea4[i])<100 and count4==0:
        Haumea4Distance.append(float(Haumea4[i]))
        nrows4 += 1
    elif float(Haumea4[i])>100 and count4==0:
        Haumea4Distance.append(float(Haumea4[i]))
        count4 += 1
        nrows4 += 1
        break
if len(Haumea4Distance)>maxValue:
    maxValue = len(Haumea4Distance)
        
Haumea5 = np.loadtxt('./distanceData/Haumea5Distance.csv', skiprows=1)
Haumea5Distance = []
count5 = 0
nrows5 = 0
for i in range(len(Haumea5)):
    if float(Haumea5[i])!=0 and float(Haumea5[i])<100 and count5==0:
        Haumea5Distance.append(float(Haumea5[i]))
        nrows5 += 1
    elif float(Haumea5[i])>100 and count5==0:
        Haumea5Distance.append(float(Haumea5[i]))
        count5 += 1
        nrows5 += 1
        break
if len(Haumea5Distance)>maxValue:
    maxValue = len(Haumea5Distance)
        
Haumea6 = np.loadtxt('./distanceData/Haumea6Distance.csv', skiprows=1)
Haumea6Distance = []
count6 = 0
nrows6 = 0
for i in range(len(Haumea6)):
    if float(Haumea6[i])!=0 and float(Haumea6[i])<100 and count6==0:
        Haumea6Distance.append(float(Haumea6[i]))
        nrows6 += 1
    elif float(Haumea6[i])>100 and count6==0:
        Haumea6Distance.append(float(Haumea6[i]))
        count6 += 1
        nrows6 += 1
        break
if len(Haumea6Distance)>maxValue:
    maxValue = len(Haumea6Distance)
        
Haumea7 = np.loadtxt('./distanceData/Haumea7Distance.csv', skiprows=1)
Haumea7Distance = []
count7 = 0
nrows7 = 0
for i in range(len(Haumea7)):
    if float(Haumea7[i])!=0 and float(Haumea7[i])<100 and count7==0:
        Haumea7Distance.append(float(Haumea7[i]))
        nrows7 += 1
    elif float(Haumea7[i])>100 and count7==0:
        Haumea7Distance.append(float(Haumea7[i]))
        count7 += 1
        nrows7 += 1
        break
if len(Haumea7Distance)>maxValue:
    maxValue = len(Haumea7Distance)
        
Haumea8 = np.loadtxt('./distanceData/Haumea8Distance.csv', skiprows=1)
Haumea8Distance = []
count8 = 0
nrows8 = 0
for i in range(len(Haumea8)):
    if float(Haumea8[i])!=0 and float(Haumea8[i])<100 and count8==0:
        Haumea8Distance.append(float(Haumea8[i]))
        nrows8 += 1
    elif float(Haumea8[i])>100 and count8==0:
        Haumea8Distance.append(float(Haumea8[i]))
        count8 += 1
        nrows8 += 1
        break
if len(Haumea8Distance)>maxValue:
    maxValue = len(Haumea8Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Neptune'], nrows=maxValue)

Haumea1e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea1.csv', usecols=['e'], nrows=nrows1)
Haumea2e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea2.csv', usecols=['e'], nrows=nrows2)
Haumea3e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea3.csv', usecols=['e'], nrows=nrows3)
Haumea4e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea4.csv', usecols=['e'], nrows=nrows4)
Haumea5e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea5.csv', usecols=['e'], nrows=nrows5)
Haumea6e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea6.csv', usecols=['e'], nrows=nrows6)
Haumea7e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea7.csv', usecols=['e'], nrows=nrows7)
Haumea8e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea8.csv', usecols=['e'], nrows=nrows8)

Haumea1i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea1.csv', usecols=['i'], nrows=nrows1)
Haumea2i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea2.csv', usecols=['i'], nrows=nrows2)
Haumea3i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea3.csv', usecols=['i'], nrows=nrows3)
Haumea4i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea4.csv', usecols=['i'], nrows=nrows4)
Haumea5i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea5.csv', usecols=['i'], nrows=nrows5)
Haumea6i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea6.csv', usecols=['i'], nrows=nrows6)
Haumea7i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea7.csv', usecols=['i'], nrows=nrows7)
Haumea8i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea8.csv', usecols=['i'], nrows=nrows8)

Haumea1iDeg = []
Haumea2iDeg = []
Haumea3iDeg = []
Haumea4iDeg = []
Haumea5iDeg = []
Haumea6iDeg = []
Haumea7iDeg = []
Haumea8iDeg = []

for j in range(nrows1):
    z = Haumea1i.values[j]
    rad = math.degrees(z)
    Haumea1iDeg.append(float(rad))
for j in range(nrows2):
    z = Haumea2i.values[j]
    rad = math.degrees(z)
    Haumea2iDeg.append(float(rad))
for j in range(nrows3):
    z = Haumea3i.values[j]
    rad = math.degrees(z)
    Haumea3iDeg.append(float(rad))
for j in range(nrows4):
    z = Haumea4i.values[j]
    rad = math.degrees(z)
    Haumea4iDeg.append(float(rad))
for j in range(nrows5):
    z = Haumea5i.values[j]
    rad = math.degrees(z)
    Haumea5iDeg.append(float(rad))
for j in range(nrows6):
    z = Haumea6i.values[j]
    rad = math.degrees(z)
    Haumea6iDeg.append(float(rad))
for j in range(nrows7):
    z = Haumea7i.values[j]
    rad = math.degrees(z)
    Haumea7iDeg.append(float(rad))
for j in range(nrows8):
    z = Haumea8i.values[j]
    rad = math.degrees(z)
    Haumea8iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(Haumea1Distance, color='blue', label='Clone 1')
ax1.plot(Haumea2Distance, color='green', label='Clone 2')
ax1.plot(Haumea3Distance, color='red', label='Clone 3')
ax1.plot(Haumea4Distance, color='brown', label='Clone 4')
ax1.plot(Haumea5Distance, color='purple', label='Clone 5')
ax1.plot(Haumea6Distance, color='orange', label='Clone 6')
ax1.plot(Haumea7Distance, color='grey', label='Clone 7')
ax1.plot(Haumea8Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(Haumea1e, color='blue', label='Clone 1')
ax2.plot(Haumea2e, color='green', label='Clone 2')
ax2.plot(Haumea3e, color='red', label='Clone 3')
ax2.plot(Haumea4e, color='brown', label='Clone 4')
ax2.plot(Haumea5e, color='purple', label='Clone 5')
ax2.plot(Haumea6e, color='orange', label='Clone 6')
ax2.plot(Haumea7e, color='grey', label='Clone 7')
ax2.plot(Haumea8e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.01,0.8)

ax3.plot(Haumea1iDeg, color='blue', label='Clone 1')
ax3.plot(Haumea2iDeg, color='green', label='Clone 2')
ax3.plot(Haumea3iDeg, color='red', label='Clone 3')
ax3.plot(Haumea4iDeg, color='brown', label='Clone 4')
ax3.plot(Haumea5iDeg, color='purple', label='Clone 5')
ax3.plot(Haumea6iDeg, color='orange', label='Clone 6')
ax3.plot(Haumea7iDeg, color='grey', label='Clone 7')
ax3.plot(Haumea8iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(0.57,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('Haumea')
fig = plt.savefig('./HaumeaFigure.png', bbox_inches='tight')

