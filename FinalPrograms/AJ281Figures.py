#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

AJ2811 = np.loadtxt('./distanceData/AJ2811Distance.csv', skiprows=1) #open('./distanceData/AJ2811Distance.csv').read().split('\n')
AJ2811Distance = []
count1 = 0
nrows1 = 0
for i in range(len(AJ2811)):
    if float(AJ2811[i])!=0 and float(AJ2811[i])<100 and count1==0:
        AJ2811Distance.append(float(AJ2811[i]))
        nrows1 += 1
    elif float(AJ2811[i])>100 and count1==0:
        AJ2811Distance.append(float(AJ2811[i]))
        count1 += 1
        nrows1 += 1
        break
if len(AJ2811Distance)>maxValue:
    maxValue = len(AJ2811Distance)

AJ2812 = np.loadtxt('./distanceData/AJ2812Distance.csv', skiprows=1)
AJ2812Distance = []
count2 = 0
nrows2 = 0
for i in range(len(AJ2812)):
    if float(AJ2812[i])!=0 and float(AJ2812[i])<100 and count2==0:
        AJ2812Distance.append(float(AJ2812[i]))
        nrows2 += 1
    elif float(AJ2812[i])>100 and count2==0:
        AJ2812Distance.append(float(AJ2812[i]))
        count2 += 1
        nrows2 += 1
        break
if len(AJ2812Distance)>maxValue:
    maxValue = len(AJ2812Distance)
        
AJ2813 = np.loadtxt('./distanceData/AJ2813Distance.csv', skiprows=1)
AJ2813Distance = []
count3 = 0
nrows3 = 0
for i in range(len(AJ2813)):
    if float(AJ2813[i])!=0 and float(AJ2813[i])<100 and count3==0:
        AJ2813Distance.append(float(AJ2813[i]))
        nrows3 += 1
    elif float(AJ2813[i])>100 and count3==0:
        AJ2813Distance.append(float(AJ2813[i]))
        count3 += 1
        nrows3 += 1
        break
if len(AJ2813Distance)>maxValue:
    maxValue = len(AJ2813Distance)
        
AJ2814 = np.loadtxt('./distanceData/AJ2814Distance.csv', skiprows=1)
AJ2814Distance = []
count4 = 0
nrows4 = 0
for i in range(len(AJ2814)):
    if float(AJ2814[i])!=0 and float(AJ2814[i])<100 and count4==0:
        AJ2814Distance.append(float(AJ2814[i]))
        nrows4 += 1
    elif float(AJ2814[i])>100 and count4==0:
        AJ2814Distance.append(float(AJ2814[i]))
        count4 += 1
        nrows4 += 1
        break
if len(AJ2814Distance)>maxValue:
    maxValue = len(AJ2814Distance)
        
AJ2815 = np.loadtxt('./distanceData/AJ2815Distance.csv', skiprows=1)
AJ2815Distance = []
count5 = 0
nrows5 = 0
for i in range(len(AJ2815)):
    if float(AJ2815[i])!=0 and float(AJ2815[i])<100 and count5==0:
        AJ2815Distance.append(float(AJ2815[i]))
        nrows5 += 1
    elif float(AJ2815[i])>100 and count5==0:
        AJ2815Distance.append(float(AJ2815[i]))
        count5 += 1
        nrows5 += 1
        break
if len(AJ2815Distance)>maxValue:
    maxValue = len(AJ2815Distance)
        
AJ2816 = np.loadtxt('./distanceData/AJ2816Distance.csv', skiprows=1)
AJ2816Distance = []
count6 = 0
nrows6 = 0
for i in range(len(AJ2816)):
    if float(AJ2816[i])!=0 and float(AJ2816[i])<100 and count6==0:
        AJ2816Distance.append(float(AJ2816[i]))
        nrows6 += 1
    elif float(AJ2816[i])>100 and count6==0:
        AJ2816Distance.append(float(AJ2816[i]))
        count6 += 1
        nrows6 += 1
        break
if len(AJ2816Distance)>maxValue:
    maxValue = len(AJ2816Distance)
        
AJ2817 = np.loadtxt('./distanceData/AJ2817Distance.csv', skiprows=1)
AJ2817Distance = []
count7 = 0
nrows7 = 0
for i in range(len(AJ2817)):
    if float(AJ2817[i])!=0 and float(AJ2817[i])<100 and count7==0:
        AJ2817Distance.append(float(AJ2817[i]))
        nrows7 += 1
    elif float(AJ2817[i])>100 and count7==0:
        AJ2817Distance.append(float(AJ2817[i]))
        count7 += 1
        nrows7 += 1
        break
if len(AJ2817Distance)>maxValue:
    maxValue = len(AJ2817Distance)
        
AJ2818 = np.loadtxt('./distanceData/AJ2818Distance.csv', skiprows=1)
AJ2818Distance = []
count8 = 0
nrows8 = 0
for i in range(len(AJ2818)):
    if float(AJ2818[i])!=0 and float(AJ2818[i])<100 and count8==0:
        AJ2818Distance.append(float(AJ2818[i]))
        nrows8 += 1
    elif float(AJ2818[i])>100 and count8==0:
        AJ2818Distance.append(float(AJ2818[i]))
        count8 += 1
        nrows8 += 1
        break
if len(AJ2818Distance)>maxValue:
    maxValue = len(AJ2818Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataAJ281.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataAJ281.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataAJ281.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataAJ281.csv', usecols=['Neptune'], nrows=maxValue)

AJ2811e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2811.csv', usecols=['e'], nrows=nrows1)
AJ2812e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2812.csv', usecols=['e'], nrows=nrows2)
AJ2813e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2813.csv', usecols=['e'], nrows=nrows3)
AJ2814e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2814.csv', usecols=['e'], nrows=nrows4)
AJ2815e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2815.csv', usecols=['e'], nrows=nrows5)
AJ2816e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2816.csv', usecols=['e'], nrows=nrows6)
AJ2817e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2817.csv', usecols=['e'], nrows=nrows7)
AJ2818e = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2818.csv', usecols=['e'], nrows=nrows8)

AJ2811i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2811.csv', usecols=['i'], nrows=nrows1)
AJ2812i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2812.csv', usecols=['i'], nrows=nrows2)
AJ2813i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2813.csv', usecols=['i'], nrows=nrows3)
AJ2814i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2814.csv', usecols=['i'], nrows=nrows4)
AJ2815i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2815.csv', usecols=['i'], nrows=nrows5)
AJ2816i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2816.csv', usecols=['i'], nrows=nrows6)
AJ2817i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2817.csv', usecols=['i'], nrows=nrows7)
AJ2818i = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/AJ2818.csv', usecols=['i'], nrows=nrows8)

 
AJ2811iDeg = []
AJ2812iDeg = []
AJ2813iDeg = []
AJ2814iDeg = []
AJ2815iDeg = []
AJ2816iDeg = []
AJ2817iDeg = []
AJ2818iDeg = []

for j in range(nrows1):
    z = AJ2811i.values[j]
    rad = math.degrees(z)
    AJ2811iDeg.append(float(rad))
for j in range(nrows2):
    z = AJ2812i.values[j]
    rad = math.degrees(z)
    AJ2812iDeg.append(float(rad))
for j in range(nrows3):
    z = AJ2813i.values[j]
    rad = math.degrees(z)
    AJ2813iDeg.append(float(rad))
for j in range(nrows4):
    z = AJ2814i.values[j]
    rad = math.degrees(z)
    AJ2814iDeg.append(float(rad))
for j in range(nrows5):
    z = AJ2815i.values[j]
    rad = math.degrees(z)
    AJ2815iDeg.append(float(rad))
for j in range(nrows6):
    z = AJ2816i.values[j]
    rad = math.degrees(z)
    AJ2816iDeg.append(float(rad))
for j in range(nrows7):
    z = AJ2817i.values[j]
    rad = math.degrees(z)
    AJ2817iDeg.append(float(rad))
for j in range(nrows8):
    z = AJ2818i.values[j]
    rad = math.degrees(z)
    AJ2818iDeg.append(float(rad))
    
print("Complete 1")

print("Complete 2")
        
fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

ax1.plot(jupiterGGData, color='black', label='Jupiter')
ax1.plot(saturnGGData, color='silver', label='Saturn')
ax1.plot(uranusGGData, color='navy', label='Uranus')
ax1.plot(neptuneGGData, color='maroon', label='Neptune')
ax1.plot(AJ2811Distance, color='blue', label='Clone 1')
ax1.plot(AJ2812Distance, color='green', label='Clone 2')
ax1.plot(AJ2813Distance, color='red', label='Clone 3')
ax1.plot(AJ2814Distance, color='brown', label='Clone 4')
ax1.plot(AJ2815Distance, color='purple', label='Clone 5')
ax1.plot(AJ2816Distance, color='orange', label='Clone 6')
ax1.plot(AJ2817Distance, color='grey', label='Clone 7')
ax1.plot(AJ2818Distance, color='yellow', label='Clone 8')
ax1.set_ylabel('Distance (au)')
ax1.set_ylim(0,100)

ax2.plot(AJ2811e, color='blue', label='Clone 1')
ax2.plot(AJ2812e, color='green', label='Clone 2')
ax2.plot(AJ2813e, color='red', label='Clone 3')
ax2.plot(AJ2814e, color='brown', label='Clone 4')
ax2.plot(AJ2815e, color='purple', label='Clone 5')
ax2.plot(AJ2816e, color='orange', label='Clone 6')
ax2.plot(AJ2817e, color='grey', label='Clone 7')
ax2.plot(AJ2818e, color='yellow', label='Clone 8')
ax2.set_ylabel('Eccentricity')
ax2.set_ylim(0.1,0.2)

ax3.plot(AJ2811iDeg, color='blue', label='Clone 1')
ax3.plot(AJ2812iDeg, color='green', label='Clone 2')
ax3.plot(AJ2813iDeg, color='red', label='Clone 3')
ax3.plot(AJ2814iDeg, color='brown', label='Clone 4')
ax3.plot(AJ2815iDeg, color='purple', label='Clone 5')
ax3.plot(AJ2816iDeg, color='orange', label='Clone 6')
ax3.plot(AJ2817iDeg, color='grey', label='Clone 7')
ax3.plot(AJ2818iDeg, color='yellow', label='Clone 8')
ax3.set_ylabel('Inclination (deg)')
ax3.set_ylim(20,40)
ax1.legend(loc='upper left', fontsize='x-small')

fig = plt.xticks(ticks=[0,(maxValue/4),(maxValue/4)*2,(maxValue/4)*3,maxValue], labels=['0',str("{:.3e}".format(((maxValue/4)*25000))),str("{:.3e}".format((((maxValue/4)*2)*25000))),str("{:.3e}".format((((maxValue/4)*3)*25000))),str("{:.3e}".format(maxValue*25000))])
fig = plt.xlabel('Time (yrs)')
ax1.set_title('AJ281')
fig = plt.savefig('./AJ281Figure.png', bbox_inches='tight')
print("Complete 3")

