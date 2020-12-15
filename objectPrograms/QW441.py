#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#QW441
lowerValueXQW441 = 3.692283242711004E+01 - 2.79219900E-04
upperValueXQW441 = 3.692283242711004E+01 + 2.79219900E-04
lowerValueYQW441 = -1.589273237766664E+01 - 9.45145327E-05
upperValueYQW441 = -1.589273237766664E+01 + 9.45145327E-05
lowerValueZQW441 = 2.318094371319762E+00 - 2.25901894E-05
upperValueZQW441 = 2.318094371319762E+00 + 2.25901894E-05
lowerValueVXQW441 = 9.285830698294615E-04 - 2.77681813E-08
upperValueVXQW441 = 9.285830698294615E-04 + 2.77681813E-08
lowerValueVYQW441 = 2.304673474551662E-03 - 1.67471166E-08
upperValueVYQW441 = 2.304673474551662E-03 + 1.67471166E-08
lowerValueVZQW441 = -1.361776799218450E-03 - 7.22378982E-09
upperValueVZQW441 = -1.361776799218450E-03 + 7.22378982E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

QW441XRange = np.linspace(lowerValueXQW441, upperValueXQW441, nClones)
QW441YRange = np.linspace(lowerValueYQW441, upperValueYQW441, nClones)
QW441ZRange = np.linspace(lowerValueZQW441, upperValueZQW441, nClones)
QW441VX = (9.285830698294615E-04)*365.25      #velocity in au/year
QW441VY = (2.304673474551662E-03)*365.25
QW441VZ = (-1.361776799218450E-03)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=QW441XRange[i], y=QW441YRange[i], z=QW441ZRange[i], vx=QW441VX, vy=QW441VY, vz=QW441VZ)
    
#sim.save("solarSystemQW441.bin")

sim = rebound.Simulation("solarSystemQW441.bin") #The saved file has the corrected units as shown above
sim.move_to_com() #move to centre of momentum frame. Is it necessary?
sim.integrator = "mercurius"
#Jupiter's sidereal orbit: 11.86 years. dt = 11.86/30 = 0.395333333    From NASA Cosmos
sim.dt = 0.395333333
nOutputs = 2529 #The correct number of outputs over 4.5billion years would be approx 11,382,799,355 (4.5Gyr/dt)
particles = sim.particles
times = np.linspace(0., 1000, nOutputs) 
dtype = [('x', np.float64), ('y', np.float64), ('z', np.float64)]

clone1X = np.zeros(nOutputs)
clone2X = np.zeros(nOutputs)
clone3X = np.zeros(nOutputs)
clone4X = np.zeros(nOutputs)
clone5X = np.zeros(nOutputs)
clone6X = np.zeros(nOutputs)
clone7X = np.zeros(nOutputs)
clone8X = np.zeros(nOutputs)

clone1Y = np.zeros(nOutputs)
clone2Y = np.zeros(nOutputs)
clone3Y = np.zeros(nOutputs)
clone4Y = np.zeros(nOutputs)
clone5Y = np.zeros(nOutputs)
clone6Y = np.zeros(nOutputs)
clone7Y = np.zeros(nOutputs)
clone8Y = np.zeros(nOutputs)

clone1Z = np.zeros(nOutputs)
clone2Z = np.zeros(nOutputs)
clone3Z = np.zeros(nOutputs)
clone4Z = np.zeros(nOutputs)
clone5Z = np.zeros(nOutputs)
clone6Z = np.zeros(nOutputs)
clone7Z = np.zeros(nOutputs)
clone8Z = np.zeros(nOutputs)

clone1OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)
clone2OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)
clone3OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)
clone4OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)
clone5OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)
clone6OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)
clone7OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)
clone8OrbitData = np.zeros(nOutputs*3).reshape(nOutputs, 3)    
counterClone1 = 0    
counterClone2 = 0 
counterClone3 = 0 
counterClone4 = 0 
counterClone5 = 0 
counterClone6 = 0 
counterClone7 = 0 
counterClone8 = 0 

jupiterXYZ = np.zeros(nOutputs*3).reshape(nOutputs, 3)
saturnXYZ = np.zeros(nOutputs*3).reshape(nOutputs, 3)
uranusXYZ = np.zeros(nOutputs*3).reshape(nOutputs, 3)
neptuneXYZ = np.zeros(nOutputs*3).reshape(nOutputs, 3)

for i,time in enumerate(times):
    sim.integrate(time)
    clone1X[i] = particles[10].x
    clone2X[i] = particles[11].x
    clone3X[i] = particles[12].x
    clone4X[i] = particles[13].x
    clone5X[i] = particles[14].x
    clone6X[i] = particles[15].x
    clone7X[i] = particles[16].x
    clone8X[i] = particles[17].x
    clone1Y[i] = particles[10].y
    clone2Y[i] = particles[11].y
    clone3Y[i] = particles[12].y
    clone4Y[i] = particles[13].y
    clone5Y[i] = particles[14].y
    clone6Y[i] = particles[15].y
    clone7Y[i] = particles[16].y
    clone8Y[i] = particles[17].y
    clone1Z[i] = particles[10].z
    clone2Z[i] = particles[11].z
    clone3Z[i] = particles[12].z
    clone4Z[i] = particles[13].z
    clone5Z[i] = particles[14].z
    clone6Z[i] = particles[15].z
    clone7Z[i] = particles[16].z
    clone8Z[i] = particles[17].z
    jupiterXYZ[i,0] = particles[5].x
    jupiterXYZ[i,1] = particles[5].y
    jupiterXYZ[i,2] = particles[5].z
    saturnXYZ[i,0] = particles[6].x
    saturnXYZ[i,1] = particles[6].y
    saturnXYZ[i,2] = particles[6].z
    uranusXYZ[i,0] = particles[7].x
    uranusXYZ[i,1] = particles[7].y
    uranusXYZ[i,2] = particles[7].z
    neptuneXYZ[i,0] = particles[8].x
    neptuneXYZ[i,1] = particles[8].y
    neptuneXYZ[i,2] = particles[8].z
    for j,orbit in enumerate(sim.calculate_orbits()): #since there are no switch case in python, nested if-else is used
        if j==9:
            clone1OrbitData[counterClone1,0] = orbit.a
            clone1OrbitData[counterClone1,1] = orbit.inc
            clone1OrbitData[counterClone1,2] = orbit.e
            counterClone1 += 1
        elif j==10:
            clone2OrbitData[counterClone2,0] = orbit.a
            clone2OrbitData[counterClone2,1] = orbit.inc
            clone2OrbitData[counterClone2,2] = orbit.e
            counterClone2 += 1
        elif j==11:
            clone3OrbitData[counterClone3,0] = orbit.a
            clone3OrbitData[counterClone3,1] = orbit.inc
            clone3OrbitData[counterClone3,2] = orbit.e
            counterClone3 += 1
        elif j==12:
            clone4OrbitData[counterClone4,0] = orbit.a
            clone4OrbitData[counterClone4,1] = orbit.inc
            clone4OrbitData[counterClone4,2] = orbit.e
            counterClone4 += 1
        elif j==13:
            clone5OrbitData[counterClone5,0] = orbit.a
            clone5OrbitData[counterClone5,1] = orbit.inc
            clone5OrbitData[counterClone5,2] = orbit.e
            counterClone5 += 1
        elif j==14:
            clone6OrbitData[counterClone6,0] = orbit.a
            clone6OrbitData[counterClone6,1] = orbit.inc
            clone6OrbitData[counterClone6,2] = orbit.e
            counterClone6 += 1
        elif j==15:
            clone7OrbitData[counterClone7,0] = orbit.a
            clone7OrbitData[counterClone7,1] = orbit.inc
            clone7OrbitData[counterClone7,2] = orbit.e
            counterClone7 += 1
        elif j==16:
            clone8OrbitData[counterClone8,0] = orbit.a
            clone8OrbitData[counterClone8,1] = orbit.inc
            clone8OrbitData[counterClone8,2] = orbit.e
            counterClone8 += 1
        
    
QW4411 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
QW4412 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
QW4413 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
QW4414 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
QW4415 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
QW4416 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
QW4417 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
QW4418 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    QW4411[i,0] = clone1X[i]
    QW4411[i,1] = clone1Y[i]
    QW4411[i,2] = clone1Z[i]
    QW4411[i,3] = clone1OrbitData[i,0]
    QW4411[i,4] = clone1OrbitData[i,1]
    QW4411[i,5] = clone1OrbitData[i,2]
    QW4412[i,0] = clone2X[i]
    QW4412[i,1] = clone2Y[i]
    QW4412[i,2] = clone2Z[i]
    QW4412[i,3] = clone2OrbitData[i,0]
    QW4412[i,4] = clone2OrbitData[i,1]
    QW4412[i,5] = clone2OrbitData[i,2]
    QW4413[i,0] = clone3X[i]
    QW4413[i,1] = clone3Y[i]
    QW4413[i,2] = clone3Z[i]
    QW4413[i,3] = clone3OrbitData[i,0]
    QW4413[i,4] = clone3OrbitData[i,1]
    QW4413[i,5] = clone3OrbitData[i,2]
    QW4414[i,0] = clone4X[i]
    QW4414[i,1] = clone4Y[i]
    QW4414[i,2] = clone4Z[i]
    QW4414[i,3] = clone4OrbitData[i,0]
    QW4414[i,4] = clone4OrbitData[i,1]
    QW4414[i,5] = clone4OrbitData[i,2]
    QW4415[i,0] = clone5X[i]
    QW4415[i,1] = clone5Y[i]
    QW4415[i,2] = clone5Z[i]
    QW4415[i,3] = clone5OrbitData[i,0]
    QW4415[i,4] = clone5OrbitData[i,1]
    QW4415[i,5] = clone5OrbitData[i,2]
    QW4416[i,0] = clone6X[i]
    QW4416[i,1] = clone6Y[i]
    QW4416[i,2] = clone6Z[i]
    QW4416[i,3] = clone6OrbitData[i,0]
    QW4416[i,4] = clone6OrbitData[i,1]
    QW4416[i,5] = clone6OrbitData[i,2]
    QW4417[i,0] = clone7X[i]
    QW4417[i,1] = clone7Y[i]
    QW4417[i,2] = clone7Z[i]
    QW4417[i,3] = clone7OrbitData[i,0]
    QW4417[i,4] = clone7OrbitData[i,1]
    QW4417[i,5] = clone7OrbitData[i,2]
    QW4418[i,0] = clone8X[i]
    QW4418[i,1] = clone8Y[i]
    QW4418[i,2] = clone8Z[i]
    QW4418[i,3] = clone8OrbitData[i,0]
    QW4418[i,4] = clone8OrbitData[i,1]
    QW4418[i,5] = clone8OrbitData[i,2]

    
np.savetxt("QW4411.csv", QW4411, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('QW4411.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4411.csv', index=False) 

np.savetxt("QW4412.csv", QW4412, delimiter=",")
df = pd.read_csv('QW4412.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4412.csv', index=False)

np.savetxt("QW4413.csv", QW4413, delimiter=",")
df = pd.read_csv('QW4413.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4413.csv', index=False)
    
np.savetxt("QW4414.csv", QW4414, delimiter=",")
df = pd.read_csv('QW4414.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4414.csv', index=False)
    
np.savetxt("QW4415.csv", QW4415, delimiter=",")
df = pd.read_csv('QW4415.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4415.csv', index=False)
    
np.savetxt("QW4416.csv", QW4416, delimiter=",")
df = pd.read_csv('QW4416.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4416.csv', index=False)
    
np.savetxt("QW4417.csv", QW4417, delimiter=",")
df = pd.read_csv('QW4417.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4417.csv', index=False)
    
np.savetxt("QW4418.csv", QW4418, delimiter=",")
df = pd.read_csv('QW4418.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('QW4418.csv', index=False)

np.savetxt("jupiterXYZQW441.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZQW441.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZQW441.csv', index=False)

np.savetxt("saturnXYZQW441.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZQW441.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZQW441.csv', index=False)

np.savetxt("uranusXYZQW441.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZQW441.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZQW441.csv', index=False)

np.savetxt("neptuneXYZQW441.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZQW441.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZQW441.csv', index=False)

print("Finished")

