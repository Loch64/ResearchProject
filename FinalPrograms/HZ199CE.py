#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

jupiterX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHZ199.csv', usecols=['x'], nrows=maxValue)
jupiterY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHZ199.csv', usecols=['y'], nrows=maxValue)
jupiterZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHZ199.csv', usecols=['z'], nrows=maxValue)
saturnX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHZ199.csv', usecols=['x'], nrows=maxValue)
saturnY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHZ199.csv', usecols=['y'], nrows=maxValue)
saturnZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHZ199.csv', usecols=['z'], nrows=maxValue)
uranusX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHZ199.csv', usecols=['x'], nrows=maxValue)
uranusY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHZ199.csv', usecols=['y'], nrows=maxValue)
uranusZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHZ199.csv', usecols=['z'], nrows=maxValue)
neptuneX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHZ199.csv', usecols=['x'], nrows=maxValue)
neptuneY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHZ199.csv', usecols=['y'], nrows=maxValue)
neptuneZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHZ199.csv', usecols=['z'], nrows=maxValue)

HZ1991x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1991.csv', usecols=['x'], nrows=nrows1)
HZ1992x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1992.csv', usecols=['x'], nrows=nrows2)
HZ1993x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1993.csv', usecols=['x'], nrows=nrows3)
HZ1994x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1994.csv', usecols=['x'], nrows=nrows4)
HZ1995x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1995.csv', usecols=['x'], nrows=nrows5)
HZ1996x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1996.csv', usecols=['x'], nrows=nrows6)
HZ1997x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1997.csv', usecols=['x'], nrows=nrows7)
HZ1998x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1998.csv', usecols=['x'], nrows=nrows8)

HZ1991y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1991.csv', usecols=['y'], nrows=nrows1)
HZ1992y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1992.csv', usecols=['y'], nrows=nrows2)
HZ1993y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1993.csv', usecols=['y'], nrows=nrows3)
HZ1994y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1994.csv', usecols=['y'], nrows=nrows4)
HZ1995y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1995.csv', usecols=['y'], nrows=nrows5)
HZ1996y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1996.csv', usecols=['y'], nrows=nrows6)
HZ1997y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1997.csv', usecols=['y'], nrows=nrows7)
HZ1998y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1998.csv', usecols=['y'], nrows=nrows8)

HZ1991z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1991.csv', usecols=['z'], nrows=nrows1)
HZ1992z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1992.csv', usecols=['z'], nrows=nrows2)
HZ1993z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1993.csv', usecols=['z'], nrows=nrows3)
HZ1994z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1994.csv', usecols=['z'], nrows=nrows4)
HZ1995z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1995.csv', usecols=['z'], nrows=nrows5)
HZ1996z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1996.csv', usecols=['z'], nrows=nrows6)
HZ1997z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1997.csv', usecols=['z'], nrows=nrows7)
HZ1998z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/HZ1998.csv', usecols=['z'], nrows=nrows8)

####################
HZ1991CE = []
HZ1992CE = []
HZ1993CE = []
HZ1994CE = []
HZ1995CE = []
HZ1996CE = []
HZ1997CE = []
HZ1998CE = []

for j in range(len(HZ1991Distance)):
    if math.sqrt(math.pow((HZ1991x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1991y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1991z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1991CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1991x.values[j]-saturnX.values[j]),2)+math.pow((HZ1991y.values[j]-saturnY.values[j]),2)+math.pow((HZ1991z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1991CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1991x.values[j]-uranusX.values[j]),2)+math.pow((HZ1991y.values[j]-uranusY.values[j]),2)+math.pow((HZ1991z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1991CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1991x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1991y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1991z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1991CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(HZ1992Distance)):
    if math.sqrt(math.pow((HZ1992x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1992y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1992z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1992CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1992x.values[j]-saturnX.values[j]),2)+math.pow((HZ1992y.values[j]-saturnY.values[j]),2)+math.pow((HZ1992z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1992CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1992x.values[j]-uranusX.values[j]),2)+math.pow((HZ1992y.values[j]-uranusY.values[j]),2)+math.pow((HZ1992z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1992CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1992x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1992y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1992z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1992CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

for j in range(len(HZ1993Distance)):
    if math.sqrt(math.pow((HZ1993x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1993y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1993z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1993CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1993x.values[j]-saturnX.values[j]),2)+math.pow((HZ1993y.values[j]-saturnY.values[j]),2)+math.pow((HZ1993z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1993CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1993x.values[j]-uranusX.values[j]),2)+math.pow((HZ1993y.values[j]-uranusY.values[j]),2)+math.pow((HZ1993z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1993CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1993x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1993y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1993z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1993CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")   

for j in range(len(HZ1994Distance)):
    if math.sqrt(math.pow((HZ1994x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1994y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1994z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1994CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1994x.values[j]-saturnX.values[j]),2)+math.pow((HZ1994y.values[j]-saturnY.values[j]),2)+math.pow((HZ1994z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1994CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1994x.values[j]-uranusX.values[j]),2)+math.pow((HZ1994y.values[j]-uranusY.values[j]),2)+math.pow((HZ1994z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1994CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1994x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1994y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1994z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1994CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(HZ1995Distance)):
    if math.sqrt(math.pow((HZ1995x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1995y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1995z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1995CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1995x.values[j]-saturnX.values[j]),2)+math.pow((HZ1995y.values[j]-saturnY.values[j]),2)+math.pow((HZ1995z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1995CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1995x.values[j]-uranusX.values[j]),2)+math.pow((HZ1995y.values[j]-uranusY.values[j]),2)+math.pow((HZ1995z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1995CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1995x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1995y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1995z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1995CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(HZ1996Distance)):
    if math.sqrt(math.pow((HZ1996x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1996y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1996z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1996CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1996x.values[j]-saturnX.values[j]),2)+math.pow((HZ1996y.values[j]-saturnY.values[j]),2)+math.pow((HZ1996z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1996CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1996x.values[j]-uranusX.values[j]),2)+math.pow((HZ1996y.values[j]-uranusY.values[j]),2)+math.pow((HZ1996z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1996CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1996x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1996y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1996z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1996CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(HZ1997Distance)):
    if math.sqrt(math.pow((HZ1997x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1997y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1997z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1997CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1997x.values[j]-saturnX.values[j]),2)+math.pow((HZ1997y.values[j]-saturnY.values[j]),2)+math.pow((HZ1997z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1997CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1997x.values[j]-uranusX.values[j]),2)+math.pow((HZ1997y.values[j]-uranusY.values[j]),2)+math.pow((HZ1997z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1997CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1997x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1997y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1997z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1997CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(HZ1998Distance)):
    if math.sqrt(math.pow((HZ1998x.values[j]-jupiterX.values[j]),2)+math.pow((HZ1998y.values[j]-jupiterY.values[j]),2)+math.pow((HZ1998z.values[j]-jupiterZ.values[j]),2))<=1.065:
        HZ1998CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1998x.values[j]-saturnX.values[j]),2)+math.pow((HZ1998y.values[j]-saturnY.values[j]),2)+math.pow((HZ1998z.values[j]-saturnZ.values[j]),2))<=1.314:
        HZ1998CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1998x.values[j]-uranusX.values[j]),2)+math.pow((HZ1998y.values[j]-uranusY.values[j]),2)+math.pow((HZ1998z.values[j]-uranusZ.values[j]),2))<=1.407:
        HZ1998CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((HZ1998x.values[j]-neptuneX.values[j]),2)+math.pow((HZ1998y.values[j]-neptuneY.values[j]),2)+math.pow((HZ1998z.values[j]-neptuneZ.values[j]),2))<=2.325:
        HZ1998CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

#######################


if len(HZ1991CE)>0:
    np.savetxt("HZ1991CE.csv", HZ1991CE, fmt='%s') 
    df = pd.read_csv('HZ1991CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1991'}, inplace=True)
    df.to_csv('HZ1991CE.csv', index=False) 
if len(HZ1992CE)>0:               
    np.savetxt("HZ1992CE.csv", HZ1992CE, fmt='%s') 
    df = pd.read_csv('HZ1992CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1992'}, inplace=True)
    df.to_csv('HZ1992CE.csv', index=False) 
if len(HZ1993CE)>0:                   
    np.savetxt("HZ1993CE.csv", HZ1993CE, fmt='%s') 
    df = pd.read_csv('HZ1993CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1993'}, inplace=True)
    df.to_csv('HZ1993CE.csv', index=False) 
if len(HZ1994CE)>0:
    np.savetxt("HZ1994CE.csv", HZ1994CE, fmt='%s') 
    df = pd.read_csv('HZ1994CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1994'}, inplace=True)
    df.to_csv('HZ1994CE.csv', index=False) 
if len(HZ1995CE)>0:
    np.savetxt("HZ1995CE.csv", HZ1995CE, fmt='%s') 
    df = pd.read_csv('HZ1995CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1995'}, inplace=True)
    df.to_csv('HZ1995CE.csv', index=False) 
if len(HZ1996CE)>0:                  
    np.savetxt("HZ1996CE.csv", HZ1996CE, fmt='%s') 
    df = pd.read_csv('HZ1996CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1996'}, inplace=True)
    df.to_csv('HZ1996CE.csv', index=False) 
if len(HZ1997CE)>0:
    np.savetxt("HZ1997CE.csv", HZ1997CE, fmt='%s') 
    df = pd.read_csv('HZ1997CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1997'}, inplace=True)
    df.to_csv('HZ1997CE.csv', index=False) 
if len(HZ1998CE)>0:                  
    np.savetxt("HZ1998CE.csv", HZ1998CE, fmt='%s') 
    df = pd.read_csv('HZ1998CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone HZ1998'}, inplace=True)
    df.to_csv('HZ1998CE.csv', index=False) 
        

print("Complete 3")
