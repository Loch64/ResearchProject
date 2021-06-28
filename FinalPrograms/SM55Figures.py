#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

SM551 = np.loadtxt('./distanceData/SM551Distance.csv', skiprows=1) #open('./distanceData/SM551Distance.csv').read().split('\n')
SM551Distance = []
count1 = 0
nrows1 = 0
for i in range(len(SM551)):
    if float(SM551[i])!=0 and float(SM551[i])<100 and count1==0:
        SM551Distance.append(float(SM551[i]))
        nrows1 += 1
    elif float(SM551[i])>100 and count1==0:
        SM551Distance.append(float(SM551[i]))
        count1 += 1
        nrows1 += 1
        break
if len(SM551Distance)>maxValue:
    maxValue = len(SM551Distance)

SM552 = np.loadtxt('./distanceData/SM552Distance.csv', skiprows=1)
SM552Distance = []
count2 = 0
nrows2 = 0
for i in range(len(SM552)):
    if float(SM552[i])!=0 and float(SM552[i])<100 and count2==0:
        SM552Distance.append(float(SM552[i]))
        nrows2 += 1
    elif float(SM552[i])>100 and count2==0:
        SM552Distance.append(float(SM552[i]))
        count2 += 1
        nrows2 += 1
        break
if len(SM552Distance)>maxValue:
    maxValue = len(SM552Distance)
        
SM553 = np.loadtxt('./distanceData/SM553Distance.csv', skiprows=1)
SM553Distance = []
count3 = 0
nrows3 = 0
for i in range(len(SM553)):
    if float(SM553[i])!=0 and float(SM553[i])<100 and count3==0:
        SM553Distance.append(float(SM553[i]))
        nrows3 += 1
    elif float(SM553[i])>100 and count3==0:
        SM553Distance.append(float(SM553[i]))
        count3 += 1
        nrows3 += 1
        break
if len(SM553Distance)>maxValue:
    maxValue = len(SM553Distance)
        
SM554 = np.loadtxt('./distanceData/SM554Distance.csv', skiprows=1)
SM554Distance = []
count4 = 0
nrows4 = 0
for i in range(len(SM554)):
    if float(SM554[i])!=0 and float(SM554[i])<100 and count4==0:
        SM554Distance.append(float(SM554[i]))
        nrows4 += 1
    elif float(SM554[i])>100 and count4==0:
        SM554Distance.append(float(SM554[i]))
        count4 += 1
        nrows4 += 1
        break
if len(SM554Distance)>maxValue:
    maxValue = len(SM554Distance)
        
SM555 = np.loadtxt('./distanceData/SM555Distance.csv', skiprows=1)
SM555Distance = []
count5 = 0
nrows5 = 0
for i in range(len(SM555)):
    if float(SM555[i])!=0 and float(SM555[i])<100 and count5==0:
        SM555Distance.append(float(SM555[i]))
        nrows5 += 1
    elif float(SM555[i])>100 and count5==0:
        SM555Distance.append(float(SM555[i]))
        count5 += 1
        nrows5 += 1
        break
if len(SM555Distance)>maxValue:
    maxValue = len(SM555Distance)
        
SM556 = np.loadtxt('./distanceData/SM556Distance.csv', skiprows=1)
SM556Distance = []
count6 = 0
nrows6 = 0
for i in range(len(SM556)):
    if float(SM556[i])!=0 and float(SM556[i])<100 and count6==0:
        SM556Distance.append(float(SM556[i]))
        nrows6 += 1
    elif float(SM556[i])>100 and count6==0:
        SM556Distance.append(float(SM556[i]))
        count6 += 1
        nrows6 += 1
        break
if len(SM556Distance)>maxValue:
    maxValue = len(SM556Distance)
        
SM557 = np.loadtxt('./distanceData/SM557Distance.csv', skiprows=1)
SM557Distance = []
count7 = 0
nrows7 = 0
for i in range(len(SM557)):
    if float(SM557[i])!=0 and float(SM557[i])<100 and count7==0:
        SM557Distance.append(float(SM557[i]))
        nrows7 += 1
    elif float(SM557[i])>100 and count7==0:
        SM557Distance.append(float(SM557[i]))
        count7 += 1
        nrows7 += 1
        break
if len(SM557Distance)>maxValue:
    maxValue = len(SM557Distance)
        
SM558 = np.loadtxt('./distanceData/SM558Distance.csv', skiprows=1)
SM558Distance = []
count8 = 0
nrows8 = 0
for i in range(len(SM558)):
    if float(SM558[i])!=0 and float(SM558[i])<100 and count8==0:
        SM558Distance.append(float(SM558[i]))
        nrows8 += 1
    elif float(SM558[i])>100 and count8==0:
        SM558Distance.append(float(SM558[i]))
        count8 += 1
        nrows8 += 1
        break
if len(SM558Distance)>maxValue:
    maxValue = len(SM558Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataSM55.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataSM55.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataSM55.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataSM55.csv', usecols=['Neptune'], nrows=maxValue)

SM551e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM551.csv', usecols=['e'], nrows=nrows1)
SM552e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM552.csv', usecols=['e'], nrows=nrows2)
SM553e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM553.csv', usecols=['e'], nrows=nrows3)
SM554e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM554.csv', usecols=['e'], nrows=nrows4)
SM555e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM555.csv', usecols=['e'], nrows=nrows5)
SM556e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM556.csv', usecols=['e'], nrows=nrows6)
SM557e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM557.csv', usecols=['e'], nrows=nrows7)
SM558e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM558.csv', usecols=['e'], nrows=nrows8)

SM551i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM551.csv', usecols=['i'], nrows=nrows1)
SM552i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM552.csv', usecols=['i'], nrows=nrows2)
SM553i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM553.csv', usecols=['i'], nrows=nrows3)
SM554i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM554.csv', usecols=['i'], nrows=nrows4)
SM555i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM555.csv', usecols=['i'], nrows=nrows5)
SM556i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM556.csv', usecols=['i'], nrows=nrows6)
SM557i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM557.csv', usecols=['i'], nrows=nrows7)
SM558i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/SM558.csv', usecols=['i'], nrows=nrows8)

SM551iDeg = []
SM552iDeg = []
SM553iDeg = []
SM554iDeg = []
SM555iDeg = []
SM556iDeg = []
SM557iDeg = []
SM558iDeg = []

for j in range(nrows1):
    z = SM551i.values[j]
    rad = math.degrees(z)
    SM551iDeg.append(float(rad))
for j in range(nrows2):
    z = SM552i.values[j]
    rad = math.degrees(z)
    SM552iDeg.append(float(rad))
for j in range(nrows3):
    z = SM553i.values[j]
    rad = math.degrees(z)
    SM553iDeg.append(float(rad))
for j in range(nrows4):
    z = SM554i.values[j]
    rad = math.degrees(z)
    SM554iDeg.append(float(rad))
for j in range(nrows5):
    z = SM555i.values[j]
    rad = math.degrees(z)
    SM555iDeg.append(float(rad))
for j in range(nrows6):
    z = SM556i.values[j]
    rad = math.degrees(z)
    SM556iDeg.append(float(rad))
for j in range(nrows7):
    z = SM557i.values[j]
    rad = math.degrees(z)
    SM557iDeg.append(float(rad))
for j in range(nrows8):
    z = SM558i.values[j]
    rad = math.degrees(z)
    SM558iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(SM551Distance, color='blue', label='Clone 1')
ax1.plot(SM552Distance, color='green', label='Clone 2')
ax1.plot(SM553Distance, color='red', label='Clone 3')
ax1.plot(SM554Distance, color='brown', label='Clone 4')
ax1.plot(SM555Distance, color='purple', label='Clone 5')
ax1.plot(SM556Distance, color='orange', label='Clone 6')
ax1.plot(SM557Distance, color='grey', label='Clone 7')
ax1.plot(SM558Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(SM551e, color='blue', label='Clone 1')
ax2.plot(SM552e, color='green', label='Clone 2')
ax2.plot(SM553e, color='red', label='Clone 3')
ax2.plot(SM554e, color='brown', label='Clone 4')
ax2.plot(SM555e, color='purple', label='Clone 5')
ax2.plot(SM556e, color='orange', label='Clone 6')
ax2.plot(SM557e, color='grey', label='Clone 7')
ax2.plot(SM558e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.08,0.12)

ax3.plot(SM551iDeg, color='blue', label='Clone 1')
ax3.plot(SM552iDeg, color='green', label='Clone 2')
ax3.plot(SM553iDeg, color='red', label='Clone 3')
ax3.plot(SM554iDeg, color='brown', label='Clone 4')
ax3.plot(SM555iDeg, color='purple', label='Clone 5')
ax3.plot(SM556iDeg, color='orange', label='Clone 6')
ax3.plot(SM557iDeg, color='grey', label='Clone 7')
ax3.plot(SM558iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('SM55')
fig = plt.savefig('./SM55Figure.png', bbox_inches='tight')

