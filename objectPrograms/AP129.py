#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#AP129
lowerValueXAP129 = -8.884500778179113E+00 - 1.15895303E-04
upperValueXAP129 = -8.884500778179113E+00 + 1.15895303E-04
lowerValueYAP129 = 3.133929737455337E+01 - 2.10684032E-04
upperValueYAP129 = 3.133929737455337E+01 + 2.10684032E-04
lowerValueZAP129 = 1.688599966269764E+01 - 1.20921986E-04
upperValueZAP129 = 1.688599966269764E+01 + 1.20921986E-04
lowerValueVXAP129 = -2.941163056819511E-03 - 1.93243671E-08
upperValueVXAP129 = -2.941163056819511E-03 + 1.93243671E-08
lowerValueVYAP129 = -6.348344188255159E-04 - 2.73871032E-08
upperValueVYAP129 = -6.348344188255159E-04 + 2.73871032E-08
lowerValueVZAP129 = 7.408813854578731E-05 - 1.53906315E-08
upperValueVZAP129 = 7.408813854578731E-05 + 1.53906315E-08

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

AP129XRange = np.linspace(lowerValueXAP129, upperValueXAP129, nClones)
AP129YRange = np.linspace(lowerValueYAP129, upperValueYAP129, nClones)
AP129ZRange = np.linspace(lowerValueZAP129, upperValueZAP129, nClones)
AP129VX = (-2.941163056819511E-03)*365.25      #velocity in au/year
AP129VY = (-6.348344188255159E-04)*365.25
AP129VZ = (7.408813854578731E-05)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=AP129XRange[i], y=AP129YRange[i], z=AP129ZRange[i], vx=AP129VX, vy=AP129VY, vz=AP129VZ)
    
#sim.save("solarSystemAP129.bin")

sim = rebound.Simulation("solarSystemAP129.bin") #The saved file has the corrected units as shown above
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
        
    
AP1291 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AP1292 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AP1293 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AP1294 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AP1295 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AP1296 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AP1297 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AP1298 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    AP1291[i,0] = clone1X[i]
    AP1291[i,1] = clone1Y[i]
    AP1291[i,2] = clone1Z[i]
    AP1291[i,3] = clone1OrbitData[i,0]
    AP1291[i,4] = clone1OrbitData[i,1]
    AP1291[i,5] = clone1OrbitData[i,2]
    AP1292[i,0] = clone2X[i]
    AP1292[i,1] = clone2Y[i]
    AP1292[i,2] = clone2Z[i]
    AP1292[i,3] = clone2OrbitData[i,0]
    AP1292[i,4] = clone2OrbitData[i,1]
    AP1292[i,5] = clone2OrbitData[i,2]
    AP1293[i,0] = clone3X[i]
    AP1293[i,1] = clone3Y[i]
    AP1293[i,2] = clone3Z[i]
    AP1293[i,3] = clone3OrbitData[i,0]
    AP1293[i,4] = clone3OrbitData[i,1]
    AP1293[i,5] = clone3OrbitData[i,2]
    AP1294[i,0] = clone4X[i]
    AP1294[i,1] = clone4Y[i]
    AP1294[i,2] = clone4Z[i]
    AP1294[i,3] = clone4OrbitData[i,0]
    AP1294[i,4] = clone4OrbitData[i,1]
    AP1294[i,5] = clone4OrbitData[i,2]
    AP1295[i,0] = clone5X[i]
    AP1295[i,1] = clone5Y[i]
    AP1295[i,2] = clone5Z[i]
    AP1295[i,3] = clone5OrbitData[i,0]
    AP1295[i,4] = clone5OrbitData[i,1]
    AP1295[i,5] = clone5OrbitData[i,2]
    AP1296[i,0] = clone6X[i]
    AP1296[i,1] = clone6Y[i]
    AP1296[i,2] = clone6Z[i]
    AP1296[i,3] = clone6OrbitData[i,0]
    AP1296[i,4] = clone6OrbitData[i,1]
    AP1296[i,5] = clone6OrbitData[i,2]
    AP1297[i,0] = clone7X[i]
    AP1297[i,1] = clone7Y[i]
    AP1297[i,2] = clone7Z[i]
    AP1297[i,3] = clone7OrbitData[i,0]
    AP1297[i,4] = clone7OrbitData[i,1]
    AP1297[i,5] = clone7OrbitData[i,2]
    AP1298[i,0] = clone8X[i]
    AP1298[i,1] = clone8Y[i]
    AP1298[i,2] = clone8Z[i]
    AP1298[i,3] = clone8OrbitData[i,0]
    AP1298[i,4] = clone8OrbitData[i,1]
    AP1298[i,5] = clone8OrbitData[i,2]

    
np.savetxt("AP1291.csv", AP1291, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('AP1291.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1291.csv', index=False) 

np.savetxt("AP1292.csv", AP1292, delimiter=",")
df = pd.read_csv('AP1292.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1292.csv', index=False)

np.savetxt("AP1293.csv", AP1293, delimiter=",")
df = pd.read_csv('AP1293.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1293.csv', index=False)
    
np.savetxt("AP1294.csv", AP1294, delimiter=",")
df = pd.read_csv('AP1294.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1294.csv', index=False)
    
np.savetxt("AP1295.csv", AP1295, delimiter=",")
df = pd.read_csv('AP1295.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1295.csv', index=False)
    
np.savetxt("AP1296.csv", AP1296, delimiter=",")
df = pd.read_csv('AP1296.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1296.csv', index=False)
    
np.savetxt("AP1297.csv", AP1297, delimiter=",")
df = pd.read_csv('AP1297.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1297.csv', index=False)
    
np.savetxt("AP1298.csv", AP1298, delimiter=",")
df = pd.read_csv('AP1298.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AP1298.csv', index=False)

np.savetxt("jupiterXYZAP129.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZAP129.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZAP129.csv', index=False)

np.savetxt("saturnXYZAP129.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZAP129.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZAP129.csv', index=False)

np.savetxt("uranusXYZAP129.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZAP129.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZAP129.csv', index=False)

np.savetxt("neptuneXYZAP129.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZAP129.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZAP129.csv', index=False)

print("Finished")

