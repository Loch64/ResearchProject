#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

AP1291 = np.loadtxt('./distanceData/AP1291Distance.csv', skiprows=1) #open('./distanceData/AP1291Distance.csv').read().split('\n')
AP1291Distance = []
count1 = 0
nrows1 = 0
for i in range(len(AP1291)):
    if float(AP1291[i])!=0 and float(AP1291[i])<100 and count1==0:
        AP1291Distance.append(float(AP1291[i]))
        nrows1 += 1
    elif float(AP1291[i])>100 and count1==0:
        AP1291Distance.append(float(AP1291[i]))
        count1 += 1
        nrows1 += 1
        break
if len(AP1291Distance)>maxValue:
    maxValue = len(AP1291Distance)

AP1292 = np.loadtxt('./distanceData/AP1292Distance.csv', skiprows=1)
AP1292Distance = []
count2 = 0
nrows2 = 0
for i in range(len(AP1292)):
    if float(AP1292[i])!=0 and float(AP1292[i])<100 and count2==0:
        AP1292Distance.append(float(AP1292[i]))
        nrows2 += 1
    elif float(AP1292[i])>100 and count2==0:
        AP1292Distance.append(float(AP1292[i]))
        count2 += 1
        nrows2 += 1
        break
if len(AP1292Distance)>maxValue:
    maxValue = len(AP1292Distance)
        
AP1293 = np.loadtxt('./distanceData/AP1293Distance.csv', skiprows=1)
AP1293Distance = []
count3 = 0
nrows3 = 0
for i in range(len(AP1293)):
    if float(AP1293[i])!=0 and float(AP1293[i])<100 and count3==0:
        AP1293Distance.append(float(AP1293[i]))
        nrows3 += 1
    elif float(AP1293[i])>100 and count3==0:
        AP1293Distance.append(float(AP1293[i]))
        count3 += 1
        nrows3 += 1
        break
if len(AP1293Distance)>maxValue:
    maxValue = len(AP1293Distance)
        
AP1294 = np.loadtxt('./distanceData/AP1294Distance.csv', skiprows=1)
AP1294Distance = []
count4 = 0
nrows4 = 0
for i in range(len(AP1294)):
    if float(AP1294[i])!=0 and float(AP1294[i])<100 and count4==0:
        AP1294Distance.append(float(AP1294[i]))
        nrows4 += 1
    elif float(AP1294[i])>100 and count4==0:
        AP1294Distance.append(float(AP1294[i]))
        count4 += 1
        nrows4 += 1
        break
if len(AP1294Distance)>maxValue:
    maxValue = len(AP1294Distance)
        
AP1295 = np.loadtxt('./distanceData/AP1295Distance.csv', skiprows=1)
AP1295Distance = []
count5 = 0
nrows5 = 0
for i in range(len(AP1295)):
    if float(AP1295[i])!=0 and float(AP1295[i])<100 and count5==0:
        AP1295Distance.append(float(AP1295[i]))
        nrows5 += 1
    elif float(AP1295[i])>100 and count5==0:
        AP1295Distance.append(float(AP1295[i]))
        count5 += 1
        nrows5 += 1
        break
if len(AP1295Distance)>maxValue:
    maxValue = len(AP1295Distance)
        
AP1296 = np.loadtxt('./distanceData/AP1296Distance.csv', skiprows=1)
AP1296Distance = []
count6 = 0
nrows6 = 0
for i in range(len(AP1296)):
    if float(AP1296[i])!=0 and float(AP1296[i])<100 and count6==0:
        AP1296Distance.append(float(AP1296[i]))
        nrows6 += 1
    elif float(AP1296[i])>100 and count6==0:
        AP1296Distance.append(float(AP1296[i]))
        count6 += 1
        nrows6 += 1
        break
if len(AP1296Distance)>maxValue:
    maxValue = len(AP1296Distance)
        
AP1297 = np.loadtxt('./distanceData/AP1297Distance.csv', skiprows=1)
AP1297Distance = []
count7 = 0
nrows7 = 0
for i in range(len(AP1297)):
    if float(AP1297[i])!=0 and float(AP1297[i])<100 and count7==0:
        AP1297Distance.append(float(AP1297[i]))
        nrows7 += 1
    elif float(AP1297[i])>100 and count7==0:
        AP1297Distance.append(float(AP1297[i]))
        count7 += 1
        nrows7 += 1
        break
if len(AP1297Distance)>maxValue:
    maxValue = len(AP1297Distance)
        
AP1298 = np.loadtxt('./distanceData/AP1298Distance.csv', skiprows=1)
AP1298Distance = []
count8 = 0
nrows8 = 0
for i in range(len(AP1298)):
    if float(AP1298[i])!=0 and float(AP1298[i])<100 and count8==0:
        AP1298Distance.append(float(AP1298[i]))
        nrows8 += 1
    elif float(AP1298[i])>100 and count8==0:
        AP1298Distance.append(float(AP1298[i]))
        count8 += 1
        nrows8 += 1
        break
if len(AP1298Distance)>maxValue:
    maxValue = len(AP1298Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataAP129.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataAP129.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataAP129.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataAP129.csv', usecols=['Neptune'], nrows=maxValue)

AP1291e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1291.csv', usecols=['e'], nrows=nrows1)
AP1292e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1292.csv', usecols=['e'], nrows=nrows2)
AP1293e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1293.csv', usecols=['e'], nrows=nrows3)
AP1294e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1294.csv', usecols=['e'], nrows=nrows4)
AP1295e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1295.csv', usecols=['e'], nrows=nrows5)
AP1296e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1296.csv', usecols=['e'], nrows=nrows6)
AP1297e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1297.csv', usecols=['e'], nrows=nrows7)
AP1298e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1298.csv', usecols=['e'], nrows=nrows8)

AP1291i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1291.csv', usecols=['i'], nrows=nrows1)
AP1292i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1292.csv', usecols=['i'], nrows=nrows2)
AP1293i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1293.csv', usecols=['i'], nrows=nrows3)
AP1294i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1294.csv', usecols=['i'], nrows=nrows4)
AP1295i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1295.csv', usecols=['i'], nrows=nrows5)
AP1296i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1296.csv', usecols=['i'], nrows=nrows6)
AP1297i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1297.csv', usecols=['i'], nrows=nrows7)
AP1298i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AP1298.csv', usecols=['i'], nrows=nrows8)

AP1291iDeg = []
AP1292iDeg = []
AP1293iDeg = []
AP1294iDeg = []
AP1295iDeg = []
AP1296iDeg = []
AP1297iDeg = []
AP1298iDeg = []

for j in range(nrows1):
    z = AP1291i.values[j]
    rad = math.degrees(z)
    AP1291iDeg.append(float(rad))
for j in range(nrows2):
    z = AP1292i.values[j]
    rad = math.degrees(z)
    AP1292iDeg.append(float(rad))
for j in range(nrows3):
    z = AP1293i.values[j]
    rad = math.degrees(z)
    AP1293iDeg.append(float(rad))
for j in range(nrows4):
    z = AP1294i.values[j]
    rad = math.degrees(z)
    AP1294iDeg.append(float(rad))
for j in range(nrows5):
    z = AP1295i.values[j]
    rad = math.degrees(z)
    AP1295iDeg.append(float(rad))
for j in range(nrows6):
    z = AP1296i.values[j]
    rad = math.degrees(z)
    AP1296iDeg.append(float(rad))
for j in range(nrows7):
    z = AP1297i.values[j]
    rad = math.degrees(z)
    AP1297iDeg.append(float(rad))
for j in range(nrows8):
    z = AP1298i.values[j]
    rad = math.degrees(z)
    AP1298iDeg.append(float(rad))

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(AP1291Distance, color='blue', label='Clone 1')
ax1.plot(AP1292Distance, color='green', label='Clone 2')
ax1.plot(AP1293Distance, color='red', label='Clone 3')
ax1.plot(AP1294Distance, color='brown', label='Clone 4')
ax1.plot(AP1295Distance, color='purple', label='Clone 5')
ax1.plot(AP1296Distance, color='orange', label='Clone 6')
ax1.plot(AP1297Distance, color='grey', label='Clone 7')
ax1.plot(AP1298Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(AP1291e, color='blue', label='Clone 1')
ax2.plot(AP1292e, color='green', label='Clone 2')
ax2.plot(AP1293e, color='red', label='Clone 3')
ax2.plot(AP1294e, color='brown', label='Clone 4')
ax2.plot(AP1295e, color='purple', label='Clone 5')
ax2.plot(AP1296e, color='orange', label='Clone 6')
ax2.plot(AP1297e, color='grey', label='Clone 7')
ax2.plot(AP1298e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.1,0.2)

ax3.plot(AP1291iDeg, color='blue', label='Clone 1')
ax3.plot(AP1292iDeg, color='green', label='Clone 2')
ax3.plot(AP1293iDeg, color='red', label='Clone 3')
ax3.plot(AP1294iDeg, color='brown', label='Clone 4')
ax3.plot(AP1295iDeg, color='purple', label='Clone 5')
ax3.plot(AP1296iDeg, color='orange', label='Clone 6')
ax3.plot(AP1297iDeg, color='grey', label='Clone 7')
ax3.plot(AP1298iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('AP129')
fig = plt.savefig('./AP129Figure.png', bbox_inches='tight')

