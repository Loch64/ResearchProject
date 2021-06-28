#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

YE71 = np.loadtxt('./distanceData/YE71Distance.csv', skiprows=1) #open('./distanceData/YE71Distance.csv').read().split('\n')
YE71Distance = []
count1 = 0
nrows1 = 0
for i in range(len(YE71)):
    if float(YE71[i])!=0 and float(YE71[i])<100 and count1==0:
        YE71Distance.append(float(YE71[i]))
        nrows1 += 1
    elif float(YE71[i])>100 and count1==0:
        YE71Distance.append(float(YE71[i]))
        count1 += 1
        nrows1 += 1
        break
if len(YE71Distance)>maxValue:
    maxValue = len(YE71Distance)

YE72 = np.loadtxt('./distanceData/YE72Distance.csv', skiprows=1)
YE72Distance = []
count2 = 0
nrows2 = 0
for i in range(len(YE72)):
    if float(YE72[i])!=0 and float(YE72[i])<100 and count2==0:
        YE72Distance.append(float(YE72[i]))
        nrows2 += 1
    elif float(YE72[i])>100 and count2==0:
        YE72Distance.append(float(YE72[i]))
        count2 += 1
        nrows2 += 1
        break
if len(YE72Distance)>maxValue:
    maxValue = len(YE72Distance)
        
YE73 = np.loadtxt('./distanceData/YE73Distance.csv', skiprows=1)
YE73Distance = []
count3 = 0
nrows3 = 0
for i in range(len(YE73)):
    if float(YE73[i])!=0 and float(YE73[i])<100 and count3==0:
        YE73Distance.append(float(YE73[i]))
        nrows3 += 1
    elif float(YE73[i])>100 and count3==0:
        YE73Distance.append(float(YE73[i]))
        count3 += 1
        nrows3 += 1
        break
if len(YE73Distance)>maxValue:
    maxValue = len(YE73Distance)
        
YE74 = np.loadtxt('./distanceData/YE74Distance.csv', skiprows=1)
YE74Distance = []
count4 = 0
nrows4 = 0
for i in range(len(YE74)):
    if float(YE74[i])!=0 and float(YE74[i])<100 and count4==0:
        YE74Distance.append(float(YE74[i]))
        nrows4 += 1
    elif float(YE74[i])>100 and count4==0:
        YE74Distance.append(float(YE74[i]))
        count4 += 1
        nrows4 += 1
        break
if len(YE74Distance)>maxValue:
    maxValue = len(YE74Distance)
        
YE75 = np.loadtxt('./distanceData/YE75Distance.csv', skiprows=1)
YE75Distance = []
count5 = 0
nrows5 = 0
for i in range(len(YE75)):
    if float(YE75[i])!=0 and float(YE75[i])<100 and count5==0:
        YE75Distance.append(float(YE75[i]))
        nrows5 += 1
    elif float(YE75[i])>100 and count5==0:
        YE75Distance.append(float(YE75[i]))
        count5 += 1
        nrows5 += 1
        break
if len(YE75Distance)>maxValue:
    maxValue = len(YE75Distance)
        
YE76 = np.loadtxt('./distanceData/YE76Distance.csv', skiprows=1)
YE76Distance = []
count6 = 0
nrows6 = 0
for i in range(len(YE76)):
    if float(YE76[i])!=0 and float(YE76[i])<100 and count6==0:
        YE76Distance.append(float(YE76[i]))
        nrows6 += 1
    elif float(YE76[i])>100 and count6==0:
        YE76Distance.append(float(YE76[i]))
        count6 += 1
        nrows6 += 1
        break
if len(YE76Distance)>maxValue:
    maxValue = len(YE76Distance)
        
YE77 = np.loadtxt('./distanceData/YE77Distance.csv', skiprows=1)
YE77Distance = []
count7 = 0
nrows7 = 0
for i in range(len(YE77)):
    if float(YE77[i])!=0 and float(YE77[i])<100 and count7==0:
        YE77Distance.append(float(YE77[i]))
        nrows7 += 1
    elif float(YE77[i])>100 and count7==0:
        YE77Distance.append(float(YE77[i]))
        count7 += 1
        nrows7 += 1
        break
if len(YE77Distance)>maxValue:
    maxValue = len(YE77Distance)
        
YE78 = np.loadtxt('./distanceData/YE78Distance.csv', skiprows=1)
YE78Distance = []
count8 = 0
nrows8 = 0
for i in range(len(YE78)):
    if float(YE78[i])!=0 and float(YE78[i])<100 and count8==0:
        YE78Distance.append(float(YE78[i]))
        nrows8 += 1
    elif float(YE78[i])>100 and count8==0:
        YE78Distance.append(float(YE78[i]))
        count8 += 1
        nrows8 += 1
        break
if len(YE78Distance)>maxValue:
    maxValue = len(YE78Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataYE7.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataYE7.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataYE7.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataYE7.csv', usecols=['Neptune'], nrows=maxValue)

YE71e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE71.csv', usecols=['e'], nrows=nrows1)
YE72e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE72.csv', usecols=['e'], nrows=nrows2)
YE73e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE73.csv', usecols=['e'], nrows=nrows3)
YE74e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE74.csv', usecols=['e'], nrows=nrows4)
YE75e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE75.csv', usecols=['e'], nrows=nrows5)
YE76e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE76.csv', usecols=['e'], nrows=nrows6)
YE77e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE77.csv', usecols=['e'], nrows=nrows7)
YE78e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE78.csv', usecols=['e'], nrows=nrows8)

YE71i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE71.csv', usecols=['i'], nrows=nrows1)
YE72i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE72.csv', usecols=['i'], nrows=nrows2)
YE73i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE73.csv', usecols=['i'], nrows=nrows3)
YE74i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE74.csv', usecols=['i'], nrows=nrows4)
YE75i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE75.csv', usecols=['i'], nrows=nrows5)
YE76i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE76.csv', usecols=['i'], nrows=nrows6)
YE77i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE77.csv', usecols=['i'], nrows=nrows7)
YE78i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/YE78.csv', usecols=['i'], nrows=nrows8)

YE71iDeg = []
YE72iDeg = []
YE73iDeg = []
YE74iDeg = []
YE75iDeg = []
YE76iDeg = []
YE77iDeg = []
YE78iDeg = []

for j in range(nrows1):
    z = YE71i.values[j]
    rad = math.degrees(z)
    YE71iDeg.append(float(rad))
for j in range(nrows2):
    z = YE72i.values[j]
    rad = math.degrees(z)
    YE72iDeg.append(float(rad))
for j in range(nrows3):
    z = YE73i.values[j]
    rad = math.degrees(z)
    YE73iDeg.append(float(rad))
for j in range(nrows4):
    z = YE74i.values[j]
    rad = math.degrees(z)
    YE74iDeg.append(float(rad))
for j in range(nrows5):
    z = YE75i.values[j]
    rad = math.degrees(z)
    YE75iDeg.append(float(rad))
for j in range(nrows6):
    z = YE76i.values[j]
    rad = math.degrees(z)
    YE76iDeg.append(float(rad))
for j in range(nrows7):
    z = YE77i.values[j]
    rad = math.degrees(z)
    YE77iDeg.append(float(rad))
for j in range(nrows8):
    z = YE78i.values[j]
    rad = math.degrees(z)
    YE78iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(YE71Distance, color='blue', label='Clone 1')
ax1.plot(YE72Distance, color='green', label='Clone 2')
ax1.plot(YE73Distance, color='red', label='Clone 3')
ax1.plot(YE74Distance, color='brown', label='Clone 4')
ax1.plot(YE75Distance, color='purple', label='Clone 5')
ax1.plot(YE76Distance, color='orange', label='Clone 6')
ax1.plot(YE77Distance, color='grey', label='Clone 7')
ax1.plot(YE78Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(YE71e, color='blue', label='Clone 1')
ax2.plot(YE72e, color='green', label='Clone 2')
ax2.plot(YE73e, color='red', label='Clone 3')
ax2.plot(YE74e, color='brown', label='Clone 4')
ax2.plot(YE75e, color='purple', label='Clone 5')
ax2.plot(YE76e, color='orange', label='Clone 6')
ax2.plot(YE77e, color='grey', label='Clone 7')
ax2.plot(YE78e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.12,0.16)

ax3.plot(YE71iDeg, color='blue', label='Clone 1')
ax3.plot(YE72iDeg, color='green', label='Clone 2')
ax3.plot(YE73iDeg, color='red', label='Clone 3')
ax3.plot(YE74iDeg, color='brown', label='Clone 4')
ax3.plot(YE75iDeg, color='purple', label='Clone 5')
ax3.plot(YE76iDeg, color='orange', label='Clone 6')
ax3.plot(YE77iDeg, color='grey', label='Clone 7')
ax3.plot(YE78iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('YE7')
fig = plt.savefig('./YE7Figure.png', bbox_inches='tight')

