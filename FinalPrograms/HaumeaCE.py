#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

Haumea1 = np.loadtxt('./distanceData/Haumea1Distance.csv', skiprows=1) #open('./distanceData/Haumea1Distance.csv').read().split('\n')
Haumea1Distance = []
count1 = 0
nrows1 = 0
for i in range(len(Haumea1)):
    if float(Haumea1[i])!=0 and float(Haumea1[i])<100 and count1==0:
        Haumea1Distance.append(float(Haumea1[i]))
        nrows1 += 1
    elif float(Haumea1[i])>100 and count1==0:
        Haumea1Distance.append(float(Haumea1[i]))
        count1 += 1
        nrows1 += 1
        break
if len(Haumea1Distance)>maxValue:
    maxValue = len(Haumea1Distance)

Haumea2 = np.loadtxt('./distanceData/Haumea2Distance.csv', skiprows=1)
Haumea2Distance = []
count2 = 0
nrows2 = 0
for i in range(len(Haumea2)):
    if float(Haumea2[i])!=0 and float(Haumea2[i])<100 and count2==0:
        Haumea2Distance.append(float(Haumea2[i]))
        nrows2 += 1
    elif float(Haumea2[i])>100 and count2==0:
        Haumea2Distance.append(float(Haumea2[i]))
        count2 += 1
        nrows2 += 1
        break
if len(Haumea2Distance)>maxValue:
    maxValue = len(Haumea2Distance)
        
Haumea3 = np.loadtxt('./distanceData/Haumea3Distance.csv', skiprows=1)
Haumea3Distance = []
count3 = 0
nrows3 = 0
for i in range(len(Haumea3)):
    if float(Haumea3[i])!=0 and float(Haumea3[i])<100 and count3==0:
        Haumea3Distance.append(float(Haumea3[i]))
        nrows3 += 1
    elif float(Haumea3[i])>100 and count3==0:
        Haumea3Distance.append(float(Haumea3[i]))
        count3 += 1
        nrows3 += 1
        break
if len(Haumea3Distance)>maxValue:
    maxValue = len(Haumea3Distance)
        
Haumea4 = np.loadtxt('./distanceData/Haumea4Distance.csv', skiprows=1)
Haumea4Distance = []
count4 = 0
nrows4 = 0
for i in range(len(Haumea4)):
    if float(Haumea4[i])!=0 and float(Haumea4[i])<100 and count4==0:
        Haumea4Distance.append(float(Haumea4[i]))
        nrows4 += 1
    elif float(Haumea4[i])>100 and count4==0:
        Haumea4Distance.append(float(Haumea4[i]))
        count4 += 1
        nrows4 += 1
        break
if len(Haumea4Distance)>maxValue:
    maxValue = len(Haumea4Distance)
        
Haumea5 = np.loadtxt('./distanceData/Haumea5Distance.csv', skiprows=1)
Haumea5Distance = []
count5 = 0
nrows5 = 0
for i in range(len(Haumea5)):
    if float(Haumea5[i])!=0 and float(Haumea5[i])<100 and count5==0:
        Haumea5Distance.append(float(Haumea5[i]))
        nrows5 += 1
    elif float(Haumea5[i])>100 and count5==0:
        Haumea5Distance.append(float(Haumea5[i]))
        count5 += 1
        nrows5 += 1
        break
if len(Haumea5Distance)>maxValue:
    maxValue = len(Haumea5Distance)
        
Haumea6 = np.loadtxt('./distanceData/Haumea6Distance.csv', skiprows=1)
Haumea6Distance = []
count6 = 0
nrows6 = 0
for i in range(len(Haumea6)):
    if float(Haumea6[i])!=0 and float(Haumea6[i])<100 and count6==0:
        Haumea6Distance.append(float(Haumea6[i]))
        nrows6 += 1
    elif float(Haumea6[i])>100 and count6==0:
        Haumea6Distance.append(float(Haumea6[i]))
        count6 += 1
        nrows6 += 1
        break
if len(Haumea6Distance)>maxValue:
    maxValue = len(Haumea6Distance)
        
Haumea7 = np.loadtxt('./distanceData/Haumea7Distance.csv', skiprows=1)
Haumea7Distance = []
count7 = 0
nrows7 = 0
for i in range(len(Haumea7)):
    if float(Haumea7[i])!=0 and float(Haumea7[i])<100 and count7==0:
        Haumea7Distance.append(float(Haumea7[i]))
        nrows7 += 1
    elif float(Haumea7[i])>100 and count7==0:
        Haumea7Distance.append(float(Haumea7[i]))
        count7 += 1
        nrows7 += 1
        break
if len(Haumea7Distance)>maxValue:
    maxValue = len(Haumea7Distance)
        
Haumea8 = np.loadtxt('./distanceData/Haumea8Distance.csv', skiprows=1)
Haumea8Distance = []
count8 = 0
nrows8 = 0
for i in range(len(Haumea8)):
    if float(Haumea8[i])!=0 and float(Haumea8[i])<100 and count8==0:
        Haumea8Distance.append(float(Haumea8[i]))
        nrows8 += 1
    elif float(Haumea8[i])>100 and count8==0:
        Haumea8Distance.append(float(Haumea8[i]))
        count8 += 1
        nrows8 += 1
        break
if len(Haumea8Distance)>maxValue:
    maxValue = len(Haumea8Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataHaumea.csv', usecols=['Neptune'], nrows=maxValue)

jupiterX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHaumea.csv', usecols=['x'], nrows=maxValue)
jupiterY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHaumea.csv', usecols=['y'], nrows=maxValue)
jupiterZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZHaumea.csv', usecols=['z'], nrows=maxValue)
saturnX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHaumea.csv', usecols=['x'], nrows=maxValue)
saturnY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHaumea.csv', usecols=['y'], nrows=maxValue)
saturnZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZHaumea.csv', usecols=['z'], nrows=maxValue)
uranusX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHaumea.csv', usecols=['x'], nrows=maxValue)
uranusY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHaumea.csv', usecols=['y'], nrows=maxValue)
uranusZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZHaumea.csv', usecols=['z'], nrows=maxValue)
neptuneX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHaumea.csv', usecols=['x'], nrows=maxValue)
neptuneY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHaumea.csv', usecols=['y'], nrows=maxValue)
neptuneZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZHaumea.csv', usecols=['z'], nrows=maxValue)

Haumea1x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea1.csv', usecols=['x'], nrows=nrows1)
Haumea2x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea2.csv', usecols=['x'], nrows=nrows2)
Haumea3x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea3.csv', usecols=['x'], nrows=nrows3)
Haumea4x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea4.csv', usecols=['x'], nrows=nrows4)
Haumea5x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea5.csv', usecols=['x'], nrows=nrows5)
Haumea6x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea6.csv', usecols=['x'], nrows=nrows6)
Haumea7x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea7.csv', usecols=['x'], nrows=nrows7)
Haumea8x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea8.csv', usecols=['x'], nrows=nrows8)

Haumea1y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea1.csv', usecols=['y'], nrows=nrows1)
Haumea2y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea2.csv', usecols=['y'], nrows=nrows2)
Haumea3y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea3.csv', usecols=['y'], nrows=nrows3)
Haumea4y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea4.csv', usecols=['y'], nrows=nrows4)
Haumea5y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea5.csv', usecols=['y'], nrows=nrows5)
Haumea6y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea6.csv', usecols=['y'], nrows=nrows6)
Haumea7y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea7.csv', usecols=['y'], nrows=nrows7)
Haumea8y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea8.csv', usecols=['y'], nrows=nrows8)

Haumea1z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea1.csv', usecols=['z'], nrows=nrows1)
Haumea2z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea2.csv', usecols=['z'], nrows=nrows2)
Haumea3z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea3.csv', usecols=['z'], nrows=nrows3)
Haumea4z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea4.csv', usecols=['z'], nrows=nrows4)
Haumea5z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea5.csv', usecols=['z'], nrows=nrows5)
Haumea6z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea6.csv', usecols=['z'], nrows=nrows6)
Haumea7z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea7.csv', usecols=['z'], nrows=nrows7)
Haumea8z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/Haumea8.csv', usecols=['z'], nrows=nrows8)

####################
Haumea1CE = []
Haumea2CE = []
Haumea3CE = []
Haumea4CE = []
Haumea5CE = []
Haumea6CE = []
Haumea7CE = []
Haumea8CE = []

for j in range(len(Haumea1Distance)):
    if math.sqrt(math.pow((Haumea1x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea1y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea1z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea1CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea1x.values[j]-saturnX.values[j]),2)+math.pow((Haumea1y.values[j]-saturnY.values[j]),2)+math.pow((Haumea1z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea1CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea1x.values[j]-uranusX.values[j]),2)+math.pow((Haumea1y.values[j]-uranusY.values[j]),2)+math.pow((Haumea1z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea1CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea1x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea1y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea1z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea1CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(Haumea2Distance)):
    if math.sqrt(math.pow((Haumea2x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea2y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea2z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea2CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea2x.values[j]-saturnX.values[j]),2)+math.pow((Haumea2y.values[j]-saturnY.values[j]),2)+math.pow((Haumea2z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea2CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea2x.values[j]-uranusX.values[j]),2)+math.pow((Haumea2y.values[j]-uranusY.values[j]),2)+math.pow((Haumea2z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea2CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea2x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea2y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea2z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea2CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

for j in range(len(Haumea3Distance)):
    if math.sqrt(math.pow((Haumea3x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea3y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea3z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea3CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea3x.values[j]-saturnX.values[j]),2)+math.pow((Haumea3y.values[j]-saturnY.values[j]),2)+math.pow((Haumea3z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea3CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea3x.values[j]-uranusX.values[j]),2)+math.pow((Haumea3y.values[j]-uranusY.values[j]),2)+math.pow((Haumea3z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea3CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea3x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea3y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea3z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea3CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")   

for j in range(len(Haumea4Distance)):
    if math.sqrt(math.pow((Haumea4x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea4y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea4z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea4CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea4x.values[j]-saturnX.values[j]),2)+math.pow((Haumea4y.values[j]-saturnY.values[j]),2)+math.pow((Haumea4z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea4CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea4x.values[j]-uranusX.values[j]),2)+math.pow((Haumea4y.values[j]-uranusY.values[j]),2)+math.pow((Haumea4z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea4CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea4x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea4y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea4z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea4CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(Haumea5Distance)):
    if math.sqrt(math.pow((Haumea5x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea5y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea5z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea5CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea5x.values[j]-saturnX.values[j]),2)+math.pow((Haumea5y.values[j]-saturnY.values[j]),2)+math.pow((Haumea5z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea5CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea5x.values[j]-uranusX.values[j]),2)+math.pow((Haumea5y.values[j]-uranusY.values[j]),2)+math.pow((Haumea5z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea5CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea5x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea5y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea5z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea5CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(Haumea6Distance)):
    if math.sqrt(math.pow((Haumea6x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea6y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea6z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea6CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea6x.values[j]-saturnX.values[j]),2)+math.pow((Haumea6y.values[j]-saturnY.values[j]),2)+math.pow((Haumea6z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea6CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea6x.values[j]-uranusX.values[j]),2)+math.pow((Haumea6y.values[j]-uranusY.values[j]),2)+math.pow((Haumea6z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea6CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea6x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea6y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea6z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea6CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(Haumea7Distance)):
    if math.sqrt(math.pow((Haumea7x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea7y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea7z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea7CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea7x.values[j]-saturnX.values[j]),2)+math.pow((Haumea7y.values[j]-saturnY.values[j]),2)+math.pow((Haumea7z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea7CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea7x.values[j]-uranusX.values[j]),2)+math.pow((Haumea7y.values[j]-uranusY.values[j]),2)+math.pow((Haumea7z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea7CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea7x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea7y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea7z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea7CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(Haumea8Distance)):
    if math.sqrt(math.pow((Haumea8x.values[j]-jupiterX.values[j]),2)+math.pow((Haumea8y.values[j]-jupiterY.values[j]),2)+math.pow((Haumea8z.values[j]-jupiterZ.values[j]),2))<=1.065:
        Haumea8CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea8x.values[j]-saturnX.values[j]),2)+math.pow((Haumea8y.values[j]-saturnY.values[j]),2)+math.pow((Haumea8z.values[j]-saturnZ.values[j]),2))<=1.314:
        Haumea8CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea8x.values[j]-uranusX.values[j]),2)+math.pow((Haumea8y.values[j]-uranusY.values[j]),2)+math.pow((Haumea8z.values[j]-uranusZ.values[j]),2))<=1.407:
        Haumea8CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((Haumea8x.values[j]-neptuneX.values[j]),2)+math.pow((Haumea8y.values[j]-neptuneY.values[j]),2)+math.pow((Haumea8z.values[j]-neptuneZ.values[j]),2))<=2.325:
        Haumea8CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

#######################


if len(Haumea1CE)>0:
    np.savetxt("Haumea1CE.csv", Haumea1CE, fmt='%s') 
    df = pd.read_csv('Haumea1CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea1'}, inplace=True)
    df.to_csv('Haumea1CE.csv', index=False) 
if len(Haumea2CE)>0:               
    np.savetxt("Haumea2CE.csv", Haumea2CE, fmt='%s') 
    df = pd.read_csv('Haumea2CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea2'}, inplace=True)
    df.to_csv('Haumea2CE.csv', index=False) 
if len(Haumea3CE)>0:                   
    np.savetxt("Haumea3CE.csv", Haumea3CE, fmt='%s') 
    df = pd.read_csv('Haumea3CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea3'}, inplace=True)
    df.to_csv('Haumea3CE.csv', index=False) 
if len(Haumea4CE)>0:
    np.savetxt("Haumea4CE.csv", Haumea4CE, fmt='%s') 
    df = pd.read_csv('Haumea4CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea4'}, inplace=True)
    df.to_csv('Haumea4CE.csv', index=False) 
if len(Haumea5CE)>0:
    np.savetxt("Haumea5CE.csv", Haumea5CE, fmt='%s') 
    df = pd.read_csv('Haumea5CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea5'}, inplace=True)
    df.to_csv('Haumea5CE.csv', index=False) 
if len(Haumea6CE)>0:                  
    np.savetxt("Haumea6CE.csv", Haumea6CE, fmt='%s') 
    df = pd.read_csv('Haumea6CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea6'}, inplace=True)
    df.to_csv('Haumea6CE.csv', index=False) 
if len(Haumea7CE)>0:
    np.savetxt("Haumea7CE.csv", Haumea7CE, fmt='%s') 
    df = pd.read_csv('Haumea7CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea7'}, inplace=True)
    df.to_csv('Haumea7CE.csv', index=False) 
if len(Haumea8CE)>0:                  
    np.savetxt("Haumea8CE.csv", Haumea8CE, fmt='%s') 
    df = pd.read_csv('Haumea8CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone Haumea8'}, inplace=True)
    df.to_csv('Haumea8CE.csv', index=False) 
        

print("Complete 3")




