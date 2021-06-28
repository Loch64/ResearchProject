#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

UQ5131 = np.loadtxt('./distanceData/UQ5131Distance.csv', skiprows=1) #open('./distanceData/UQ5131Distance.csv').read().split('\n')
UQ5131Distance = []
count1 = 0
nrows1 = 0
for i in range(len(UQ5131)):
    if float(UQ5131[i])!=0 and float(UQ5131[i])<100 and count1==0:
        UQ5131Distance.append(float(UQ5131[i]))
        nrows1 += 1
    elif float(UQ5131[i])>100 and count1==0:
        UQ5131Distance.append(float(UQ5131[i]))
        count1 += 1
        nrows1 += 1
        break
if len(UQ5131Distance)>maxValue:
    maxValue = len(UQ5131Distance)

UQ5132 = np.loadtxt('./distanceData/UQ5132Distance.csv', skiprows=1)
UQ5132Distance = []
count2 = 0
nrows2 = 0
for i in range(len(UQ5132)):
    if float(UQ5132[i])!=0 and float(UQ5132[i])<100 and count2==0:
        UQ5132Distance.append(float(UQ5132[i]))
        nrows2 += 1
    elif float(UQ5132[i])>100 and count2==0:
        UQ5132Distance.append(float(UQ5132[i]))
        count2 += 1
        nrows2 += 1
        break
if len(UQ5132Distance)>maxValue:
    maxValue = len(UQ5132Distance)
        
UQ5133 = np.loadtxt('./distanceData/UQ5133Distance.csv', skiprows=1)
UQ5133Distance = []
count3 = 0
nrows3 = 0
for i in range(len(UQ5133)):
    if float(UQ5133[i])!=0 and float(UQ5133[i])<100 and count3==0:
        UQ5133Distance.append(float(UQ5133[i]))
        nrows3 += 1
    elif float(UQ5133[i])>100 and count3==0:
        UQ5133Distance.append(float(UQ5133[i]))
        count3 += 1
        nrows3 += 1
        break
if len(UQ5133Distance)>maxValue:
    maxValue = len(UQ5133Distance)
        
UQ5134 = np.loadtxt('./distanceData/UQ5134Distance.csv', skiprows=1)
UQ5134Distance = []
count4 = 0
nrows4 = 0
for i in range(len(UQ5134)):
    if float(UQ5134[i])!=0 and float(UQ5134[i])<100 and count4==0:
        UQ5134Distance.append(float(UQ5134[i]))
        nrows4 += 1
    elif float(UQ5134[i])>100 and count4==0:
        UQ5134Distance.append(float(UQ5134[i]))
        count4 += 1
        nrows4 += 1
        break
if len(UQ5134Distance)>maxValue:
    maxValue = len(UQ5134Distance)
        
UQ5135 = np.loadtxt('./distanceData/UQ5135Distance.csv', skiprows=1)
UQ5135Distance = []
count5 = 0
nrows5 = 0
for i in range(len(UQ5135)):
    if float(UQ5135[i])!=0 and float(UQ5135[i])<100 and count5==0:
        UQ5135Distance.append(float(UQ5135[i]))
        nrows5 += 1
    elif float(UQ5135[i])>100 and count5==0:
        UQ5135Distance.append(float(UQ5135[i]))
        count5 += 1
        nrows5 += 1
        break
if len(UQ5135Distance)>maxValue:
    maxValue = len(UQ5135Distance)
        
UQ5136 = np.loadtxt('./distanceData/UQ5136Distance.csv', skiprows=1)
UQ5136Distance = []
count6 = 0
nrows6 = 0
for i in range(len(UQ5136)):
    if float(UQ5136[i])!=0 and float(UQ5136[i])<100 and count6==0:
        UQ5136Distance.append(float(UQ5136[i]))
        nrows6 += 1
    elif float(UQ5136[i])>100 and count6==0:
        UQ5136Distance.append(float(UQ5136[i]))
        count6 += 1
        nrows6 += 1
        break
if len(UQ5136Distance)>maxValue:
    maxValue = len(UQ5136Distance)
        
UQ5137 = np.loadtxt('./distanceData/UQ5137Distance.csv', skiprows=1)
UQ5137Distance = []
count7 = 0
nrows7 = 0
for i in range(len(UQ5137)):
    if float(UQ5137[i])!=0 and float(UQ5137[i])<100 and count7==0:
        UQ5137Distance.append(float(UQ5137[i]))
        nrows7 += 1
    elif float(UQ5137[i])>100 and count7==0:
        UQ5137Distance.append(float(UQ5137[i]))
        count7 += 1
        nrows7 += 1
        break
if len(UQ5137Distance)>maxValue:
    maxValue = len(UQ5137Distance)
        
UQ5138 = np.loadtxt('./distanceData/UQ5138Distance.csv', skiprows=1)
UQ5138Distance = []
count8 = 0
nrows8 = 0
for i in range(len(UQ5138)):
    if float(UQ5138[i])!=0 and float(UQ5138[i])<100 and count8==0:
        UQ5138Distance.append(float(UQ5138[i]))
        nrows8 += 1
    elif float(UQ5138[i])>100 and count8==0:
        UQ5138Distance.append(float(UQ5138[i]))
        count8 += 1
        nrows8 += 1
        break
if len(UQ5138Distance)>maxValue:
    maxValue = len(UQ5138Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataUQ513.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataUQ513.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataUQ513.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataUQ513.csv', usecols=['Neptune'], nrows=maxValue)

UQ5131e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5131.csv', usecols=['e'], nrows=nrows1)
UQ5132e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5132.csv', usecols=['e'], nrows=nrows2)
UQ5133e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5133.csv', usecols=['e'], nrows=nrows3)
UQ5134e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5134.csv', usecols=['e'], nrows=nrows4)
UQ5135e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5135.csv', usecols=['e'], nrows=nrows5)
UQ5136e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5136.csv', usecols=['e'], nrows=nrows6)
UQ5137e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5137.csv', usecols=['e'], nrows=nrows7)
UQ5138e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5138.csv', usecols=['e'], nrows=nrows8)

UQ5131i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5131.csv', usecols=['i'], nrows=nrows1)
UQ5132i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5132.csv', usecols=['i'], nrows=nrows2)
UQ5133i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5133.csv', usecols=['i'], nrows=nrows3)
UQ5134i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5134.csv', usecols=['i'], nrows=nrows4)
UQ5135i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5135.csv', usecols=['i'], nrows=nrows5)
UQ5136i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5136.csv', usecols=['i'], nrows=nrows6)
UQ5137i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5137.csv', usecols=['i'], nrows=nrows7)
UQ5138i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UQ5138.csv', usecols=['i'], nrows=nrows8)

UQ5131iDeg = []
UQ5132iDeg = []
UQ5133iDeg = []
UQ5134iDeg = []
UQ5135iDeg = []
UQ5136iDeg = []
UQ5137iDeg = []
UQ5138iDeg = []

for j in range(nrows1):
    z = UQ5131i.values[j]
    rad = math.degrees(z)
    UQ5131iDeg.append(float(rad))
for j in range(nrows2):
    z = UQ5132i.values[j]
    rad = math.degrees(z)
    UQ5132iDeg.append(float(rad))
for j in range(nrows3):
    z = UQ5133i.values[j]
    rad = math.degrees(z)
    UQ5133iDeg.append(float(rad))
for j in range(nrows4):
    z = UQ5134i.values[j]
    rad = math.degrees(z)
    UQ5134iDeg.append(float(rad))
for j in range(nrows5):
    z = UQ5135i.values[j]
    rad = math.degrees(z)
    UQ5135iDeg.append(float(rad))
for j in range(nrows6):
    z = UQ5136i.values[j]
    rad = math.degrees(z)
    UQ5136iDeg.append(float(rad))
for j in range(nrows7):
    z = UQ5137i.values[j]
    rad = math.degrees(z)
    UQ5137iDeg.append(float(rad))
for j in range(nrows8):
    z = UQ5138i.values[j]
    rad = math.degrees(z)
    UQ5138iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(UQ5131Distance, color='blue', label='Clone 1')
ax1.plot(UQ5132Distance, color='green', label='Clone 2')
ax1.plot(UQ5133Distance, color='red', label='Clone 3')
ax1.plot(UQ5134Distance, color='brown', label='Clone 4')
ax1.plot(UQ5135Distance, color='purple', label='Clone 5')
ax1.plot(UQ5136Distance, color='orange', label='Clone 6')
ax1.plot(UQ5137Distance, color='grey', label='Clone 7')
ax1.plot(UQ5138Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(UQ5131e, color='blue', label='Clone 1')
ax2.plot(UQ5132e, color='green', label='Clone 2')
ax2.plot(UQ5133e, color='red', label='Clone 3')
ax2.plot(UQ5134e, color='brown', label='Clone 4')
ax2.plot(UQ5135e, color='purple', label='Clone 5')
ax2.plot(UQ5136e, color='orange', label='Clone 6')
ax2.plot(UQ5137e, color='grey', label='Clone 7')
ax2.plot(UQ5138e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.12,0.18)

ax3.plot(UQ5131iDeg, color='blue', label='Clone 1')
ax3.plot(UQ5132iDeg, color='green', label='Clone 2')
ax3.plot(UQ5133iDeg, color='red', label='Clone 3')
ax3.plot(UQ5134iDeg, color='brown', label='Clone 4')
ax3.plot(UQ5135iDeg, color='purple', label='Clone 5')
ax3.plot(UQ5136iDeg, color='orange', label='Clone 6')
ax3.plot(UQ5137iDeg, color='grey', label='Clone 7')
ax3.plot(UQ5138iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('UQ513')
fig = plt.savefig('./UQ513Figure.png', bbox_inches='tight')

