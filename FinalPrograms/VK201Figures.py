#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

VK2011 = np.loadtxt('./distanceData/VK2011Distance.csv', skiprows=1) #open('./distanceData/VK2011Distance.csv').read().split('\n')
VK2011Distance = []
count1 = 0
nrows1 = 0
for i in range(len(VK2011)):
    if float(VK2011[i])!=0 and float(VK2011[i])<100 and count1==0:
        VK2011Distance.append(float(VK2011[i]))
        nrows1 += 1
    elif float(VK2011[i])>100 and count1==0:
        VK2011Distance.append(float(VK2011[i]))
        count1 += 1
        nrows1 += 1
        break
if len(VK2011Distance)>maxValue:
    maxValue = len(VK2011Distance)

VK2012 = np.loadtxt('./distanceData/VK2012Distance.csv', skiprows=1)
VK2012Distance = []
count2 = 0
nrows2 = 0
for i in range(len(VK2012)):
    if float(VK2012[i])!=0 and float(VK2012[i])<100 and count2==0:
        VK2012Distance.append(float(VK2012[i]))
        nrows2 += 1
    elif float(VK2012[i])>100 and count2==0:
        VK2012Distance.append(float(VK2012[i]))
        count2 += 1
        nrows2 += 1
        break
if len(VK2012Distance)>maxValue:
    maxValue = len(VK2012Distance)
        
VK2013 = np.loadtxt('./distanceData/VK2013Distance.csv', skiprows=1)
VK2013Distance = []
count3 = 0
nrows3 = 0
for i in range(len(VK2013)):
    if float(VK2013[i])!=0 and float(VK2013[i])<100 and count3==0:
        VK2013Distance.append(float(VK2013[i]))
        nrows3 += 1
    elif float(VK2013[i])>100 and count3==0:
        VK2013Distance.append(float(VK2013[i]))
        count3 += 1
        nrows3 += 1
        break
if len(VK2013Distance)>maxValue:
    maxValue = len(VK2013Distance)
        
VK2014 = np.loadtxt('./distanceData/VK2014Distance.csv', skiprows=1)
VK2014Distance = []
count4 = 0
nrows4 = 0
for i in range(len(VK2014)):
    if float(VK2014[i])!=0 and float(VK2014[i])<100 and count4==0:
        VK2014Distance.append(float(VK2014[i]))
        nrows4 += 1
    elif float(VK2014[i])>100 and count4==0:
        VK2014Distance.append(float(VK2014[i]))
        count4 += 1
        nrows4 += 1
        break
if len(VK2014Distance)>maxValue:
    maxValue = len(VK2014Distance)
        
VK2015 = np.loadtxt('./distanceData/VK2015Distance.csv', skiprows=1)
VK2015Distance = []
count5 = 0
nrows5 = 0
for i in range(len(VK2015)):
    if float(VK2015[i])!=0 and float(VK2015[i])<100 and count5==0:
        VK2015Distance.append(float(VK2015[i]))
        nrows5 += 1
    elif float(VK2015[i])>100 and count5==0:
        VK2015Distance.append(float(VK2015[i]))
        count5 += 1
        nrows5 += 1
        break
if len(VK2015Distance)>maxValue:
    maxValue = len(VK2015Distance)
        
VK2016 = np.loadtxt('./distanceData/VK2016Distance.csv', skiprows=1)
VK2016Distance = []
count6 = 0
nrows6 = 0
for i in range(len(VK2016)):
    if float(VK2016[i])!=0 and float(VK2016[i])<100 and count6==0:
        VK2016Distance.append(float(VK2016[i]))
        nrows6 += 1
    elif float(VK2016[i])>100 and count6==0:
        VK2016Distance.append(float(VK2016[i]))
        count6 += 1
        nrows6 += 1
        break
if len(VK2016Distance)>maxValue:
    maxValue = len(VK2016Distance)
        
VK2017 = np.loadtxt('./distanceData/VK2017Distance.csv', skiprows=1)
VK2017Distance = []
count7 = 0
nrows7 = 0
for i in range(len(VK2017)):
    if float(VK2017[i])!=0 and float(VK2017[i])<100 and count7==0:
        VK2017Distance.append(float(VK2017[i]))
        nrows7 += 1
    elif float(VK2017[i])>100 and count7==0:
        VK2017Distance.append(float(VK2017[i]))
        count7 += 1
        nrows7 += 1
        break
if len(VK2017Distance)>maxValue:
    maxValue = len(VK2017Distance)
        
VK2018 = np.loadtxt('./distanceData/VK2018Distance.csv', skiprows=1)
VK2018Distance = []
count8 = 0
nrows8 = 0
for i in range(len(VK2018)):
    if float(VK2018[i])!=0 and float(VK2018[i])<100 and count8==0:
        VK2018Distance.append(float(VK2018[i]))
        nrows8 += 1
    elif float(VK2018[i])>100 and count8==0:
        VK2018Distance.append(float(VK2018[i]))
        count8 += 1
        nrows8 += 1
        break
if len(VK2018Distance)>maxValue:
    maxValue = len(VK2018Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataVK201.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataVK201.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataVK201.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataVK201.csv', usecols=['Neptune'], nrows=maxValue)

VK2011e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2011.csv', usecols=['e'], nrows=nrows1)
VK2012e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2012.csv', usecols=['e'], nrows=nrows2)
VK2013e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2013.csv', usecols=['e'], nrows=nrows3)
VK2014e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2014.csv', usecols=['e'], nrows=nrows4)
VK2015e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2015.csv', usecols=['e'], nrows=nrows5)
VK2016e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2016.csv', usecols=['e'], nrows=nrows6)
VK2017e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2017.csv', usecols=['e'], nrows=nrows7)
VK2018e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2018.csv', usecols=['e'], nrows=nrows8)

VK2011i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2011.csv', usecols=['i'], nrows=nrows1)
VK2012i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2012.csv', usecols=['i'], nrows=nrows2)
VK2013i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2013.csv', usecols=['i'], nrows=nrows3)
VK2014i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2014.csv', usecols=['i'], nrows=nrows4)
VK2015i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2015.csv', usecols=['i'], nrows=nrows5)
VK2016i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2016.csv', usecols=['i'], nrows=nrows6)
VK2017i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2017.csv', usecols=['i'], nrows=nrows7)
VK2018i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/VK2018.csv', usecols=['i'], nrows=nrows8)

VK2011iDeg = []
VK2012iDeg = []
VK2013iDeg = []
VK2014iDeg = []
VK2015iDeg = []
VK2016iDeg = []
VK2017iDeg = []
VK2018iDeg = []

for j in range(nrows1):
    z = VK2011i.values[j]
    rad = math.degrees(z)
    VK2011iDeg.append(float(rad))
for j in range(nrows2):
    z = VK2012i.values[j]
    rad = math.degrees(z)
    VK2012iDeg.append(float(rad))
for j in range(nrows3):
    z = VK2013i.values[j]
    rad = math.degrees(z)
    VK2013iDeg.append(float(rad))
for j in range(nrows4):
    z = VK2014i.values[j]
    rad = math.degrees(z)
    VK2014iDeg.append(float(rad))
for j in range(nrows5):
    z = VK2015i.values[j]
    rad = math.degrees(z)
    VK2015iDeg.append(float(rad))
for j in range(nrows6):
    z = VK2016i.values[j]
    rad = math.degrees(z)
    VK2016iDeg.append(float(rad))
for j in range(nrows7):
    z = VK2017i.values[j]
    rad = math.degrees(z)
    VK2017iDeg.append(float(rad))
for j in range(nrows8):
    z = VK2018i.values[j]
    rad = math.degrees(z)
    VK2018iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(VK2011Distance, color='blue', label='Clone 1')
ax1.plot(VK2012Distance, color='green', label='Clone 2')
ax1.plot(VK2013Distance, color='red', label='Clone 3')
ax1.plot(VK2014Distance, color='brown', label='Clone 4')
ax1.plot(VK2015Distance, color='purple', label='Clone 5')
ax1.plot(VK2016Distance, color='orange', label='Clone 6')
ax1.plot(VK2017Distance, color='grey', label='Clone 7')
ax1.plot(VK2018Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(VK2011e, color='blue', label='Clone 1')
ax2.plot(VK2012e, color='green', label='Clone 2')
ax2.plot(VK2013e, color='red', label='Clone 3')
ax2.plot(VK2014e, color='brown', label='Clone 4')
ax2.plot(VK2015e, color='purple', label='Clone 5')
ax2.plot(VK2016e, color='orange', label='Clone 6')
ax2.plot(VK2017e, color='grey', label='Clone 7')
ax2.plot(VK2018e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.08,0.12)

ax3.plot(VK2011iDeg, color='blue', label='Clone 1')
ax3.plot(VK2012iDeg, color='green', label='Clone 2')
ax3.plot(VK2013iDeg, color='red', label='Clone 3')
ax3.plot(VK2014iDeg, color='brown', label='Clone 4')
ax3.plot(VK2015iDeg, color='purple', label='Clone 5')
ax3.plot(VK2016iDeg, color='orange', label='Clone 6')
ax3.plot(VK2017iDeg, color='grey', label='Clone 7')
ax3.plot(VK2018iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('VK201')
fig = plt.savefig('./VK201Figure.png', bbox_inches='tight')

