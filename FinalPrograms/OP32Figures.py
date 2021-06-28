#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

OP321 = np.loadtxt('./distanceData/OP321Distance.csv', skiprows=1) #open('./distanceData/OP321Distance.csv').read().split('\n')
OP321Distance = []
count1 = 0
nrows1 = 0
for i in range(len(OP321)):
    if float(OP321[i])!=0 and float(OP321[i])<100 and count1==0:
        OP321Distance.append(float(OP321[i]))
        nrows1 += 1
    elif float(OP321[i])>100 and count1==0:
        OP321Distance.append(float(OP321[i]))
        count1 += 1
        nrows1 += 1
        break
if len(OP321Distance)>maxValue:
    maxValue = len(OP321Distance)

OP322 = np.loadtxt('./distanceData/OP322Distance.csv', skiprows=1)
OP322Distance = []
count2 = 0
nrows2 = 0
for i in range(len(OP322)):
    if float(OP322[i])!=0 and float(OP322[i])<100 and count2==0:
        OP322Distance.append(float(OP322[i]))
        nrows2 += 1
    elif float(OP322[i])>100 and count2==0:
        OP322Distance.append(float(OP322[i]))
        count2 += 1
        nrows2 += 1
        break
if len(OP322Distance)>maxValue:
    maxValue = len(OP322Distance)
        
OP323 = np.loadtxt('./distanceData/OP323Distance.csv', skiprows=1)
OP323Distance = []
count3 = 0
nrows3 = 0
for i in range(len(OP323)):
    if float(OP323[i])!=0 and float(OP323[i])<100 and count3==0:
        OP323Distance.append(float(OP323[i]))
        nrows3 += 1
    elif float(OP323[i])>100 and count3==0:
        OP323Distance.append(float(OP323[i]))
        count3 += 1
        nrows3 += 1
        break
if len(OP323Distance)>maxValue:
    maxValue = len(OP323Distance)
        
OP324 = np.loadtxt('./distanceData/OP324Distance.csv', skiprows=1)
OP324Distance = []
count4 = 0
nrows4 = 0
for i in range(len(OP324)):
    if float(OP324[i])!=0 and float(OP324[i])<100 and count4==0:
        OP324Distance.append(float(OP324[i]))
        nrows4 += 1
    elif float(OP324[i])>100 and count4==0:
        OP324Distance.append(float(OP324[i]))
        count4 += 1
        nrows4 += 1
        break
if len(OP324Distance)>maxValue:
    maxValue = len(OP324Distance)
        
OP325 = np.loadtxt('./distanceData/OP325Distance.csv', skiprows=1)
OP325Distance = []
count5 = 0
nrows5 = 0
for i in range(len(OP325)):
    if float(OP325[i])!=0 and float(OP325[i])<100 and count5==0:
        OP325Distance.append(float(OP325[i]))
        nrows5 += 1
    elif float(OP325[i])>100 and count5==0:
        OP325Distance.append(float(OP325[i]))
        count5 += 1
        nrows5 += 1
        break
if len(OP325Distance)>maxValue:
    maxValue = len(OP325Distance)
        
OP326 = np.loadtxt('./distanceData/OP326Distance.csv', skiprows=1)
OP326Distance = []
count6 = 0
nrows6 = 0
for i in range(len(OP326)):
    if float(OP326[i])!=0 and float(OP326[i])<100 and count6==0:
        OP326Distance.append(float(OP326[i]))
        nrows6 += 1
    elif float(OP326[i])>100 and count6==0:
        OP326Distance.append(float(OP326[i]))
        count6 += 1
        nrows6 += 1
        break
if len(OP326Distance)>maxValue:
    maxValue = len(OP326Distance)
        
OP327 = np.loadtxt('./distanceData/OP327Distance.csv', skiprows=1)
OP327Distance = []
count7 = 0
nrows7 = 0
for i in range(len(OP327)):
    if float(OP327[i])!=0 and float(OP327[i])<100 and count7==0:
        OP327Distance.append(float(OP327[i]))
        nrows7 += 1
    elif float(OP327[i])>100 and count7==0:
        OP327Distance.append(float(OP327[i]))
        count7 += 1
        nrows7 += 1
        break
if len(OP327Distance)>maxValue:
    maxValue = len(OP327Distance)
        
OP328 = np.loadtxt('./distanceData/OP328Distance.csv', skiprows=1)
OP328Distance = []
count8 = 0
nrows8 = 0
for i in range(len(OP328)):
    if float(OP328[i])!=0 and float(OP328[i])<100 and count8==0:
        OP328Distance.append(float(OP328[i]))
        nrows8 += 1
    elif float(OP328[i])>100 and count8==0:
        OP328Distance.append(float(OP328[i]))
        count8 += 1
        nrows8 += 1
        break
if len(OP328Distance)>maxValue:
    maxValue = len(OP328Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataOP32.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataOP32.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataOP32.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataOP32.csv', usecols=['Neptune'], nrows=maxValue)

OP321e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP321.csv', usecols=['e'], nrows=nrows1)
OP322e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP322.csv', usecols=['e'], nrows=nrows2)
OP323e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP323.csv', usecols=['e'], nrows=nrows3)
OP324e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP324.csv', usecols=['e'], nrows=nrows4)
OP325e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP325.csv', usecols=['e'], nrows=nrows5)
OP326e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP326.csv', usecols=['e'], nrows=nrows6)
OP327e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP327.csv', usecols=['e'], nrows=nrows7)
OP328e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP328.csv', usecols=['e'], nrows=nrows8)

OP321i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP321.csv', usecols=['i'], nrows=nrows1)
OP322i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP322.csv', usecols=['i'], nrows=nrows2)
OP323i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP323.csv', usecols=['i'], nrows=nrows3)
OP324i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP324.csv', usecols=['i'], nrows=nrows4)
OP325i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP325.csv', usecols=['i'], nrows=nrows5)
OP326i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP326.csv', usecols=['i'], nrows=nrows6)
OP327i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP327.csv', usecols=['i'], nrows=nrows7)
OP328i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/OP328.csv', usecols=['i'], nrows=nrows8)

OP321iDeg = []
OP322iDeg = []
OP323iDeg = []
OP324iDeg = []
OP325iDeg = []
OP326iDeg = []
OP327iDeg = []
OP328iDeg = []

for j in range(nrows1):
    z = OP321i.values[j]
    rad = math.degrees(z)
    OP321iDeg.append(float(rad))
for j in range(nrows2):
    z = OP322i.values[j]
    rad = math.degrees(z)
    OP322iDeg.append(float(rad))
for j in range(nrows3):
    z = OP323i.values[j]
    rad = math.degrees(z)
    OP323iDeg.append(float(rad))
for j in range(nrows4):
    z = OP324i.values[j]
    rad = math.degrees(z)
    OP324iDeg.append(float(rad))
for j in range(nrows5):
    z = OP325i.values[j]
    rad = math.degrees(z)
    OP325iDeg.append(float(rad))
for j in range(nrows6):
    z = OP326i.values[j]
    rad = math.degrees(z)
    OP326iDeg.append(float(rad))
for j in range(nrows7):
    z = OP327i.values[j]
    rad = math.degrees(z)
    OP327iDeg.append(float(rad))
for j in range(nrows8):
    z = OP328i.values[j]
    rad = math.degrees(z)
    OP328iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(OP321Distance, color='blue', label='Clone 1')
ax1.plot(OP322Distance, color='green', label='Clone 2')
ax1.plot(OP323Distance, color='red', label='Clone 3')
ax1.plot(OP324Distance, color='brown', label='Clone 4')
ax1.plot(OP325Distance, color='purple', label='Clone 5')
ax1.plot(OP326Distance, color='orange', label='Clone 6')
ax1.plot(OP327Distance, color='grey', label='Clone 7')
ax1.plot(OP328Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(OP321e, color='blue', label='Clone 1')
ax2.plot(OP322e, color='green', label='Clone 2')
ax2.plot(OP323e, color='red', label='Clone 3')
ax2.plot(OP324e, color='brown', label='Clone 4')
ax2.plot(OP325e, color='purple', label='Clone 5')
ax2.plot(OP326e, color='orange', label='Clone 6')
ax2.plot(OP327e, color='grey', label='Clone 7')
ax2.plot(OP328e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.08,0.12)

ax3.plot(OP321iDeg, color='blue', label='Clone 1')
ax3.plot(OP322iDeg, color='green', label='Clone 2')
ax3.plot(OP323iDeg, color='red', label='Clone 3')
ax3.plot(OP324iDeg, color='brown', label='Clone 4')
ax3.plot(OP325iDeg, color='purple', label='Clone 5')
ax3.plot(OP326iDeg, color='orange', label='Clone 6')
ax3.plot(OP327iDeg, color='grey', label='Clone 7')
ax3.plot(OP328iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('OP32')
fig = plt.savefig('./OP32Figure.png', bbox_inches='tight')

