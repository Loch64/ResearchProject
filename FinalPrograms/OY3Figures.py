#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

OY31 = np.loadtxt('./distanceData/OY31Distance.csv', skiprows=1) #open('./distanceData/OY31Distance.csv').read().split('\n')
OY31Distance = []
count1 = 0
nrows1 = 0
for i in range(len(OY31)):
    if float(OY31[i])!=0 and float(OY31[i])<100 and count1==0:
        OY31Distance.append(float(OY31[i]))
        nrows1 += 1
    elif float(OY31[i])>100 and count1==0:
        OY31Distance.append(float(OY31[i]))
        count1 += 1
        nrows1 += 1
        break
if len(OY31Distance)>maxValue:
    maxValue = len(OY31Distance)

OY32 = np.loadtxt('./distanceData/OY32Distance.csv', skiprows=1)
OY32Distance = []
count2 = 0
nrows2 = 0
for i in range(len(OY32)):
    if float(OY32[i])!=0 and float(OY32[i])<100 and count2==0:
        OY32Distance.append(float(OY32[i]))
        nrows2 += 1
    elif float(OY32[i])>100 and count2==0:
        OY32Distance.append(float(OY32[i]))
        count2 += 1
        nrows2 += 1
        break
if len(OY32Distance)>maxValue:
    maxValue = len(OY32Distance)
        
OY33 = np.loadtxt('./distanceData/OY33Distance.csv', skiprows=1)
OY33Distance = []
count3 = 0
nrows3 = 0
for i in range(len(OY33)):
    if float(OY33[i])!=0 and float(OY33[i])<100 and count3==0:
        OY33Distance.append(float(OY33[i]))
        nrows3 += 1
    elif float(OY33[i])>100 and count3==0:
        OY33Distance.append(float(OY33[i]))
        count3 += 1
        nrows3 += 1
        break
if len(OY33Distance)>maxValue:
    maxValue = len(OY33Distance)
        
OY34 = np.loadtxt('./distanceData/OY34Distance.csv', skiprows=1)
OY34Distance = []
count4 = 0
nrows4 = 0
for i in range(len(OY34)):
    if float(OY34[i])!=0 and float(OY34[i])<100 and count4==0:
        OY34Distance.append(float(OY34[i]))
        nrows4 += 1
    elif float(OY34[i])>100 and count4==0:
        OY34Distance.append(float(OY34[i]))
        count4 += 1
        nrows4 += 1
        break
if len(OY34Distance)>maxValue:
    maxValue = len(OY34Distance)
        
OY35 = np.loadtxt('./distanceData/OY35Distance.csv', skiprows=1)
OY35Distance = []
count5 = 0
nrows5 = 0
for i in range(len(OY35)):
    if float(OY35[i])!=0 and float(OY35[i])<100 and count5==0:
        OY35Distance.append(float(OY35[i]))
        nrows5 += 1
    elif float(OY35[i])>100 and count5==0:
        OY35Distance.append(float(OY35[i]))
        count5 += 1
        nrows5 += 1
        break
if len(OY35Distance)>maxValue:
    maxValue = len(OY35Distance)
        
OY36 = np.loadtxt('./distanceData/OY36Distance.csv', skiprows=1)
OY36Distance = []
count6 = 0
nrows6 = 0
for i in range(len(OY36)):
    if float(OY36[i])!=0 and float(OY36[i])<100 and count6==0:
        OY36Distance.append(float(OY36[i]))
        nrows6 += 1
    elif float(OY36[i])>100 and count6==0:
        OY36Distance.append(float(OY36[i]))
        count6 += 1
        nrows6 += 1
        break
if len(OY36Distance)>maxValue:
    maxValue = len(OY36Distance)
        
OY37 = np.loadtxt('./distanceData/OY37Distance.csv', skiprows=1)
OY37Distance = []
count7 = 0
nrows7 = 0
for i in range(len(OY37)):
    if float(OY37[i])!=0 and float(OY37[i])<100 and count7==0:
        OY37Distance.append(float(OY37[i]))
        nrows7 += 1
    elif float(OY37[i])>100 and count7==0:
        OY37Distance.append(float(OY37[i]))
        count7 += 1
        nrows7 += 1
        break
if len(OY37Distance)>maxValue:
    maxValue = len(OY37Distance)
        
OY38 = np.loadtxt('./distanceData/OY38Distance.csv', skiprows=1)
OY38Distance = []
count8 = 0
nrows8 = 0
for i in range(len(OY38)):
    if float(OY38[i])!=0 and float(OY38[i])<100 and count8==0:
        OY38Distance.append(float(OY38[i]))
        nrows8 += 1
    elif float(OY38[i])>100 and count8==0:
        OY38Distance.append(float(OY38[i]))
        count8 += 1
        nrows8 += 1
        break
if len(OY38Distance)>maxValue:
    maxValue = len(OY38Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataOY3.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataOY3.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataOY3.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataOY3.csv', usecols=['Neptune'], nrows=maxValue)

OY31e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY31.csv', usecols=['e'], nrows=nrows1)
OY32e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY32.csv', usecols=['e'], nrows=nrows2)
OY33e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY33.csv', usecols=['e'], nrows=nrows3)
OY34e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY34.csv', usecols=['e'], nrows=nrows4)
OY35e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY35.csv', usecols=['e'], nrows=nrows5)
OY36e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY36.csv', usecols=['e'], nrows=nrows6)
OY37e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY37.csv', usecols=['e'], nrows=nrows7)
OY38e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY38.csv', usecols=['e'], nrows=nrows8)

OY31i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY31.csv', usecols=['i'], nrows=nrows1)
OY32i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY32.csv', usecols=['i'], nrows=nrows2)
OY33i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY33.csv', usecols=['i'], nrows=nrows3)
OY34i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY34.csv', usecols=['i'], nrows=nrows4)
OY35i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY35.csv', usecols=['i'], nrows=nrows5)
OY36i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY36.csv', usecols=['i'], nrows=nrows6)
OY37i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY37.csv', usecols=['i'], nrows=nrows7)
OY38i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OY38.csv', usecols=['i'], nrows=nrows8)

OY31iDeg = []
OY32iDeg = []
OY33iDeg = []
OY34iDeg = []
OY35iDeg = []
OY36iDeg = []
OY37iDeg = []
OY38iDeg = []

for j in range(nrows1):
    z = OY31i.values[j]
    rad = math.degrees(z)
    OY31iDeg.append(float(rad))
for j in range(nrows2):
    z = OY32i.values[j]
    rad = math.degrees(z)
    OY32iDeg.append(float(rad))
for j in range(nrows3):
    z = OY33i.values[j]
    rad = math.degrees(z)
    OY33iDeg.append(float(rad))
for j in range(nrows4):
    z = OY34i.values[j]
    rad = math.degrees(z)
    OY34iDeg.append(float(rad))
for j in range(nrows5):
    z = OY35i.values[j]
    rad = math.degrees(z)
    OY35iDeg.append(float(rad))
for j in range(nrows6):
    z = OY36i.values[j]
    rad = math.degrees(z)
    OY36iDeg.append(float(rad))
for j in range(nrows7):
    z = OY37i.values[j]
    rad = math.degrees(z)
    OY37iDeg.append(float(rad))
for j in range(nrows8):
    z = OY38i.values[j]
    rad = math.degrees(z)
    OY38iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(OY31Distance, color='blue', label='Clone 1')
ax1.plot(OY32Distance, color='green', label='Clone 2')
ax1.plot(OY33Distance, color='red', label='Clone 3')
ax1.plot(OY34Distance, color='brown', label='Clone 4')
ax1.plot(OY35Distance, color='purple', label='Clone 5')
ax1.plot(OY36Distance, color='orange', label='Clone 6')
ax1.plot(OY37Distance, color='grey', label='Clone 7')
ax1.plot(OY38Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(OY31e, color='blue', label='Clone 1')
ax2.plot(OY32e, color='green', label='Clone 2')
ax2.plot(OY33e, color='red', label='Clone 3')
ax2.plot(OY34e, color='brown', label='Clone 4')
ax2.plot(OY35e, color='purple', label='Clone 5')
ax2.plot(OY36e, color='orange', label='Clone 6')
ax2.plot(OY37e, color='grey', label='Clone 7')
ax2.plot(OY38e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.14,0.2)

ax3.plot(OY31iDeg, color='blue', label='Clone 1')
ax3.plot(OY32iDeg, color='green', label='Clone 2')
ax3.plot(OY33iDeg, color='red', label='Clone 3')
ax3.plot(OY34iDeg, color='brown', label='Clone 4')
ax3.plot(OY35iDeg, color='purple', label='Clone 5')
ax3.plot(OY36iDeg, color='orange', label='Clone 6')
ax3.plot(OY37iDeg, color='grey', label='Clone 7')
ax3.plot(OY38iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('OY3')
fig = plt.savefig('./OY3Figure.png', bbox_inches='tight')

