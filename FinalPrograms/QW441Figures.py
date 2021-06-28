#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

QW4411 = np.loadtxt('./distanceData/QW4411Distance.csv', skiprows=1) #open('./distanceData/QW4411Distance.csv').read().split('\n')
QW4411Distance = []
count1 = 0
nrows1 = 0
for i in range(len(QW4411)):
    if float(QW4411[i])!=0 and float(QW4411[i])<100 and count1==0:
        QW4411Distance.append(float(QW4411[i]))
        nrows1 += 1
    elif float(QW4411[i])>100 and count1==0:
        QW4411Distance.append(float(QW4411[i]))
        count1 += 1
        nrows1 += 1
        break
if len(QW4411Distance)>maxValue:
    maxValue = len(QW4411Distance)

QW4412 = np.loadtxt('./distanceData/QW4412Distance.csv', skiprows=1)
QW4412Distance = []
count2 = 0
nrows2 = 0
for i in range(len(QW4412)):
    if float(QW4412[i])!=0 and float(QW4412[i])<100 and count2==0:
        QW4412Distance.append(float(QW4412[i]))
        nrows2 += 1
    elif float(QW4412[i])>100 and count2==0:
        QW4412Distance.append(float(QW4412[i]))
        count2 += 1
        nrows2 += 1
        break
if len(QW4412Distance)>maxValue:
    maxValue = len(QW4412Distance)
        
QW4413 = np.loadtxt('./distanceData/QW4413Distance.csv', skiprows=1)
QW4413Distance = []
count3 = 0
nrows3 = 0
for i in range(len(QW4413)):
    if float(QW4413[i])!=0 and float(QW4413[i])<100 and count3==0:
        QW4413Distance.append(float(QW4413[i]))
        nrows3 += 1
    elif float(QW4413[i])>100 and count3==0:
        QW4413Distance.append(float(QW4413[i]))
        count3 += 1
        nrows3 += 1
        break
if len(QW4413Distance)>maxValue:
    maxValue = len(QW4413Distance)
        
QW4414 = np.loadtxt('./distanceData/QW4414Distance.csv', skiprows=1)
QW4414Distance = []
count4 = 0
nrows4 = 0
for i in range(len(QW4414)):
    if float(QW4414[i])!=0 and float(QW4414[i])<100 and count4==0:
        QW4414Distance.append(float(QW4414[i]))
        nrows4 += 1
    elif float(QW4414[i])>100 and count4==0:
        QW4414Distance.append(float(QW4414[i]))
        count4 += 1
        nrows4 += 1
        break
if len(QW4414Distance)>maxValue:
    maxValue = len(QW4414Distance)
        
QW4415 = np.loadtxt('./distanceData/QW4415Distance.csv', skiprows=1)
QW4415Distance = []
count5 = 0
nrows5 = 0
for i in range(len(QW4415)):
    if float(QW4415[i])!=0 and float(QW4415[i])<100 and count5==0:
        QW4415Distance.append(float(QW4415[i]))
        nrows5 += 1
    elif float(QW4415[i])>100 and count5==0:
        QW4415Distance.append(float(QW4415[i]))
        count5 += 1
        nrows5 += 1
        break
if len(QW4415Distance)>maxValue:
    maxValue = len(QW4415Distance)
        
QW4416 = np.loadtxt('./distanceData/QW4416Distance.csv', skiprows=1)
QW4416Distance = []
count6 = 0
nrows6 = 0
for i in range(len(QW4416)):
    if float(QW4416[i])!=0 and float(QW4416[i])<100 and count6==0:
        QW4416Distance.append(float(QW4416[i]))
        nrows6 += 1
    elif float(QW4416[i])>100 and count6==0:
        QW4416Distance.append(float(QW4416[i]))
        count6 += 1
        nrows6 += 1
        break
if len(QW4416Distance)>maxValue:
    maxValue = len(QW4416Distance)
        
QW4417 = np.loadtxt('./distanceData/QW4417Distance.csv', skiprows=1)
QW4417Distance = []
count7 = 0
nrows7 = 0
for i in range(len(QW4417)):
    if float(QW4417[i])!=0 and float(QW4417[i])<100 and count7==0:
        QW4417Distance.append(float(QW4417[i]))
        nrows7 += 1
    elif float(QW4417[i])>100 and count7==0:
        QW4417Distance.append(float(QW4417[i]))
        count7 += 1
        nrows7 += 1
        break
if len(QW4417Distance)>maxValue:
    maxValue = len(QW4417Distance)
        
QW4418 = np.loadtxt('./distanceData/QW4418Distance.csv', skiprows=1)
QW4418Distance = []
count8 = 0
nrows8 = 0
for i in range(len(QW4418)):
    if float(QW4418[i])!=0 and float(QW4418[i])<100 and count8==0:
        QW4418Distance.append(float(QW4418[i]))
        nrows8 += 1
    elif float(QW4418[i])>100 and count8==0:
        QW4418Distance.append(float(QW4418[i]))
        count8 += 1
        nrows8 += 1
        break
if len(QW4418Distance)>maxValue:
    maxValue = len(QW4418Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataQW441.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataQW441.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataQW441.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataQW441.csv', usecols=['Neptune'], nrows=maxValue)

QW4411e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4411.csv', usecols=['e'], nrows=nrows1)
QW4412e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4412.csv', usecols=['e'], nrows=nrows2)
QW4413e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4413.csv', usecols=['e'], nrows=nrows3)
QW4414e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4414.csv', usecols=['e'], nrows=nrows4)
QW4415e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4415.csv', usecols=['e'], nrows=nrows5)
QW4416e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4416.csv', usecols=['e'], nrows=nrows6)
QW4417e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4417.csv', usecols=['e'], nrows=nrows7)
QW4418e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4418.csv', usecols=['e'], nrows=nrows8)

QW4411i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4411.csv', usecols=['i'], nrows=nrows1)
QW4412i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4412.csv', usecols=['i'], nrows=nrows2)
QW4413i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4413.csv', usecols=['i'], nrows=nrows3)
QW4414i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4414.csv', usecols=['i'], nrows=nrows4)
QW4415i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4415.csv', usecols=['i'], nrows=nrows5)
QW4416i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4416.csv', usecols=['i'], nrows=nrows6)
QW4417i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4417.csv', usecols=['i'], nrows=nrows7)
QW4418i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/QW4418.csv', usecols=['i'], nrows=nrows8)

QW4411iDeg = []
QW4412iDeg = []
QW4413iDeg = []
QW4414iDeg = []
QW4415iDeg = []
QW4416iDeg = []
QW4417iDeg = []
QW4418iDeg = []

for j in range(nrows1):
    z = QW4411i.values[j]
    rad = math.degrees(z)
    QW4411iDeg.append(float(rad))
for j in range(nrows2):
    z = QW4412i.values[j]
    rad = math.degrees(z)
    QW4412iDeg.append(float(rad))
for j in range(nrows3):
    z = QW4413i.values[j]
    rad = math.degrees(z)
    QW4413iDeg.append(float(rad))
for j in range(nrows4):
    z = QW4414i.values[j]
    rad = math.degrees(z)
    QW4414iDeg.append(float(rad))
for j in range(nrows5):
    z = QW4415i.values[j]
    rad = math.degrees(z)
    QW4415iDeg.append(float(rad))
for j in range(nrows6):
    z = QW4416i.values[j]
    rad = math.degrees(z)
    QW4416iDeg.append(float(rad))
for j in range(nrows7):
    z = QW4417i.values[j]
    rad = math.degrees(z)
    QW4417iDeg.append(float(rad))
for j in range(nrows8):
    z = QW4418i.values[j]
    rad = math.degrees(z)
    QW4418iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(QW4411Distance, color='blue', label='Clone 1')
ax1.plot(QW4412Distance, color='green', label='Clone 2')
ax1.plot(QW4413Distance, color='red', label='Clone 3')
ax1.plot(QW4414Distance, color='brown', label='Clone 4')
ax1.plot(QW4415Distance, color='purple', label='Clone 5')
ax1.plot(QW4416Distance, color='orange', label='Clone 6')
ax1.plot(QW4417Distance, color='grey', label='Clone 7')
ax1.plot(QW4418Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(QW4411e, color='blue', label='Clone 1')
ax2.plot(QW4412e, color='green', label='Clone 2')
ax2.plot(QW4413e, color='red', label='Clone 3')
ax2.plot(QW4414e, color='brown', label='Clone 4')
ax2.plot(QW4415e, color='purple', label='Clone 5')
ax2.plot(QW4416e, color='orange', label='Clone 6')
ax2.plot(QW4417e, color='grey', label='Clone 7')
ax2.plot(QW4418e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.08,0.12)

ax3.plot(QW4411iDeg, color='blue', label='Clone 1')
ax3.plot(QW4412iDeg, color='green', label='Clone 2')
ax3.plot(QW4413iDeg, color='red', label='Clone 3')
ax3.plot(QW4414iDeg, color='brown', label='Clone 4')
ax3.plot(QW4415iDeg, color='purple', label='Clone 5')
ax3.plot(QW4416iDeg, color='orange', label='Clone 6')
ax3.plot(QW4417iDeg, color='grey', label='Clone 7')
ax3.plot(QW4418iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('QW441')
fig = plt.savefig('./QW441Figure.png', bbox_inches='tight')

