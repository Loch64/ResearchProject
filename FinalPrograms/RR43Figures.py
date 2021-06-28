#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

RR431 = np.loadtxt('./distanceData/RR431Distance.csv', skiprows=1) #open('./distanceData/RR431Distance.csv').read().split('\n')
RR431Distance = []
count1 = 0
nrows1 = 0
for i in range(len(RR431)):
    if float(RR431[i])!=0 and float(RR431[i])<100 and count1==0:
        RR431Distance.append(float(RR431[i]))
        nrows1 += 1
    elif float(RR431[i])>100 and count1==0:
        RR431Distance.append(float(RR431[i]))
        count1 += 1
        nrows1 += 1
        break
if len(RR431Distance)>maxValue:
    maxValue = len(RR431Distance)

RR432 = np.loadtxt('./distanceData/RR432Distance.csv', skiprows=1)
RR432Distance = []
count2 = 0
nrows2 = 0
for i in range(len(RR432)):
    if float(RR432[i])!=0 and float(RR432[i])<100 and count2==0:
        RR432Distance.append(float(RR432[i]))
        nrows2 += 1
    elif float(RR432[i])>100 and count2==0:
        RR432Distance.append(float(RR432[i]))
        count2 += 1
        nrows2 += 1
        break
if len(RR432Distance)>maxValue:
    maxValue = len(RR432Distance)
        
RR433 = np.loadtxt('./distanceData/RR433Distance.csv', skiprows=1)
RR433Distance = []
count3 = 0
nrows3 = 0
for i in range(len(RR433)):
    if float(RR433[i])!=0 and float(RR433[i])<100 and count3==0:
        RR433Distance.append(float(RR433[i]))
        nrows3 += 1
    elif float(RR433[i])>100 and count3==0:
        RR433Distance.append(float(RR433[i]))
        count3 += 1
        nrows3 += 1
        break
if len(RR433Distance)>maxValue:
    maxValue = len(RR433Distance)
        
RR434 = np.loadtxt('./distanceData/RR434Distance.csv', skiprows=1)
RR434Distance = []
count4 = 0
nrows4 = 0
for i in range(len(RR434)):
    if float(RR434[i])!=0 and float(RR434[i])<100 and count4==0:
        RR434Distance.append(float(RR434[i]))
        nrows4 += 1
    elif float(RR434[i])>100 and count4==0:
        RR434Distance.append(float(RR434[i]))
        count4 += 1
        nrows4 += 1
        break
if len(RR434Distance)>maxValue:
    maxValue = len(RR434Distance)
        
RR435 = np.loadtxt('./distanceData/RR435Distance.csv', skiprows=1)
RR435Distance = []
count5 = 0
nrows5 = 0
for i in range(len(RR435)):
    if float(RR435[i])!=0 and float(RR435[i])<100 and count5==0:
        RR435Distance.append(float(RR435[i]))
        nrows5 += 1
    elif float(RR435[i])>100 and count5==0:
        RR435Distance.append(float(RR435[i]))
        count5 += 1
        nrows5 += 1
        break
if len(RR435Distance)>maxValue:
    maxValue = len(RR435Distance)
        
RR436 = np.loadtxt('./distanceData/RR436Distance.csv', skiprows=1)
RR436Distance = []
count6 = 0
nrows6 = 0
for i in range(len(RR436)):
    if float(RR436[i])!=0 and float(RR436[i])<100 and count6==0:
        RR436Distance.append(float(RR436[i]))
        nrows6 += 1
    elif float(RR436[i])>100 and count6==0:
        RR436Distance.append(float(RR436[i]))
        count6 += 1
        nrows6 += 1
        break
if len(RR436Distance)>maxValue:
    maxValue = len(RR436Distance)
        
RR437 = np.loadtxt('./distanceData/RR437Distance.csv', skiprows=1)
RR437Distance = []
count7 = 0
nrows7 = 0
for i in range(len(RR437)):
    if float(RR437[i])!=0 and float(RR437[i])<100 and count7==0:
        RR437Distance.append(float(RR437[i]))
        nrows7 += 1
    elif float(RR437[i])>100 and count7==0:
        RR437Distance.append(float(RR437[i]))
        count7 += 1
        nrows7 += 1
        break
if len(RR437Distance)>maxValue:
    maxValue = len(RR437Distance)
        
RR438 = np.loadtxt('./distanceData/RR438Distance.csv', skiprows=1)
RR438Distance = []
count8 = 0
nrows8 = 0
for i in range(len(RR438)):
    if float(RR438[i])!=0 and float(RR438[i])<100 and count8==0:
        RR438Distance.append(float(RR438[i]))
        nrows8 += 1
    elif float(RR438[i])>100 and count8==0:
        RR438Distance.append(float(RR438[i]))
        count8 += 1
        nrows8 += 1
        break
if len(RR438Distance)>maxValue:
    maxValue = len(RR438Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataRR43.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataRR43.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataRR43.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataRR43.csv', usecols=['Neptune'], nrows=maxValue)

RR431e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR431.csv', usecols=['e'], nrows=nrows1)
RR432e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR432.csv', usecols=['e'], nrows=nrows2)
RR433e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR433.csv', usecols=['e'], nrows=nrows3)
RR434e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR434.csv', usecols=['e'], nrows=nrows4)
RR435e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR435.csv', usecols=['e'], nrows=nrows5)
RR436e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR436.csv', usecols=['e'], nrows=nrows6)
RR437e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR437.csv', usecols=['e'], nrows=nrows7)
RR438e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR438.csv', usecols=['e'], nrows=nrows8)

RR431i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR431.csv', usecols=['i'], nrows=nrows1)
RR432i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR432.csv', usecols=['i'], nrows=nrows2)
RR433i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR433.csv', usecols=['i'], nrows=nrows3)
RR434i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR434.csv', usecols=['i'], nrows=nrows4)
RR435i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR435.csv', usecols=['i'], nrows=nrows5)
RR436i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR436.csv', usecols=['i'], nrows=nrows6)
RR437i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR437.csv', usecols=['i'], nrows=nrows7)
RR438i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/RR438.csv', usecols=['i'], nrows=nrows8)

RR431iDeg = []
RR432iDeg = []
RR433iDeg = []
RR434iDeg = []
RR435iDeg = []
RR436iDeg = []
RR437iDeg = []
RR438iDeg = []

for j in range(nrows1):
    z = RR431i.values[j]
    rad = math.degrees(z)
    RR431iDeg.append(float(rad))
for j in range(nrows2):
    z = RR432i.values[j]
    rad = math.degrees(z)
    RR432iDeg.append(float(rad))
for j in range(nrows3):
    z = RR433i.values[j]
    rad = math.degrees(z)
    RR433iDeg.append(float(rad))
for j in range(nrows4):
    z = RR434i.values[j]
    rad = math.degrees(z)
    RR434iDeg.append(float(rad))
for j in range(nrows5):
    z = RR435i.values[j]
    rad = math.degrees(z)
    RR435iDeg.append(float(rad))
for j in range(nrows6):
    z = RR436i.values[j]
    rad = math.degrees(z)
    RR436iDeg.append(float(rad))
for j in range(nrows7):
    z = RR437i.values[j]
    rad = math.degrees(z)
    RR437iDeg.append(float(rad))
for j in range(nrows8):
    z = RR438i.values[j]
    rad = math.degrees(z)
    RR438iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(RR431Distance, color='blue', label='Clone 1')
ax1.plot(RR432Distance, color='green', label='Clone 2')
ax1.plot(RR433Distance, color='red', label='Clone 3')
ax1.plot(RR434Distance, color='brown', label='Clone 4')
ax1.plot(RR435Distance, color='purple', label='Clone 5')
ax1.plot(RR436Distance, color='orange', label='Clone 6')
ax1.plot(RR437Distance, color='grey', label='Clone 7')
ax1.plot(RR438Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(RR431e, color='blue', label='Clone 1')
ax2.plot(RR432e, color='green', label='Clone 2')
ax2.plot(RR433e, color='red', label='Clone 3')
ax2.plot(RR434e, color='brown', label='Clone 4')
ax2.plot(RR435e, color='purple', label='Clone 5')
ax2.plot(RR436e, color='orange', label='Clone 6')
ax2.plot(RR437e, color='grey', label='Clone 7')
ax2.plot(RR438e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.1,0.155)

ax3.plot(RR431iDeg, color='blue', label='Clone 1')
ax3.plot(RR432iDeg, color='green', label='Clone 2')
ax3.plot(RR433iDeg, color='red', label='Clone 3')
ax3.plot(RR434iDeg, color='brown', label='Clone 4')
ax3.plot(RR435iDeg, color='purple', label='Clone 5')
ax3.plot(RR436iDeg, color='orange', label='Clone 6')
ax3.plot(RR437iDeg, color='grey', label='Clone 7')
ax3.plot(RR438iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('RR43')
fig = plt.savefig('./RR43Figure.png', bbox_inches='tight')

