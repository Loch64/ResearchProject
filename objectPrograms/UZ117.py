#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#UZ117
lowerValueXUZ117 = 3.166659841593118E+01 - 1.55629630E-04
upperValueXUZ117 = 3.166659841593118E+01 + 1.55629630E-04
lowerValueYUZ117 = 2.428550758078162E+01 - 1.47623561E-04
upperValueYUZ117 = 2.428550758078162E+01 + 1.47623561E-04
lowerValueZUZ117 = -4.606357829098204E+00 - 3.98936618E-05
upperValueZUZ117 = -4.606357829098204E+00 + 3.98936618E-05
lowerValueVXUZ117 = -1.866588508363532E-03 - 1.92382700E-08
upperValueVXUZ117 = -1.866588508363532E-03 + 1.92382700E-08
lowerValueVYUZ117 = 1.748866408602661E-03 - 1.55191660E-08
upperValueVYUZ117 = 1.748866408602661E-03 + 1.55191660E-08
lowerValueVZUZ117 = -1.228375401664573E-03 - 5.74531091E-09
upperValueVZUZ117 = -1.228375401664573E-03 + 5.74531091E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

UZ117XRange = np.linspace(lowerValueXUZ117, upperValueXUZ117, nClones)
UZ117YRange = np.linspace(lowerValueYUZ117, upperValueYUZ117, nClones)
UZ117ZRange = np.linspace(lowerValueZUZ117, upperValueZUZ117, nClones)
UZ117VX = (-1.866588508363532E-03)*365.25      #velocity in au/year
UZ117VY = (1.748866408602661E-03)*365.25
UZ117VZ = (-1.228375401664573E-03)*365.25

sim = rebound.Simulation()
sim.units = ('yr', 'AU', 'Msun')
sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
for i in range(nClones):
    sim.add(x=UZ117XRange[i], y=UZ117YRange[i], z=UZ117ZRange[i], vx=UZ117VX, vy=UZ117VY, vz=UZ117VZ)
    
sim.save("solarSystemUZ117.bin")

#sim = rebound.Simulation("solarSystemUZ117.bin") #The saved file has the corrected units as shown above
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
        
    
UZ1171 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UZ1172 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UZ1173 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UZ1174 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UZ1175 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UZ1176 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UZ1177 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UZ1178 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    UZ1171[i,0] = clone1X[i]
    UZ1171[i,1] = clone1Y[i]
    UZ1171[i,2] = clone1Z[i]
    UZ1171[i,3] = clone1OrbitData[i,0]
    UZ1171[i,4] = clone1OrbitData[i,1]
    UZ1171[i,5] = clone1OrbitData[i,2]
    UZ1172[i,0] = clone2X[i]
    UZ1172[i,1] = clone2Y[i]
    UZ1172[i,2] = clone2Z[i]
    UZ1172[i,3] = clone2OrbitData[i,0]
    UZ1172[i,4] = clone2OrbitData[i,1]
    UZ1172[i,5] = clone2OrbitData[i,2]
    UZ1173[i,0] = clone3X[i]
    UZ1173[i,1] = clone3Y[i]
    UZ1173[i,2] = clone3Z[i]
    UZ1173[i,3] = clone3OrbitData[i,0]
    UZ1173[i,4] = clone3OrbitData[i,1]
    UZ1173[i,5] = clone3OrbitData[i,2]
    UZ1174[i,0] = clone4X[i]
    UZ1174[i,1] = clone4Y[i]
    UZ1174[i,2] = clone4Z[i]
    UZ1174[i,3] = clone4OrbitData[i,0]
    UZ1174[i,4] = clone4OrbitData[i,1]
    UZ1174[i,5] = clone4OrbitData[i,2]
    UZ1175[i,0] = clone5X[i]
    UZ1175[i,1] = clone5Y[i]
    UZ1175[i,2] = clone5Z[i]
    UZ1175[i,3] = clone5OrbitData[i,0]
    UZ1175[i,4] = clone5OrbitData[i,1]
    UZ1175[i,5] = clone5OrbitData[i,2]
    UZ1176[i,0] = clone6X[i]
    UZ1176[i,1] = clone6Y[i]
    UZ1176[i,2] = clone6Z[i]
    UZ1176[i,3] = clone6OrbitData[i,0]
    UZ1176[i,4] = clone6OrbitData[i,1]
    UZ1176[i,5] = clone6OrbitData[i,2]
    UZ1177[i,0] = clone7X[i]
    UZ1177[i,1] = clone7Y[i]
    UZ1177[i,2] = clone7Z[i]
    UZ1177[i,3] = clone7OrbitData[i,0]
    UZ1177[i,4] = clone7OrbitData[i,1]
    UZ1177[i,5] = clone7OrbitData[i,2]
    UZ1178[i,0] = clone8X[i]
    UZ1178[i,1] = clone8Y[i]
    UZ1178[i,2] = clone8Z[i]
    UZ1178[i,3] = clone8OrbitData[i,0]
    UZ1178[i,4] = clone8OrbitData[i,1]
    UZ1178[i,5] = clone8OrbitData[i,2]

    
np.savetxt("UZ1171.csv", UZ1171, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('UZ1171.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1171.csv', index=False) 

np.savetxt("UZ1172.csv", UZ1172, delimiter=",")
df = pd.read_csv('UZ1172.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1172.csv', index=False)

np.savetxt("UZ1173.csv", UZ1173, delimiter=",")
df = pd.read_csv('UZ1173.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1173.csv', index=False)
    
np.savetxt("UZ1174.csv", UZ1174, delimiter=",")
df = pd.read_csv('UZ1174.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1174.csv', index=False)
    
np.savetxt("UZ1175.csv", UZ1175, delimiter=",")
df = pd.read_csv('UZ1175.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1175.csv', index=False)
    
np.savetxt("UZ1176.csv", UZ1176, delimiter=",")
df = pd.read_csv('UZ1176.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1176.csv', index=False)
    
np.savetxt("UZ1177.csv", UZ1177, delimiter=",")
df = pd.read_csv('UZ1177.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1177.csv', index=False)
    
np.savetxt("UZ1178.csv", UZ1178, delimiter=",")
df = pd.read_csv('UZ1178.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UZ1178.csv', index=False)

np.savetxt("jupiterXYZUZ117.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZUZ117.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZUZ117.csv', index=False)

np.savetxt("saturnXYZUZ117.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZUZ117.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZUZ117.csv', index=False)

np.savetxt("uranusXYZUZ117.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZUZ117.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZUZ117.csv', index=False)

np.savetxt("neptuneXYZUZ117.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZUZ117.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZUZ117.csv', index=False)

print("Finished")

