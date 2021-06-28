#!/usr/bin/env python
# coding: utf-8

# In[4]:


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

    
print("Complete 1")
    
jupiterX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZCB79.csv', usecols=['x'], nrows=maxValue)
jupiterY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZCB79.csv', usecols=['y'], nrows=maxValue)
jupiterZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/jupiterXYZCB79.csv', usecols=['z'], nrows=maxValue)
saturnX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZCB79.csv', usecols=['x'], nrows=maxValue)
saturnY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZCB79.csv', usecols=['y'], nrows=maxValue)
saturnZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/saturnXYZCB79.csv', usecols=['z'], nrows=maxValue)
uranusX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZCB79.csv', usecols=['x'], nrows=maxValue)
uranusY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZCB79.csv', usecols=['y'], nrows=maxValue)
uranusZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/uranusXYZCB79.csv', usecols=['z'], nrows=maxValue)
neptuneX = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZCB79.csv', usecols=['x'], nrows=maxValue)
neptuneY = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZCB79.csv', usecols=['y'], nrows=maxValue)
neptuneZ = pd.read_csv('./USQHPCResultsAndPrograms/FINALGGDATA/neptuneXYZCB79.csv', usecols=['z'], nrows=maxValue)

CB791x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB791.csv', usecols=['x'], nrows=nrows1)
CB792x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB792.csv', usecols=['x'], nrows=nrows2)
CB793x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB793.csv', usecols=['x'], nrows=nrows3)
CB794x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB794.csv', usecols=['x'], nrows=nrows4)
CB795x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB795.csv', usecols=['x'], nrows=nrows5)
CB796x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB796.csv', usecols=['x'], nrows=nrows6)
CB797x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB797.csv', usecols=['x'], nrows=nrows7)
CB798x = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB798.csv', usecols=['x'], nrows=nrows8)

CB791y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB791.csv', usecols=['y'], nrows=nrows1)
CB792y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB792.csv', usecols=['y'], nrows=nrows2)
CB793y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB793.csv', usecols=['y'], nrows=nrows3)
CB794y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB794.csv', usecols=['y'], nrows=nrows4)
CB795y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB795.csv', usecols=['y'], nrows=nrows5)
CB796y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB796.csv', usecols=['y'], nrows=nrows6)
CB797y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB797.csv', usecols=['y'], nrows=nrows7)
CB798y = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB798.csv', usecols=['y'], nrows=nrows8)

CB791z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB791.csv', usecols=['z'], nrows=nrows1)
CB792z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB792.csv', usecols=['z'], nrows=nrows2)
CB793z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB793.csv', usecols=['z'], nrows=nrows3)
CB794z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB794.csv', usecols=['z'], nrows=nrows4)
CB795z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB795.csv', usecols=['z'], nrows=nrows5)
CB796z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB796.csv', usecols=['z'], nrows=nrows6)
CB797z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB797.csv', usecols=['z'], nrows=nrows7)
CB798z = pd.read_csv('./USQHPCResultsAndPrograms/4.5Gyr_180000Output/CB798.csv', usecols=['z'], nrows=nrows8)

####################
CB791CE = []
CB792CE = []
CB793CE = []
CB794CE = []
CB795CE = []
CB796CE = []
CB797CE = []
CB798CE = []

for j in range(len(CB791Distance)):
    if math.sqrt(math.pow((CB791x.values[j]-jupiterX.values[j]),2)+math.pow((CB791y.values[j]-jupiterY.values[j]),2)+math.pow((CB791z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB791CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB791x.values[j]-saturnX.values[j]),2)+math.pow((CB791y.values[j]-saturnY.values[j]),2)+math.pow((CB791z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB791CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB791x.values[j]-uranusX.values[j]),2)+math.pow((CB791y.values[j]-uranusY.values[j]),2)+math.pow((CB791z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB791CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB791x.values[j]-neptuneX.values[j]),2)+math.pow((CB791y.values[j]-neptuneY.values[j]),2)+math.pow((CB791z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB791CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(CB792Distance)):
    if math.sqrt(math.pow((CB792x.values[j]-jupiterX.values[j]),2)+math.pow((CB792y.values[j]-jupiterY.values[j]),2)+math.pow((CB792z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB792CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB792x.values[j]-saturnX.values[j]),2)+math.pow((CB792y.values[j]-saturnY.values[j]),2)+math.pow((CB792z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB792CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB792x.values[j]-uranusX.values[j]),2)+math.pow((CB792y.values[j]-uranusY.values[j]),2)+math.pow((CB792z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB792CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB792x.values[j]-neptuneX.values[j]),2)+math.pow((CB792y.values[j]-neptuneY.values[j]),2)+math.pow((CB792z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB792CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

for j in range(len(CB793Distance)):
    if math.sqrt(math.pow((CB793x.values[j]-jupiterX.values[j]),2)+math.pow((CB793y.values[j]-jupiterY.values[j]),2)+math.pow((CB793z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB793CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB793x.values[j]-saturnX.values[j]),2)+math.pow((CB793y.values[j]-saturnY.values[j]),2)+math.pow((CB793z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB793CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB793x.values[j]-uranusX.values[j]),2)+math.pow((CB793y.values[j]-uranusY.values[j]),2)+math.pow((CB793z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB793CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB793x.values[j]-neptuneX.values[j]),2)+math.pow((CB793y.values[j]-neptuneY.values[j]),2)+math.pow((CB793z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB793CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")   

for j in range(len(CB794Distance)):
    if math.sqrt(math.pow((CB794x.values[j]-jupiterX.values[j]),2)+math.pow((CB794y.values[j]-jupiterY.values[j]),2)+math.pow((CB794z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB794CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB794x.values[j]-saturnX.values[j]),2)+math.pow((CB794y.values[j]-saturnY.values[j]),2)+math.pow((CB794z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB794CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB794x.values[j]-uranusX.values[j]),2)+math.pow((CB794y.values[j]-uranusY.values[j]),2)+math.pow((CB794z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB794CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB794x.values[j]-neptuneX.values[j]),2)+math.pow((CB794y.values[j]-neptuneY.values[j]),2)+math.pow((CB794z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB794CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(CB795Distance)):
    if math.sqrt(math.pow((CB795x.values[j]-jupiterX.values[j]),2)+math.pow((CB795y.values[j]-jupiterY.values[j]),2)+math.pow((CB795z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB795CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB795x.values[j]-saturnX.values[j]),2)+math.pow((CB795y.values[j]-saturnY.values[j]),2)+math.pow((CB795z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB795CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB795x.values[j]-uranusX.values[j]),2)+math.pow((CB795y.values[j]-uranusY.values[j]),2)+math.pow((CB795z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB795CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB795x.values[j]-neptuneX.values[j]),2)+math.pow((CB795y.values[j]-neptuneY.values[j]),2)+math.pow((CB795z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB795CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(CB796Distance)):
    if math.sqrt(math.pow((CB796x.values[j]-jupiterX.values[j]),2)+math.pow((CB796y.values[j]-jupiterY.values[j]),2)+math.pow((CB796z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB796CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB796x.values[j]-saturnX.values[j]),2)+math.pow((CB796y.values[j]-saturnY.values[j]),2)+math.pow((CB796z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB796CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB796x.values[j]-uranusX.values[j]),2)+math.pow((CB796y.values[j]-uranusY.values[j]),2)+math.pow((CB796z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB796CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB796x.values[j]-neptuneX.values[j]),2)+math.pow((CB796y.values[j]-neptuneY.values[j]),2)+math.pow((CB796z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB796CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(CB797Distance)):
    if math.sqrt(math.pow((CB797x.values[j]-jupiterX.values[j]),2)+math.pow((CB797y.values[j]-jupiterY.values[j]),2)+math.pow((CB797z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB797CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB797x.values[j]-saturnX.values[j]),2)+math.pow((CB797y.values[j]-saturnY.values[j]),2)+math.pow((CB797z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB797CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB797x.values[j]-uranusX.values[j]),2)+math.pow((CB797y.values[j]-uranusY.values[j]),2)+math.pow((CB797z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB797CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB797x.values[j]-neptuneX.values[j]),2)+math.pow((CB797y.values[j]-neptuneY.values[j]),2)+math.pow((CB797z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB797CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")
        
for j in range(len(CB798Distance)):
    if math.sqrt(math.pow((CB798x.values[j]-jupiterX.values[j]),2)+math.pow((CB798y.values[j]-jupiterY.values[j]),2)+math.pow((CB798z.values[j]-jupiterZ.values[j]),2))<=1.065:
        CB798CE.append("Close encounter of JUPITER at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB798x.values[j]-saturnX.values[j]),2)+math.pow((CB798y.values[j]-saturnY.values[j]),2)+math.pow((CB798z.values[j]-saturnZ.values[j]),2))<=1.314:
        CB798CE.append("Close encounter of SATURN at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB798x.values[j]-uranusX.values[j]),2)+math.pow((CB798y.values[j]-uranusY.values[j]),2)+math.pow((CB798z.values[j]-uranusZ.values[j]),2))<=1.407:
        CB798CE.append("Close encounter of URANUS at "+str(j*25000)+" years")
    elif math.sqrt(math.pow((CB798x.values[j]-neptuneX.values[j]),2)+math.pow((CB798y.values[j]-neptuneY.values[j]),2)+math.pow((CB798z.values[j]-neptuneZ.values[j]),2))<=2.325:
        CB798CE.append("Close encounter of NEPTUNE at "+str(j*25000)+" years")

#######################


if len(CB791CE)>0:
    np.savetxt("CB791CE.csv", CB791CE, fmt='%s') 
    df = pd.read_csv('CB791CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB791'}, inplace=True)
    df.to_csv('CB791CE.csv', index=False) 
if len(CB792CE)>0:               
    np.savetxt("CB792CE.csv", CB792CE, fmt='%s') 
    df = pd.read_csv('CB792CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB792'}, inplace=True)
    df.to_csv('CB792CE.csv', index=False) 
if len(CB793CE)>0:                   
    np.savetxt("CB793CE.csv", CB793CE, fmt='%s') 
    df = pd.read_csv('CB793CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB793'}, inplace=True)
    df.to_csv('CB793CE.csv', index=False) 
if len(CB794CE)>0:
    np.savetxt("CB794CE.csv", CB794CE, fmt='%s') 
    df = pd.read_csv('CB794CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB794'}, inplace=True)
    df.to_csv('CB794CE.csv', index=False) 
if len(CB795CE)>0:
    np.savetxt("CB795CE.csv", CB795CE, fmt='%s') 
    df = pd.read_csv('CB795CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB795'}, inplace=True)
    df.to_csv('CB795CE.csv', index=False) 
if len(CB796CE)>0:                  
    np.savetxt("CB796CE.csv", CB796CE, fmt='%s') 
    df = pd.read_csv('CB796CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB796'}, inplace=True)
    df.to_csv('CB796CE.csv', index=False) 
if len(CB797CE)>0:
    np.savetxt("CB797CE.csv", CB797CE, fmt='%s') 
    df = pd.read_csv('CB797CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB797'}, inplace=True)
    df.to_csv('CB797CE.csv', index=False) 
if len(CB798CE)>0:                  
    np.savetxt("CB798CE.csv", CB798CE, fmt='%s') 
    df = pd.read_csv('CB798CE.csv', header=None)
    df.rename(columns={0: 'Close encounters of the clone CB798'}, inplace=True)
    df.to_csv('CB798CE.csv', index=False) 
        

print("Complete 3")


