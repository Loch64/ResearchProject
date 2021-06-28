#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

CB791 = np.loadtxt('./distanceData/CB791Distance.csv', skiprows=1) #open('./distanceData/CB791Distance.csv').read().split('\n')
CB791Distance = []
count1 = 0
nrows1 = 0
for i in range(len(CB791)):
    if float(CB791[i])!=0 and float(CB791[i])<100 and count1==0:
        CB791Distance.append(float(CB791[i]))
        nrows1 += 1
    elif float(CB791[i])>100 and count1==0:
        CB791Distance.append(float(CB791[i]))
        count1 += 1
        nrows1 += 1
        break
if len(CB791Distance)>maxValue:
    maxValue = len(CB791Distance)

CB792 = np.loadtxt('./distanceData/CB792Distance.csv', skiprows=1)
CB792Distance = []
count2 = 0
nrows2 = 0
for i in range(len(CB792)):
    if float(CB792[i])!=0 and float(CB792[i])<100 and count2==0:
        CB792Distance.append(float(CB792[i]))
        nrows2 += 1
    elif float(CB792[i])>100 and count2==0:
        CB792Distance.append(float(CB792[i]))
        count2 += 1
        nrows2 += 1
        break
if len(CB792Distance)>maxValue:
    maxValue = len(CB792Distance)
        
CB793 = np.loadtxt('./distanceData/CB793Distance.csv', skiprows=1)
CB793Distance = []
count3 = 0
nrows3 = 0
for i in range(len(CB793)):
    if float(CB793[i])!=0 and float(CB793[i])<100 and count3==0:
        CB793Distance.append(float(CB793[i]))
        nrows3 += 1
    elif float(CB793[i])>100 and count3==0:
        CB793Distance.append(float(CB793[i]))
        count3 += 1
        nrows3 += 1
        break
if len(CB793Distance)>maxValue:
    maxValue = len(CB793Distance)
        
CB794 = np.loadtxt('./distanceData/CB794Distance.csv', skiprows=1)
CB794Distance = []
count4 = 0
nrows4 = 0
for i in range(len(CB794)):
    if float(CB794[i])!=0 and float(CB794[i])<100 and count4==0:
        CB794Distance.append(float(CB794[i]))
        nrows4 += 1
    elif float(CB794[i])>100 and count4==0:
        CB794Distance.append(float(CB794[i]))
        count4 += 1
        nrows4 += 1
        break
if len(CB794Distance)>maxValue:
    maxValue = len(CB794Distance)
        
CB795 = np.loadtxt('./distanceData/CB795Distance.csv', skiprows=1)
CB795Distance = []
count5 = 0
nrows5 = 0
for i in range(len(CB795)):
    if float(CB795[i])!=0 and float(CB795[i])<100 and count5==0:
        CB795Distance.append(float(CB795[i]))
        nrows5 += 1
    elif float(CB795[i])>100 and count5==0:
        CB795Distance.append(float(CB795[i]))
        count5 += 1
        nrows5 += 1
        break
if len(CB795Distance)>maxValue:
    maxValue = len(CB795Distance)
        
CB796 = np.loadtxt('./distanceData/CB796Distance.csv', skiprows=1)
CB796Distance = []
count6 = 0
nrows6 = 0
for i in range(len(CB796)):
    if float(CB796[i])!=0 and float(CB796[i])<100 and count6==0:
        CB796Distance.append(float(CB796[i]))
        nrows6 += 1
    elif float(CB796[i])>100 and count6==0:
        CB796Distance.append(float(CB796[i]))
        count6 += 1
        nrows6 += 1
        break
if len(CB796Distance)>maxValue:
    maxValue = len(CB796Distance)
        
CB797 = np.loadtxt('./distanceData/CB797Distance.csv', skiprows=1)
CB797Distance = []
count7 = 0
nrows7 = 0
for i in range(len(CB797)):
    if float(CB797[i])!=0 and float(CB797[i])<100 and count7==0:
        CB797Distance.append(float(CB797[i]))
        nrows7 += 1
    elif float(CB797[i])>100 and count7==0:
        CB797Distance.append(float(CB797[i]))
        count7 += 1
        nrows7 += 1
        break
if len(CB797Distance)>maxValue:
    maxValue = len(CB797Distance)
        
CB798 = np.loadtxt('./distanceData/CB798Distance.csv', skiprows=1)
CB798Distance = []
count8 = 0
nrows8 = 0
for i in range(len(CB798)):
    if float(CB798[i])!=0 and float(CB798[i])<100 and count8==0:
        CB798Distance.append(float(CB798[i]))
        nrows8 += 1
    elif float(CB798[i])>100 and count8==0:
        CB798Distance.append(float(CB798[i]))
        count8 += 1
        nrows8 += 1
        break
if len(CB798Distance)>maxValue:
    maxValue = len(CB798Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataCB79.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataCB79.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataCB79.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataCB79.csv', usecols=['Neptune'], nrows=maxValue)

CB791e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB791.csv', usecols=['e'], nrows=nrows1)
CB792e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB792.csv', usecols=['e'], nrows=nrows2)
CB793e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB793.csv', usecols=['e'], nrows=nrows3)
CB794e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB794.csv', usecols=['e'], nrows=nrows4)
CB795e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB795.csv', usecols=['e'], nrows=nrows5)
CB796e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB796.csv', usecols=['e'], nrows=nrows6)
CB797e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB797.csv', usecols=['e'], nrows=nrows7)
CB798e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB798.csv', usecols=['e'], nrows=nrows8)

CB791i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB791.csv', usecols=['i'], nrows=nrows1)
CB792i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB792.csv', usecols=['i'], nrows=nrows2)
CB793i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB793.csv', usecols=['i'], nrows=nrows3)
CB794i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB794.csv', usecols=['i'], nrows=nrows4)
CB795i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB795.csv', usecols=['i'], nrows=nrows5)
CB796i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB796.csv', usecols=['i'], nrows=nrows6)
CB797i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB797.csv', usecols=['i'], nrows=nrows7)
CB798i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/CB798.csv', usecols=['i'], nrows=nrows8)

 
CB791iDeg = []
CB792iDeg = []
CB793iDeg = []
CB794iDeg = []
CB795iDeg = []
CB796iDeg = []
CB797iDeg = []
CB798iDeg = []

for j in range(nrows1):
    z = CB791i.values[j]
    rad = math.degrees(z)
    CB791iDeg.append(float(rad))
for j in range(nrows2):
    z = CB792i.values[j]
    rad = math.degrees(z)
    CB792iDeg.append(float(rad))
for j in range(nrows3):
    z = CB793i.values[j]
    rad = math.degrees(z)
    CB793iDeg.append(float(rad))
for j in range(nrows4):
    z = CB794i.values[j]
    rad = math.degrees(z)
    CB794iDeg.append(float(rad))
for j in range(nrows5):
    z = CB795i.values[j]
    rad = math.degrees(z)
    CB795iDeg.append(float(rad))
for j in range(nrows6):
    z = CB796i.values[j]
    rad = math.degrees(z)
    CB796iDeg.append(float(rad))
for j in range(nrows7):
    z = CB797i.values[j]
    rad = math.degrees(z)
    CB797iDeg.append(float(rad))
for j in range(nrows8):
    z = CB798i.values[j]
    rad = math.degrees(z)
    CB798iDeg.append(float(rad))
    
print("Complete 1")
    

####################


#######################
print("Complete 2")



        
fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(CB791Distance, color='blue', label='Clone 1')
ax1.plot(CB792Distance, color='green', label='Clone 2')
ax1.plot(CB793Distance, color='red', label='Clone 3')
ax1.plot(CB794Distance, color='brown', label='Clone 4')
ax1.plot(CB795Distance, color='purple', label='Clone 5')
ax1.plot(CB796Distance, color='orange', label='Clone 6')
ax1.plot(CB797Distance, color='grey', label='Clone 7')
ax1.plot(CB798Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(CB791e, color='blue', label='Clone 1')
ax2.plot(CB792e, color='green', label='Clone 2')
ax2.plot(CB793e, color='red', label='Clone 3')
ax2.plot(CB794e, color='brown', label='Clone 4')
ax2.plot(CB795e, color='purple', label='Clone 5')
ax2.plot(CB796e, color='orange', label='Clone 6')
ax2.plot(CB797e, color='grey', label='Clone 7')
ax2.plot(CB798e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.6,1)

ax3.plot(CB791iDeg, color='blue', label='Clone 1')
ax3.plot(CB792iDeg, color='green', label='Clone 2')
ax3.plot(CB793iDeg, color='red', label='Clone 3')
ax3.plot(CB794iDeg, color='brown', label='Clone 4')
ax3.plot(CB795iDeg, color='purple', label='Clone 5')
ax3.plot(CB796iDeg, color='orange', label='Clone 6')
ax3.plot(CB797iDeg, color='grey', label='Clone 7')
ax3.plot(CB798iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(10,60)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*500))),str("{:.3e}".format((((maxValue/4)*2)*500))),str("{:.3e}".format((((maxValue/4)*3)*500))),str("{:.3e}".format(maxValue*500))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('CB79')
fig = plt.savefig('./CB79Figure.png', bbox_inches='tight')
print("Complete 3")


# In[ ]:




