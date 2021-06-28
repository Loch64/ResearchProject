#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

TO661 = np.loadtxt('./distanceData/TO661Distance.csv', skiprows=1) #open('./distanceData/TO661Distance.csv').read().split('\n')
TO661Distance = []
count1 = 0
nrows1 = 0
for i in range(len(TO661)):
    if float(TO661[i])!=0 and float(TO661[i])<100 and count1==0:
        TO661Distance.append(float(TO661[i]))
        nrows1 += 1
    elif float(TO661[i])>100 and count1==0:
        TO661Distance.append(float(TO661[i]))
        count1 += 1
        nrows1 += 1
        break
if len(TO661Distance)>maxValue:
    maxValue = len(TO661Distance)

TO662 = np.loadtxt('./distanceData/TO662Distance.csv', skiprows=1)
TO662Distance = []
count2 = 0
nrows2 = 0
for i in range(len(TO662)):
    if float(TO662[i])!=0 and float(TO662[i])<100 and count2==0:
        TO662Distance.append(float(TO662[i]))
        nrows2 += 1
    elif float(TO662[i])>100 and count2==0:
        TO662Distance.append(float(TO662[i]))
        count2 += 1
        nrows2 += 1
        break
if len(TO662Distance)>maxValue:
    maxValue = len(TO662Distance)
        
TO663 = np.loadtxt('./distanceData/TO663Distance.csv', skiprows=1)
TO663Distance = []
count3 = 0
nrows3 = 0
for i in range(len(TO663)):
    if float(TO663[i])!=0 and float(TO663[i])<100 and count3==0:
        TO663Distance.append(float(TO663[i]))
        nrows3 += 1
    elif float(TO663[i])>100 and count3==0:
        TO663Distance.append(float(TO663[i]))
        count3 += 1
        nrows3 += 1
        break
if len(TO663Distance)>maxValue:
    maxValue = len(TO663Distance)
        
TO664 = np.loadtxt('./distanceData/TO664Distance.csv', skiprows=1)
TO664Distance = []
count4 = 0
nrows4 = 0
for i in range(len(TO664)):
    if float(TO664[i])!=0 and float(TO664[i])<100 and count4==0:
        TO664Distance.append(float(TO664[i]))
        nrows4 += 1
    elif float(TO664[i])>100 and count4==0:
        TO664Distance.append(float(TO664[i]))
        count4 += 1
        nrows4 += 1
        break
if len(TO664Distance)>maxValue:
    maxValue = len(TO664Distance)
        
TO665 = np.loadtxt('./distanceData/TO665Distance.csv', skiprows=1)
TO665Distance = []
count5 = 0
nrows5 = 0
for i in range(len(TO665)):
    if float(TO665[i])!=0 and float(TO665[i])<100 and count5==0:
        TO665Distance.append(float(TO665[i]))
        nrows5 += 1
    elif float(TO665[i])>100 and count5==0:
        TO665Distance.append(float(TO665[i]))
        count5 += 1
        nrows5 += 1
        break
if len(TO665Distance)>maxValue:
    maxValue = len(TO665Distance)
        
TO666 = np.loadtxt('./distanceData/TO666Distance.csv', skiprows=1)
TO666Distance = []
count6 = 0
nrows6 = 0
for i in range(len(TO666)):
    if float(TO666[i])!=0 and float(TO666[i])<100 and count6==0:
        TO666Distance.append(float(TO666[i]))
        nrows6 += 1
    elif float(TO666[i])>100 and count6==0:
        TO666Distance.append(float(TO666[i]))
        count6 += 1
        nrows6 += 1
        break
if len(TO666Distance)>maxValue:
    maxValue = len(TO666Distance)
        
TO667 = np.loadtxt('./distanceData/TO667Distance.csv', skiprows=1)
TO667Distance = []
count7 = 0
nrows7 = 0
for i in range(len(TO667)):
    if float(TO667[i])!=0 and float(TO667[i])<100 and count7==0:
        TO667Distance.append(float(TO667[i]))
        nrows7 += 1
    elif float(TO667[i])>100 and count7==0:
        TO667Distance.append(float(TO667[i]))
        count7 += 1
        nrows7 += 1
        break
if len(TO667Distance)>maxValue:
    maxValue = len(TO667Distance)
        
TO668 = np.loadtxt('./distanceData/TO668Distance.csv', skiprows=1)
TO668Distance = []
count8 = 0
nrows8 = 0
for i in range(len(TO668)):
    if float(TO668[i])!=0 and float(TO668[i])<100 and count8==0:
        TO668Distance.append(float(TO668[i]))
        nrows8 += 1
    elif float(TO668[i])>100 and count8==0:
        TO668Distance.append(float(TO668[i]))
        count8 += 1
        nrows8 += 1
        break
if len(TO668Distance)>maxValue:
    maxValue = len(TO668Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataTO66.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataTO66.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataTO66.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataTO66.csv', usecols=['Neptune'], nrows=maxValue)

TO661e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO661.csv', usecols=['e'], nrows=nrows1)
TO662e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO662.csv', usecols=['e'], nrows=nrows2)
TO663e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO663.csv', usecols=['e'], nrows=nrows3)
TO664e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO664.csv', usecols=['e'], nrows=nrows4)
TO665e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO665.csv', usecols=['e'], nrows=nrows5)
TO666e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO666.csv', usecols=['e'], nrows=nrows6)
TO667e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO667.csv', usecols=['e'], nrows=nrows7)
TO668e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO668.csv', usecols=['e'], nrows=nrows8)

TO661i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO661.csv', usecols=['i'], nrows=nrows1)
TO662i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO662.csv', usecols=['i'], nrows=nrows2)
TO663i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO663.csv', usecols=['i'], nrows=nrows3)
TO664i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO664.csv', usecols=['i'], nrows=nrows4)
TO665i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO665.csv', usecols=['i'], nrows=nrows5)
TO666i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO666.csv', usecols=['i'], nrows=nrows6)
TO667i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO667.csv', usecols=['i'], nrows=nrows7)
TO668i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/TO668.csv', usecols=['i'], nrows=nrows8)

TO661iDeg = []
TO662iDeg = []
TO663iDeg = []
TO664iDeg = []
TO665iDeg = []
TO666iDeg = []
TO667iDeg = []
TO668iDeg = []

for j in range(nrows1):
    z = TO661i.values[j]
    rad = math.degrees(z)
    TO661iDeg.append(float(rad))
for j in range(nrows2):
    z = TO662i.values[j]
    rad = math.degrees(z)
    TO662iDeg.append(float(rad))
for j in range(nrows3):
    z = TO663i.values[j]
    rad = math.degrees(z)
    TO663iDeg.append(float(rad))
for j in range(nrows4):
    z = TO664i.values[j]
    rad = math.degrees(z)
    TO664iDeg.append(float(rad))
for j in range(nrows5):
    z = TO665i.values[j]
    rad = math.degrees(z)
    TO665iDeg.append(float(rad))
for j in range(nrows6):
    z = TO666i.values[j]
    rad = math.degrees(z)
    TO666iDeg.append(float(rad))
for j in range(nrows7):
    z = TO667i.values[j]
    rad = math.degrees(z)
    TO667iDeg.append(float(rad))
for j in range(nrows8):
    z = TO668i.values[j]
    rad = math.degrees(z)
    TO668iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(TO661Distance, color='blue', label='Clone 1')
ax1.plot(TO662Distance, color='green', label='Clone 2')
ax1.plot(TO663Distance, color='red', label='Clone 3')
ax1.plot(TO664Distance, color='brown', label='Clone 4')
ax1.plot(TO665Distance, color='purple', label='Clone 5')
ax1.plot(TO666Distance, color='orange', label='Clone 6')
ax1.plot(TO667Distance, color='grey', label='Clone 7')
ax1.plot(TO668Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(TO661e, color='blue', label='Clone 1')
ax2.plot(TO662e, color='green', label='Clone 2')
ax2.plot(TO663e, color='red', label='Clone 3')
ax2.plot(TO664e, color='brown', label='Clone 4')
ax2.plot(TO665e, color='purple', label='Clone 5')
ax2.plot(TO666e, color='orange', label='Clone 6')
ax2.plot(TO667e, color='grey', label='Clone 7')
ax2.plot(TO668e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.09,0.145)

ax3.plot(TO661iDeg, color='blue', label='Clone 1')
ax3.plot(TO662iDeg, color='green', label='Clone 2')
ax3.plot(TO663iDeg, color='red', label='Clone 3')
ax3.plot(TO664iDeg, color='brown', label='Clone 4')
ax3.plot(TO665iDeg, color='purple', label='Clone 5')
ax3.plot(TO666iDeg, color='orange', label='Clone 6')
ax3.plot(TO667iDeg, color='grey', label='Clone 7')
ax3.plot(TO668iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('TO66')
fig = plt.savefig('./TO66Figure.png', bbox_inches='tight')

