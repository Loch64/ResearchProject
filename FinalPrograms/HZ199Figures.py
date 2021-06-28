#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

HZ1991 = np.loadtxt('./distanceData/HZ1991Distance.csv', skiprows=1) #open('./distanceData/HZ1991Distance.csv').read().split('\n')
HZ1991Distance = []
count1 = 0
nrows1 = 0
for i in range(len(HZ1991)):
    if float(HZ1991[i])!=0 and float(HZ1991[i])<100 and count1==0:
        HZ1991Distance.append(float(HZ1991[i]))
        nrows1 += 1
    elif float(HZ1991[i])>100 and count1==0:
        HZ1991Distance.append(float(HZ1991[i]))
        count1 += 1
        nrows1 += 1
        break
if len(HZ1991Distance)>maxValue:
    maxValue = len(HZ1991Distance)

HZ1992 = np.loadtxt('./distanceData/HZ1992Distance.csv', skiprows=1)
HZ1992Distance = []
count2 = 0
nrows2 = 0
for i in range(len(HZ1992)):
    if float(HZ1992[i])!=0 and float(HZ1992[i])<100 and count2==0:
        HZ1992Distance.append(float(HZ1992[i]))
        nrows2 += 1
    elif float(HZ1992[i])>100 and count2==0:
        HZ1992Distance.append(float(HZ1992[i]))
        count2 += 1
        nrows2 += 1
        break
if len(HZ1992Distance)>maxValue:
    maxValue = len(HZ1992Distance)
        
HZ1993 = np.loadtxt('./distanceData/HZ1993Distance.csv', skiprows=1)
HZ1993Distance = []
count3 = 0
nrows3 = 0
for i in range(len(HZ1993)):
    if float(HZ1993[i])!=0 and float(HZ1993[i])<100 and count3==0:
        HZ1993Distance.append(float(HZ1993[i]))
        nrows3 += 1
    elif float(HZ1993[i])>100 and count3==0:
        HZ1993Distance.append(float(HZ1993[i]))
        count3 += 1
        nrows3 += 1
        break
if len(HZ1993Distance)>maxValue:
    maxValue = len(HZ1993Distance)
        
HZ1994 = np.loadtxt('./distanceData/HZ1994Distance.csv', skiprows=1)
HZ1994Distance = []
count4 = 0
nrows4 = 0
for i in range(len(HZ1994)):
    if float(HZ1994[i])!=0 and float(HZ1994[i])<100 and count4==0:
        HZ1994Distance.append(float(HZ1994[i]))
        nrows4 += 1
    elif float(HZ1994[i])>100 and count4==0:
        HZ1994Distance.append(float(HZ1994[i]))
        count4 += 1
        nrows4 += 1
        break
if len(HZ1994Distance)>maxValue:
    maxValue = len(HZ1994Distance)
        
HZ1995 = np.loadtxt('./distanceData/HZ1995Distance.csv', skiprows=1)
HZ1995Distance = []
count5 = 0
nrows5 = 0
for i in range(len(HZ1995)):
    if float(HZ1995[i])!=0 and float(HZ1995[i])<100 and count5==0:
        HZ1995Distance.append(float(HZ1995[i]))
        nrows5 += 1
    elif float(HZ1995[i])>100 and count5==0:
        HZ1995Distance.append(float(HZ1995[i]))
        count5 += 1
        nrows5 += 1
        break
if len(HZ1995Distance)>maxValue:
    maxValue = len(HZ1995Distance)
        
HZ1996 = np.loadtxt('./distanceData/HZ1996Distance.csv', skiprows=1)
HZ1996Distance = []
count6 = 0
nrows6 = 0
for i in range(len(HZ1996)):
    if float(HZ1996[i])!=0 and float(HZ1996[i])<100 and count6==0:
        HZ1996Distance.append(float(HZ1996[i]))
        nrows6 += 1
    elif float(HZ1996[i])>100 and count6==0:
        HZ1996Distance.append(float(HZ1996[i]))
        count6 += 1
        nrows6 += 1
        break
if len(HZ1996Distance)>maxValue:
    maxValue = len(HZ1996Distance)
        
HZ1997 = np.loadtxt('./distanceData/HZ1997Distance.csv', skiprows=1)
HZ1997Distance = []
count7 = 0
nrows7 = 0
for i in range(len(HZ1997)):
    if float(HZ1997[i])!=0 and float(HZ1997[i])<100 and count7==0:
        HZ1997Distance.append(float(HZ1997[i]))
        nrows7 += 1
    elif float(HZ1997[i])>100 and count7==0:
        HZ1997Distance.append(float(HZ1997[i]))
        count7 += 1
        nrows7 += 1
        break
if len(HZ1997Distance)>maxValue:
    maxValue = len(HZ1997Distance)
        
HZ1998 = np.loadtxt('./distanceData/HZ1998Distance.csv', skiprows=1)
HZ1998Distance = []
count8 = 0
nrows8 = 0
for i in range(len(HZ1998)):
    if float(HZ1998[i])!=0 and float(HZ1998[i])<100 and count8==0:
        HZ1998Distance.append(float(HZ1998[i]))
        nrows8 += 1
    elif float(HZ1998[i])>100 and count8==0:
        HZ1998Distance.append(float(HZ1998[i]))
        count8 += 1
        nrows8 += 1
        break
if len(HZ1998Distance)>maxValue:
    maxValue = len(HZ1998Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataHZ199.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataHZ199.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataHZ199.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataHZ199.csv', usecols=['Neptune'], nrows=maxValue)

HZ1991e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1991.csv', usecols=['e'], nrows=nrows1)
HZ1992e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1992.csv', usecols=['e'], nrows=nrows2)
HZ1993e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1993.csv', usecols=['e'], nrows=nrows3)
HZ1994e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1994.csv', usecols=['e'], nrows=nrows4)
HZ1995e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1995.csv', usecols=['e'], nrows=nrows5)
HZ1996e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1996.csv', usecols=['e'], nrows=nrows6)
HZ1997e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1997.csv', usecols=['e'], nrows=nrows7)
HZ1998e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1998.csv', usecols=['e'], nrows=nrows8)

HZ1991i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1991.csv', usecols=['i'], nrows=nrows1)
HZ1992i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1992.csv', usecols=['i'], nrows=nrows2)
HZ1993i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1993.csv', usecols=['i'], nrows=nrows3)
HZ1994i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1994.csv', usecols=['i'], nrows=nrows4)
HZ1995i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1995.csv', usecols=['i'], nrows=nrows5)
HZ1996i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1996.csv', usecols=['i'], nrows=nrows6)
HZ1997i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1997.csv', usecols=['i'], nrows=nrows7)
HZ1998i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1998.csv', usecols=['i'], nrows=nrows8)

HZ1991iDeg = []
HZ1992iDeg = []
HZ1993iDeg = []
HZ1994iDeg = []
HZ1995iDeg = []
HZ1996iDeg = []
HZ1997iDeg = []
HZ1998iDeg = []

for j in range(nrows1):
    z = HZ1991i.values[j]
    rad = math.degrees(z)
    HZ1991iDeg.append(float(rad))
for j in range(nrows2):
    z = HZ1992i.values[j]
    rad = math.degrees(z)
    HZ1992iDeg.append(float(rad))
for j in range(nrows3):
    z = HZ1993i.values[j]
    rad = math.degrees(z)
    HZ1993iDeg.append(float(rad))
for j in range(nrows4):
    z = HZ1994i.values[j]
    rad = math.degrees(z)
    HZ1994iDeg.append(float(rad))
for j in range(nrows5):
    z = HZ1995i.values[j]
    rad = math.degrees(z)
    HZ1995iDeg.append(float(rad))
for j in range(nrows6):
    z = HZ1996i.values[j]
    rad = math.degrees(z)
    HZ1996iDeg.append(float(rad))
for j in range(nrows7):
    z = HZ1997i.values[j]
    rad = math.degrees(z)
    HZ1997iDeg.append(float(rad))
for j in range(nrows8):
    z = HZ1998i.values[j]
    rad = math.degrees(z)
    HZ1998iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(HZ1991Distance, color='blue', label='Clone 1')
ax1.plot(HZ1992Distance, color='green', label='Clone 2')
ax1.plot(HZ1993Distance, color='red', label='Clone 3')
ax1.plot(HZ1994Distance, color='brown', label='Clone 4')
ax1.plot(HZ1995Distance, color='purple', label='Clone 5')
ax1.plot(HZ1996Distance, color='orange', label='Clone 6')
ax1.plot(HZ1997Distance, color='grey', label='Clone 7')
ax1.plot(HZ1998Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(HZ1991e, color='blue', label='Clone 1')
ax2.plot(HZ1992e, color='green', label='Clone 2')
ax2.plot(HZ1993e, color='red', label='Clone 3')
ax2.plot(HZ1994e, color='brown', label='Clone 4')
ax2.plot(HZ1995e, color='purple', label='Clone 5')
ax2.plot(HZ1996e, color='orange', label='Clone 6')
ax2.plot(HZ1997e, color='grey', label='Clone 7')
ax2.plot(HZ1998e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.01,1)

ax3.plot(HZ1991iDeg, color='blue', label='Clone 1')
ax3.plot(HZ1992iDeg, color='green', label='Clone 2')
ax3.plot(HZ1993iDeg, color='red', label='Clone 3')
ax3.plot(HZ1994iDeg, color='brown', label='Clone 4')
ax3.plot(HZ1995iDeg, color='purple', label='Clone 5')
ax3.plot(HZ1996iDeg, color='orange', label='Clone 6')
ax3.plot(HZ1997iDeg, color='grey', label='Clone 7')
ax3.plot(HZ1998iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(0.5,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('HZ199')
fig = plt.savefig('./HZ199Figure.png', bbox_inches='tight')

