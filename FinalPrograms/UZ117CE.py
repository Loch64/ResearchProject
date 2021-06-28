#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

maxValue = 0

UZ1171 = np.loadtxt('./distanceData/UZ1171Distance.csv', skiprows=1) #open('./distanceData/UZ1171Distance.csv').read().split('\n')
UZ1171Distance = []
count1 = 0
nrows1 = 0
for i in range(len(UZ1171)):
    if float(UZ1171[i])!=0 and float(UZ1171[i])<100 and count1==0:
        UZ1171Distance.append(float(UZ1171[i]))
        nrows1 += 1
    elif float(UZ1171[i])>100 and count1==0:
        UZ1171Distance.append(float(UZ1171[i]))
        count1 += 1
        nrows1 += 1
        break
if len(UZ1171Distance)>maxValue:
    maxValue = len(UZ1171Distance)

UZ1172 = np.loadtxt('./distanceData/UZ1172Distance.csv', skiprows=1)
UZ1172Distance = []
count2 = 0
nrows2 = 0
for i in range(len(UZ1172)):
    if float(UZ1172[i])!=0 and float(UZ1172[i])<100 and count2==0:
        UZ1172Distance.append(float(UZ1172[i]))
        nrows2 += 1
    elif float(UZ1172[i])>100 and count2==0:
        UZ1172Distance.append(float(UZ1172[i]))
        count2 += 1
        nrows2 += 1
        break
if len(UZ1172Distance)>maxValue:
    maxValue = len(UZ1172Distance)
        
UZ1173 = np.loadtxt('./distanceData/UZ1173Distance.csv', skiprows=1)
UZ1173Distance = []
count3 = 0
nrows3 = 0
for i in range(len(UZ1173)):
    if float(UZ1173[i])!=0 and float(UZ1173[i])<100 and count3==0:
        UZ1173Distance.append(float(UZ1173[i]))
        nrows3 += 1
    elif float(UZ1173[i])>100 and count3==0:
        UZ1173Distance.append(float(UZ1173[i]))
        count3 += 1
        nrows3 += 1
        break
if len(UZ1173Distance)>maxValue:
    maxValue = len(UZ1173Distance)
        
UZ1174 = np.loadtxt('./distanceData/UZ1174Distance.csv', skiprows=1)
UZ1174Distance = []
count4 = 0
nrows4 = 0
for i in range(len(UZ1174)):
    if float(UZ1174[i])!=0 and float(UZ1174[i])<100 and count4==0:
        UZ1174Distance.append(float(UZ1174[i]))
        nrows4 += 1
    elif float(UZ1174[i])>100 and count4==0:
        UZ1174Distance.append(float(UZ1174[i]))
        count4 += 1
        nrows4 += 1
        break
if len(UZ1174Distance)>maxValue:
    maxValue = len(UZ1174Distance)
        
UZ1175 = np.loadtxt('./distanceData/UZ1175Distance.csv', skiprows=1)
UZ1175Distance = []
count5 = 0
nrows5 = 0
for i in range(len(UZ1175)):
    if float(UZ1175[i])!=0 and float(UZ1175[i])<100 and count5==0:
        UZ1175Distance.append(float(UZ1175[i]))
        nrows5 += 1
    elif float(UZ1175[i])>100 and count5==0:
        UZ1175Distance.append(float(UZ1175[i]))
        count5 += 1
        nrows5 += 1
        break
if len(UZ1175Distance)>maxValue:
    maxValue = len(UZ1175Distance)
        
UZ1176 = np.loadtxt('./distanceData/UZ1176Distance.csv', skiprows=1)
UZ1176Distance = []
count6 = 0
nrows6 = 0
for i in range(len(UZ1176)):
    if float(UZ1176[i])!=0 and float(UZ1176[i])<100 and count6==0:
        UZ1176Distance.append(float(UZ1176[i]))
        nrows6 += 1
    elif float(UZ1176[i])>100 and count6==0:
        UZ1176Distance.append(float(UZ1176[i]))
        count6 += 1
        nrows6 += 1
        break
if len(UZ1176Distance)>maxValue:
    maxValue = len(UZ1176Distance)
        
UZ1177 = np.loadtxt('./distanceData/UZ1177Distance.csv', skiprows=1)
UZ1177Distance = []
count7 = 0
nrows7 = 0
for i in range(len(UZ1177)):
    if float(UZ1177[i])!=0 and float(UZ1177[i])<100 and count7==0:
        UZ1177Distance.append(float(UZ1177[i]))
        nrows7 += 1
    elif float(UZ1177[i])>100 and count7==0:
        UZ1177Distance.append(float(UZ1177[i]))
        count7 += 1
        nrows7 += 1
        break
if len(UZ1177Distance)>maxValue:
    maxValue = len(UZ1177Distance)
        
UZ1178 = np.loadtxt('./distanceData/UZ1178Distance.csv', skiprows=1)
UZ1178Distance = []
count8 = 0
nrows8 = 0
for i in range(len(UZ1178)):
    if float(UZ1178[i])!=0 and float(UZ1178[i])<100 and count8==0:
        UZ1178Distance.append(float(UZ1178[i]))
        nrows8 += 1
    elif float(UZ1178[i])>100 and count8==0:
        UZ1178Distance.append(float(UZ1178[i]))
        count8 += 1
        nrows8 += 1
        break
if len(UZ1178Distance)>maxValue:
    maxValue = len(UZ1178Distance)

print(maxValue)

jupiterGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Jupiter'], nrows=maxValue)
saturnGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Saturn'], nrows=maxValue)
uranusGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Uranus'], nrows=maxValue)
neptuneGGData = pd.read_csv('./distanceData/FinalGGDataUZ117.csv', usecols=['Neptune'], nrows=maxValue)

jupiterX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZUZ117.csv', usecols=['x'], nrows=maxValue)
jupiterY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZUZ117.csv', usecols=['y'], nrows=maxValue)
jupiterZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZUZ117.csv', usecols=['z'], nrows=maxValue)
saturnX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZUZ117.csv', usecols=['x'], nrows=maxValue)
saturnY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZUZ117.csv', usecols=['y'], nrows=maxValue)
saturnZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZUZ117.csv', usecols=['z'], nrows=maxValue)
uranusX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZUZ117.csv', usecols=['x'], nrows=maxValue)
uranusY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZUZ117.csv', usecols=['y'], nrows=maxValue)
uranusZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZUZ117.csv', usecols=['z'], nrows=maxValue)
neptuneX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZUZ117.csv', usecols=['x'], nrows=maxValue)
neptuneY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZUZ117.csv', usecols=['y'], nrows=maxValue)
neptuneZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZUZ117.csv', usecols=['z'], nrows=maxValue)

UZ1171x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1171.csv', usecols=['x'], nrows=nrows1)
UZ1172x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1172.csv', usecols=['x'], nrows=nrows2)
UZ1173x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1173.csv', usecols=['x'], nrows=nrows3)
UZ1174x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1174.csv', usecols=['x'], nrows=nrows4)
UZ1175x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1175.csv', usecols=['x'], nrows=nrows5)
UZ1176x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1176.csv', usecols=['x'], nrows=nrows6)
UZ1177x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1177.csv', usecols=['x'], nrows=nrows7)
UZ1178x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1178.csv', usecols=['x'], nrows=nrows8)

UZ1171y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1171.csv', usecols=['y'], nrows=nrows1)
UZ1172y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1172.csv', usecols=['y'], nrows=nrows2)
UZ1173y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1173.csv', usecols=['y'], nrows=nrows3)
UZ1174y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1174.csv', usecols=['y'], nrows=nrows4)
UZ1175y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1175.csv', usecols=['y'], nrows=nrows5)
UZ1176y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1176.csv', usecols=['y'], nrows=nrows6)
UZ1177y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1177.csv', usecols=['y'], nrows=nrows7)
UZ1178y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1178.csv', usecols=['y'], nrows=nrows8)

UZ1171z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1171.csv', usecols=['z'], nrows=nrows1)
UZ1172z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1172.csv', usecols=['z'], nrows=nrows2)
UZ1173z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1173.csv', usecols=['z'], nrows=nrows3)
UZ1174z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1174.csv', usecols=['z'], nrows=nrows4)
UZ1175z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1175.csv', usecols=['z'], nrows=nrows5)
UZ1176z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1176.csv', usecols=['z'], nrows=nrows6)
UZ1177z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1177.csv', usecols=['z'], nrows=nrows7)
UZ1178z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000OutputModifiedTest/UZ1178.csv', usecols=['z'], nrows=nrows8)

####################
UZ1171CE = []
UZ1172CE = []
UZ1173CE = []
UZ1174CE = []
UZ1175CE = []
UZ1176CE = []
UZ1177CE = []
UZ1178CE = []

for j in range(len(UZ1171Distance)):
    if math.sqrt(math.pow((UZ1171x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1171y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1171z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1171CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1171x.values[j]-saturnX.values[j]),2)+math.pow((UZ1171y.values[j]-saturnY.values[j]),2)+math.pow((UZ1171z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1171CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1171x.values[j]-uranusX.values[j]),2)+math.pow((UZ1171y.values[j]-uranusY.values[j]),2)+math.pow((UZ1171z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1171CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1171x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1171y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1171z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1171CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(UZ1172Distance)):
    if math.sqrt(math.pow((UZ1172x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1172y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1172z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1172CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1172x.values[j]-saturnX.values[j]),2)+math.pow((UZ1172y.values[j]-saturnY.values[j]),2)+math.pow((UZ1172z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1172CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1172x.values[j]-uranusX.values[j]),2)+math.pow((UZ1172y.values[j]-uranusY.values[j]),2)+math.pow((UZ1172z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1172CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1172x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1172y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1172z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1172CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

for j in range(len(UZ1173Distance)):
    if math.sqrt(math.pow((UZ1173x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1173y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1173z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1173CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1173x.values[j]-saturnX.values[j]),2)+math.pow((UZ1173y.values[j]-saturnY.values[j]),2)+math.pow((UZ1173z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1173CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1173x.values[j]-uranusX.values[j]),2)+math.pow((UZ1173y.values[j]-uranusY.values[j]),2)+math.pow((UZ1173z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1173CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1173x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1173y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1173z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1173CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")   

for j in range(len(UZ1174Distance)):
    if math.sqrt(math.pow((UZ1174x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1174y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1174z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1174CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1174x.values[j]-saturnX.values[j]),2)+math.pow((UZ1174y.values[j]-saturnY.values[j]),2)+math.pow((UZ1174z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1174CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1174x.values[j]-uranusX.values[j]),2)+math.pow((UZ1174y.values[j]-uranusY.values[j]),2)+math.pow((UZ1174z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1174CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1174x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1174y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1174z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1174CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(UZ1175Distance)):
    if math.sqrt(math.pow((UZ1175x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1175y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1175z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1175CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1175x.values[j]-saturnX.values[j]),2)+math.pow((UZ1175y.values[j]-saturnY.values[j]),2)+math.pow((UZ1175z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1175CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1175x.values[j]-uranusX.values[j]),2)+math.pow((UZ1175y.values[j]-uranusY.values[j]),2)+math.pow((UZ1175z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1175CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1175x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1175y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1175z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1175CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(UZ1176Distance)):
    if math.sqrt(math.pow((UZ1176x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1176y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1176z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1176CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1176x.values[j]-saturnX.values[j]),2)+math.pow((UZ1176y.values[j]-saturnY.values[j]),2)+math.pow((UZ1176z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1176CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1176x.values[j]-uranusX.values[j]),2)+math.pow((UZ1176y.values[j]-uranusY.values[j]),2)+math.pow((UZ1176z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1176CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1176x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1176y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1176z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1176CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(UZ1177Distance)):
    if math.sqrt(math.pow((UZ1177x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1177y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1177z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1177CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1177x.values[j]-saturnX.values[j]),2)+math.pow((UZ1177y.values[j]-saturnY.values[j]),2)+math.pow((UZ1177z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1177CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1177x.values[j]-uranusX.values[j]),2)+math.pow((UZ1177y.values[j]-uranusY.values[j]),2)+math.pow((UZ1177z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1177CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1177x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1177y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1177z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1177CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(UZ1178Distance)):
    if math.sqrt(math.pow((UZ1178x.values[j]-jupiterX.values[j]),2)+math.pow((UZ1178y.values[j]-jupiterY.values[j]),2)+math.pow((UZ1178z.values[j]-jupiterZ.values[j]),2))<=1.065:
        UZ1178CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1178x.values[j]-saturnX.values[j]),2)+math.pow((UZ1178y.values[j]-saturnY.values[j]),2)+math.pow((UZ1178z.values[j]-saturnZ.values[j]),2))<=1.314:
        UZ1178CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1178x.values[j]-uranusX.values[j]),2)+math.pow((UZ1178y.values[j]-uranusY.values[j]),2)+math.pow((UZ1178z.values[j]-uranusZ.values[j]),2))<=1.407:
        UZ1178CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((UZ1178x.values[j]-neptuneX.values[j]),2)+math.pow((UZ1178y.values[j]-neptuneY.values[j]),2)+math.pow((UZ1178z.values[j]-neptuneZ.values[j]),2))<=2.325:
        UZ1178CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

#######################


if len(UZ1171CE)>0:
    np.savetxt("UZ1171CE.csv", UZ1171CE, fmt='%s') 
    df = pd.read_csv('UZ1171CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1171'}, inplace=True)
    df.to_csv('UZ1171CE.csv', index=False) 
if len(UZ1172CE)>0:               
    np.savetxt("UZ1172CE.csv", UZ1172CE, fmt='%s') 
    df = pd.read_csv('UZ1172CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1172'}, inplace=True)
    df.to_csv('UZ1172CE.csv', index=False) 
if len(UZ1173CE)>0:                   
    np.savetxt("UZ1173CE.csv", UZ1173CE, fmt='%s') 
    df = pd.read_csv('UZ1173CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1173'}, inplace=True)
    df.to_csv('UZ1173CE.csv', index=False) 
if len(UZ1174CE)>0:
    np.savetxt("UZ1174CE.csv", UZ1174CE, fmt='%s') 
    df = pd.read_csv('UZ1174CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1174'}, inplace=True)
    df.to_csv('UZ1174CE.csv', index=False) 
if len(UZ1175CE)>0:
    np.savetxt("UZ1175CE.csv", UZ1175CE, fmt='%s') 
    df = pd.read_csv('UZ1175CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1175'}, inplace=True)
    df.to_csv('UZ1175CE.csv', index=False) 
if len(UZ1176CE)>0:                  
    np.savetxt("UZ1176CE.csv", UZ1176CE, fmt='%s') 
    df = pd.read_csv('UZ1176CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1176'}, inplace=True)
    df.to_csv('UZ1176CE.csv', index=False) 
if len(UZ1177CE)>0:
    np.savetxt("UZ1177CE.csv", UZ1177CE, fmt='%s') 
    df = pd.read_csv('UZ1177CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1177'}, inplace=True)
    df.to_csv('UZ1177CE.csv', index=False) 
if len(UZ1178CE)>0:                  
    np.savetxt("UZ1178CE.csv", UZ1178CE, fmt='%s') 
    df = pd.read_csv('UZ1178CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone UZ1178'}, inplace=True)
    df.to_csv('UZ1178CE.csv', index=False) 
        

print("Complete 3")
