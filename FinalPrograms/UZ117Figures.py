#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

UZ1171 = np.loadtxt('./distanceData/UZ1171Distance.csv', skiprows=1) #open('./distanceData/UZ1171Distance.csv').read().split('\n')
UZ1171Distance = []
count1 = 0
nrows1 = 0
for i in range(len(UZ1171)):
    if float(UZ1171[i])!=0 and float(UZ1171[i])<100 and count1==0:
        UZ1171Distance.append(float(UZ1171[i]))
        nrows1 += 1
    elif float(UZ1171[i])>100 and count1==0:
        UZ1171Distance.append(float(UZ1171[i]))
        count1 += 1
        nrows1 += 1
        break
if len(UZ1171Distance)>maxValue:
    maxValue = len(UZ1171Distance)

UZ1172 = np.loadtxt('./distanceData/UZ1172Distance.csv', skiprows=1)
UZ1172Distance = []
count2 = 0
nrows2 = 0
for i in range(len(UZ1172)):
    if float(UZ1172[i])!=0 and float(UZ1172[i])<100 and count2==0:
        UZ1172Distance.append(float(UZ1172[i]))
        nrows2 += 1
    elif float(UZ1172[i])>100 and count2==0:
        UZ1172Distance.append(float(UZ1172[i]))
        count2 += 1
        nrows2 += 1
        break
if len(UZ1172Distance)>maxValue:
    maxValue = len(UZ1172Distance)
        
UZ1173 = np.loadtxt('./distanceData/UZ1173Distance.csv', skiprows=1)
UZ1173Distance = []
count3 = 0
nrows3 = 0
for i in range(len(UZ1173)):
    if float(UZ1173[i])!=0 and float(UZ1173[i])<100 and count3==0:
        UZ1173Distance.append(float(UZ1173[i]))
        nrows3 += 1
    elif float(UZ1173[i])>100 and count3==0:
        UZ1173Distance.append(float(UZ1173[i]))
        count3 += 1
        nrows3 += 1
        break
if len(UZ1173Distance)>maxValue:
    maxValue = len(UZ1173Distance)
        
UZ1174 = np.loadtxt('./distanceData/UZ1174Distance.csv', skiprows=1)
UZ1174Distance = []
count4 = 0
nrows4 = 0
for i in range(len(UZ1174)):
    if float(UZ1174[i])!=0 and float(UZ1174[i])<100 and count4==0:
        UZ1174Distance.append(float(UZ1174[i]))
        nrows4 += 1
    elif float(UZ1174[i])>100 and count4==0:
        UZ1174Distance.append(float(UZ1174[i]))
        count4 += 1
        nrows4 += 1
        break
if len(UZ1174Distance)>maxValue:
    maxValue = len(UZ1174Distance)
        
UZ1175 = np.loadtxt('./distanceData/UZ1175Distance.csv', skiprows=1)
UZ1175Distance = []
count5 = 0
nrows5 = 0
for i in range(len(UZ1175)):
    if float(UZ1175[i])!=0 and float(UZ1175[i])<100 and count5==0:
        UZ1175Distance.append(float(UZ1175[i]))
        nrows5 += 1
    elif float(UZ1175[i])>100 and count5==0:
        UZ1175Distance.append(float(UZ1175[i]))
        count5 += 1
        nrows5 += 1
        break
if len(UZ1175Distance)>maxValue:
    maxValue = len(UZ1175Distance)
        
UZ1176 = np.loadtxt('./distanceData/UZ1176Distance.csv', skiprows=1)
UZ1176Distance = []
count6 = 0
nrows6 = 0
for i in range(len(UZ1176)):
    if float(UZ1176[i])!=0 and float(UZ1176[i])<100 and count6==0:
        UZ1176Distance.append(float(UZ1176[i]))
        nrows6 += 1
    elif float(UZ1176[i])>100 and count6==0:
        UZ1176Distance.append(float(UZ1176[i]))
        count6 += 1
        nrows6 += 1
        break
if len(UZ1176Distance)>maxValue:
    maxValue = len(UZ1176Distance)
        
UZ1177 = np.loadtxt('./distanceData/UZ1177Distance.csv', skiprows=1)
UZ1177Distance = []
count7 = 0
nrows7 = 0
for i in range(len(UZ1177)):
    if float(UZ1177[i])!=0 and float(UZ1177[i])<100 and count7==0:
        UZ1177Distance.append(float(UZ1177[i]))
        nrows7 += 1
    elif float(UZ1177[i])>100 and count7==0:
        UZ1177Distance.append(float(UZ1177[i]))
        count7 += 1
        nrows7 += 1
        break
if len(UZ1177Distance)>maxValue:
    maxValue = len(UZ1177Distance)
        
UZ1178 = np.loadtxt('./distanceData/UZ1178Distance.csv', skiprows=1)
UZ1178Distance = []
count8 = 0
nrows8 = 0
for i in range(len(UZ1178)):
    if float(UZ1178[i])!=0 and float(UZ1178[i])<100 and count8==0:
        UZ1178Distance.append(float(UZ1178[i]))
        nrows8 += 1
    elif float(UZ1178[i])>100 and count8==0:
        UZ1178Distance.append(float(UZ1178[i]))
        count8 += 1
        nrows8 += 1
        break
if len(UZ1178Distance)>maxValue:
    maxValue = len(UZ1178Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Neptune'], nrows=maxValue)

UZ1171e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1171.csv', usecols=['e'], nrows=nrows1)
UZ1172e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1172.csv', usecols=['e'], nrows=nrows2)
UZ1173e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1173.csv', usecols=['e'], nrows=nrows3)
UZ1174e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1174.csv', usecols=['e'], nrows=nrows4)
UZ1175e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1175.csv', usecols=['e'], nrows=nrows5)
UZ1176e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1176.csv', usecols=['e'], nrows=nrows6)
UZ1177e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1177.csv', usecols=['e'], nrows=nrows7)
UZ1178e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1178.csv', usecols=['e'], nrows=nrows8)

UZ1171i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1171.csv', usecols=['i'], nrows=nrows1)
UZ1172i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1172.csv', usecols=['i'], nrows=nrows2)
UZ1173i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1173.csv', usecols=['i'], nrows=nrows3)
UZ1174i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1174.csv', usecols=['i'], nrows=nrows4)
UZ1175i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1175.csv', usecols=['i'], nrows=nrows5)
UZ1176i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1176.csv', usecols=['i'], nrows=nrows6)
UZ1177i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1177.csv', usecols=['i'], nrows=nrows7)
UZ1178i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1178.csv', usecols=['i'], nrows=nrows8)

UZ1171iDeg = []
UZ1172iDeg = []
UZ1173iDeg = []
UZ1174iDeg = []
UZ1175iDeg = []
UZ1176iDeg = []
UZ1177iDeg = []
UZ1178iDeg = []

for j in range(nrows1):
    z = UZ1171i.values[j]
    rad = math.degrees(z)
    UZ1171iDeg.append(float(rad))
for j in range(nrows2):
    z = UZ1172i.values[j]
    rad = math.degrees(z)
    UZ1172iDeg.append(float(rad))
for j in range(nrows3):
    z = UZ1173i.values[j]
    rad = math.degrees(z)
    UZ1173iDeg.append(float(rad))
for j in range(nrows4):
    z = UZ1174i.values[j]
    rad = math.degrees(z)
    UZ1174iDeg.append(float(rad))
for j in range(nrows5):
    z = UZ1175i.values[j]
    rad = math.degrees(z)
    UZ1175iDeg.append(float(rad))
for j in range(nrows6):
    z = UZ1176i.values[j]
    rad = math.degrees(z)
    UZ1176iDeg.append(float(rad))
for j in range(nrows7):
    z = UZ1177i.values[j]
    rad = math.degrees(z)
    UZ1177iDeg.append(float(rad))
for j in range(nrows8):
    z = UZ1178i.values[j]
    rad = math.degrees(z)
    UZ1178iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(UZ1171Distance, color='blue', label='Clone 1')
ax1.plot(UZ1172Distance, color='green', label='Clone 2')
ax1.plot(UZ1173Distance, color='red', label='Clone 3')
ax1.plot(UZ1174Distance, color='brown', label='Clone 4')
ax1.plot(UZ1175Distance, color='purple', label='Clone 5')
ax1.plot(UZ1176Distance, color='orange', label='Clone 6')
ax1.plot(UZ1177Distance, color='grey', label='Clone 7')
ax1.plot(UZ1178Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(UZ1171e, color='blue', label='Clone 1')
ax2.plot(UZ1172e, color='green', label='Clone 2')
ax2.plot(UZ1173e, color='red', label='Clone 3')
ax2.plot(UZ1174e, color='brown', label='Clone 4')
ax2.plot(UZ1175e, color='purple', label='Clone 5')
ax2.plot(UZ1176e, color='orange', label='Clone 6')
ax2.plot(UZ1177e, color='grey', label='Clone 7')
ax2.plot(UZ1178e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.01,1)

ax3.plot(UZ1171iDeg, color='blue', label='Clone 1')
ax3.plot(UZ1172iDeg, color='green', label='Clone 2')
ax3.plot(UZ1173iDeg, color='red', label='Clone 3')
ax3.plot(UZ1174iDeg, color='brown', label='Clone 4')
ax3.plot(UZ1175iDeg, color='purple', label='Clone 5')
ax3.plot(UZ1176iDeg, color='orange', label='Clone 6')
ax3.plot(UZ1177iDeg, color='grey', label='Clone 7')
ax3.plot(UZ1178iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(0.5,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('UZ117')
fig = plt.savefig('./UZ117Figure.png', bbox_inches='tight')

