#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Haumea
lowerValueXHaumea = -4.599717797858857e+01 - 1.91381851e-04
upperValueXHaumea = -4.599717797858857e+01 + 1.91381851e-04
lowerValueYHaumea = -5.122234721042839e+00 - 2.98402290e-05
upperValueYHaumea = -5.122234721042839e+00 + 2.98402290e-05
lowerValueZHaumea = 2.238566634229499e+01 - 9.54655948e-05
upperValueZHaumea = 2.238566634229499e+01 + 9.54655948e-05
lowerValueVXHaumea = 4.822841731276640e-04 - 1.46937240e-08
upperValueVXHaumea = 4.822841731276640e-04 + 1.46937240e-08
lowerValueVYHaumea = -2.069938387294513e-03 - 1.05605779e-08
upperValueVYHaumea = -2.069938387294513e-03 + 1.05605779e-08
lowerValueVZHaumea = 3.679397601691202e-04 - 8.41178128e-09
upperValueVZHaumea = 3.679397601691202e-04 + 8.41178128e-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

HaumeaXRange = np.linspace(lowerValueXHaumea, upperValueXHaumea, nClones)
HaumeaYRange = np.linspace(lowerValueYHaumea, upperValueYHaumea, nClones)
HaumeaZRange = np.linspace(lowerValueZHaumea, upperValueZHaumea, nClones)
HaumeaVX = (4.822841731276640e-04)*365.25      #velocity in au/year
HaumeaVY = (-2.069938387294513e-03)*365.25
HaumeaVZ = (3.679397601691202e-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
#for i in range(nClones):
    #sim.add(x=HaumeaXRange[i], y=HaumeaYRange[i], z=HaumeaZRange[i], vx=HaumeaVX, vy=HaumeaVY, vz=HaumeaVZ)
    
#sim.save("solarSystemHaumea.bin")

sim = rebound.Simulation("solarSystemHaumea.bin") #The saved file has the corrected units as shown above
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
        
    
Haumea1 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
Haumea2 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
Haumea3 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
Haumea4 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
Haumea5 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
Haumea6 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
Haumea7 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
Haumea8 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    Haumea1[i,0] = clone1X[i]
    Haumea1[i,1] = clone1Y[i]
    Haumea1[i,2] = clone1Z[i]
    Haumea1[i,3] = clone1OrbitData[i,0]
    Haumea1[i,4] = clone1OrbitData[i,1]
    Haumea1[i,5] = clone1OrbitData[i,2]
    Haumea2[i,0] = clone2X[i]
    Haumea2[i,1] = clone2Y[i]
    Haumea2[i,2] = clone2Z[i]
    Haumea2[i,3] = clone2OrbitData[i,0]
    Haumea2[i,4] = clone2OrbitData[i,1]
    Haumea2[i,5] = clone2OrbitData[i,2]
    Haumea3[i,0] = clone3X[i]
    Haumea3[i,1] = clone3Y[i]
    Haumea3[i,2] = clone3Z[i]
    Haumea3[i,3] = clone3OrbitData[i,0]
    Haumea3[i,4] = clone3OrbitData[i,1]
    Haumea3[i,5] = clone3OrbitData[i,2]
    Haumea4[i,0] = clone4X[i]
    Haumea4[i,1] = clone4Y[i]
    Haumea4[i,2] = clone4Z[i]
    Haumea4[i,3] = clone4OrbitData[i,0]
    Haumea4[i,4] = clone4OrbitData[i,1]
    Haumea4[i,5] = clone4OrbitData[i,2]
    Haumea5[i,0] = clone5X[i]
    Haumea5[i,1] = clone5Y[i]
    Haumea5[i,2] = clone5Z[i]
    Haumea5[i,3] = clone5OrbitData[i,0]
    Haumea5[i,4] = clone5OrbitData[i,1]
    Haumea5[i,5] = clone5OrbitData[i,2]
    Haumea6[i,0] = clone6X[i]
    Haumea6[i,1] = clone6Y[i]
    Haumea6[i,2] = clone6Z[i]
    Haumea6[i,3] = clone6OrbitData[i,0]
    Haumea6[i,4] = clone6OrbitData[i,1]
    Haumea6[i,5] = clone6OrbitData[i,2]
    Haumea7[i,0] = clone7X[i]
    Haumea7[i,1] = clone7Y[i]
    Haumea7[i,2] = clone7Z[i]
    Haumea7[i,3] = clone7OrbitData[i,0]
    Haumea7[i,4] = clone7OrbitData[i,1]
    Haumea7[i,5] = clone7OrbitData[i,2]
    Haumea8[i,0] = clone8X[i]
    Haumea8[i,1] = clone8Y[i]
    Haumea8[i,2] = clone8Z[i]
    Haumea8[i,3] = clone8OrbitData[i,0]
    Haumea8[i,4] = clone8OrbitData[i,1]
    Haumea8[i,5] = clone8OrbitData[i,2]

    
np.savetxt("Haumea1.csv", Haumea1, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('Haumea1.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea1.csv', index=False) 

np.savetxt("Haumea2.csv", Haumea2, delimiter=",")
df = pd.read_csv('Haumea2.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea2.csv', index=False)

np.savetxt("Haumea3.csv", Haumea3, delimiter=",")
df = pd.read_csv('Haumea3.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea3.csv', index=False)
    
np.savetxt("Haumea4.csv", Haumea4, delimiter=",")
df = pd.read_csv('Haumea4.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea4.csv', index=False)
    
np.savetxt("Haumea5.csv", Haumea5, delimiter=",")
df = pd.read_csv('Haumea5.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea5.csv', index=False)
    
np.savetxt("Haumea6.csv", Haumea6, delimiter=",")
df = pd.read_csv('Haumea6.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea6.csv', index=False)
    
np.savetxt("Haumea7.csv", Haumea7, delimiter=",")
df = pd.read_csv('Haumea7.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea7.csv', index=False)
    
np.savetxt("Haumea8.csv", Haumea8, delimiter=",")
df = pd.read_csv('Haumea8.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('Haumea8.csv', index=False)

np.savetxt("jupiterXYZHaumea.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZHaumea.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZHaumea.csv', index=False)

np.savetxt("saturnXYZHaumea.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZHaumea.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZHaumea.csv', index=False)

np.savetxt("uranusXYZHaumea.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZHaumea.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZHaumea.csv', index=False)

np.savetxt("neptuneXYZHaumea.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZHaumea.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZHaumea.csv', index=False)

print("Finished")

