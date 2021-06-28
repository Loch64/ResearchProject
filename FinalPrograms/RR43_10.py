#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#RR43
lowerValueXRR43 = 2.715540541667707E+01 - 1.11612762E-04
upperValueXRR43 = 2.715540541667707E+01 + 1.11612762E-04
lowerValueYRR43 = 2.249544653703840E+01 - 1.02227641E-04
upperValueYRR43 = 2.249544653703840E+01 + 1.02227641E-04
lowerValueZRR43 = -1.382470156293514E+01 - 5.81514216E-05
upperValueZRR43 = -1.382470156293514E+01 + 5.81514216E-05
lowerValueVXRR43 = -1.372551507575829E-03 - 1.25774210E-08
upperValueVXRR43 = -1.372551507575829E-03 + 1.25774210E-08
lowerValueVYRR43 = 2.489753187247984E-03 - 9.92868393E-09
upperValueVYRR43 = 2.489753187247984E-03 + 9.92868393E-09
lowerValueVZRR43 = 8.414242338934075E-04 - 6.92969175E-09
upperValueVZRR43 = 8.414242338934075E-04 + 6.92969175E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

RR43XRange = np.linspace(lowerValueXRR43, upperValueXRR43, nClones)
RR43YRange = np.linspace(lowerValueYRR43, upperValueYRR43, nClones)
RR43ZRange = np.linspace(lowerValueZRR43, upperValueZRR43, nClones)
RR43VX = (-1.372551507575829E-03)*365.25      #velocity in au/year
RR43VY = (2.489753187247984E-03)*365.25
RR43VZ = (8.414242338934075E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=RR43XRange[i], y=RR43YRange[i], z=RR43ZRange[i], vx=RR43VX, vy=RR43VY, vz=RR43VZ)
    
#sim.save("solarSystemRR43.bin")

sim = rebound.Simulation("solarSystemRR43.bin") #The saved file has the corrected units as shown above
sim.move_to_com() #move to centre of momentum frame. Is it necessary?
sim.integrator = "mercurius"
#Jupiter's sidereal orbit: 11.86 years. dt = 11.86/30 = 0.395333333    From NASA Cosmos
sim.dt = 0.395333333
nOutputs = 180000 #The correct number of outputs over 4.5billion years would be approx 11,382,799,335 (4.5Gyr/dt)
particles = sim.particles
times = np.linspace(0., 4500000000, nOutputs) 
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
    clone1X[i] = particles[5].x
    clone2X[i] = particles[6].x
    clone3X[i] = particles[7].x
    clone4X[i] = particles[8].x
    clone5X[i] = particles[9].x
    clone6X[i] = particles[10].x
    clone7X[i] = particles[11].x
    clone8X[i] = particles[12].x
    clone1Y[i] = particles[5].y
    clone2Y[i] = particles[6].y
    clone3Y[i] = particles[7].y
    clone4Y[i] = particles[8].y
    clone5Y[i] = particles[9].y
    clone6Y[i] = particles[10].y
    clone7Y[i] = particles[11].y
    clone8Y[i] = particles[12].y
    clone1Z[i] = particles[5].z
    clone2Z[i] = particles[6].z
    clone3Z[i] = particles[7].z
    clone4Z[i] = particles[8].z
    clone5Z[i] = particles[9].z
    clone6Z[i] = particles[10].z
    clone7Z[i] = particles[11].z
    clone8Z[i] = particles[12].z
    jupiterXYZ[i,0] = particles[1].x
    jupiterXYZ[i,1] = particles[1].y
    jupiterXYZ[i,2] = particles[1].z
    saturnXYZ[i,0] = particles[2].x
    saturnXYZ[i,1] = particles[2].y
    saturnXYZ[i,2] = particles[2].z
    uranusXYZ[i,0] = particles[3].x
    uranusXYZ[i,1] = particles[3].y
    uranusXYZ[i,2] = particles[3].z
    neptuneXYZ[i,0] = particles[4].x
    neptuneXYZ[i,1] = particles[4].y
    neptuneXYZ[i,2] = particles[4].z
    clone1OrbitData[i,0] = sim.particles[5].orbit.a
    clone1OrbitData[i,1] = sim.particles[5].orbit.inc
    clone1OrbitData[i,2] = sim.particles[5].orbit.e
    clone2OrbitData[i,0] = sim.particles[6].orbit.a
    clone2OrbitData[i,1] = sim.particles[6].orbit.inc
    clone2OrbitData[i,2] = sim.particles[6].orbit.e
    clone3OrbitData[i,0] = sim.particles[7].orbit.a
    clone3OrbitData[i,1] = sim.particles[7].orbit.inc
    clone3OrbitData[i,2] = sim.particles[7].orbit.e
    clone4OrbitData[i,0] = sim.particles[8].orbit.a
    clone4OrbitData[i,1] = sim.particles[8].orbit.inc
    clone4OrbitData[i,2] = sim.particles[8].orbit.e
    clone5OrbitData[i,0] = sim.particles[9].orbit.a
    clone5OrbitData[i,1] = sim.particles[9].orbit.inc
    clone5OrbitData[i,2] = sim.particles[9].orbit.e
    clone6OrbitData[i,0] = sim.particles[10].orbit.a
    clone6OrbitData[i,1] = sim.particles[10].orbit.inc
    clone6OrbitData[i,2] = sim.particles[10].orbit.e
    clone7OrbitData[i,0] = sim.particles[11].orbit.a
    clone7OrbitData[i,1] = sim.particles[11].orbit.inc
    clone7OrbitData[i,2] = sim.particles[11].orbit.e
    clone8OrbitData[i,0] = sim.particles[12].orbit.a
    clone8OrbitData[i,1] = sim.particles[12].orbit.inc
    clone8OrbitData[i,2] = sim.particles[12].orbit.e
        
    
RR431 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
RR432 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
RR433 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
RR434 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
RR435 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
RR436 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
RR437 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
RR438 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    RR431[i,0] = clone1X[i]
    RR431[i,1] = clone1Y[i]
    RR431[i,2] = clone1Z[i]
    RR431[i,3] = clone1OrbitData[i,0]
    RR431[i,4] = clone1OrbitData[i,1]
    RR431[i,5] = clone1OrbitData[i,2]
    RR432[i,0] = clone2X[i]
    RR432[i,1] = clone2Y[i]
    RR432[i,2] = clone2Z[i]
    RR432[i,3] = clone2OrbitData[i,0]
    RR432[i,4] = clone2OrbitData[i,1]
    RR432[i,5] = clone2OrbitData[i,2]
    RR433[i,0] = clone3X[i]
    RR433[i,1] = clone3Y[i]
    RR433[i,2] = clone3Z[i]
    RR433[i,3] = clone3OrbitData[i,0]
    RR433[i,4] = clone3OrbitData[i,1]
    RR433[i,5] = clone3OrbitData[i,2]
    RR434[i,0] = clone4X[i]
    RR434[i,1] = clone4Y[i]
    RR434[i,2] = clone4Z[i]
    RR434[i,3] = clone4OrbitData[i,0]
    RR434[i,4] = clone4OrbitData[i,1]
    RR434[i,5] = clone4OrbitData[i,2]
    RR435[i,0] = clone5X[i]
    RR435[i,1] = clone5Y[i]
    RR435[i,2] = clone5Z[i]
    RR435[i,3] = clone5OrbitData[i,0]
    RR435[i,4] = clone5OrbitData[i,1]
    RR435[i,5] = clone5OrbitData[i,2]
    RR436[i,0] = clone6X[i]
    RR436[i,1] = clone6Y[i]
    RR436[i,2] = clone6Z[i]
    RR436[i,3] = clone6OrbitData[i,0]
    RR436[i,4] = clone6OrbitData[i,1]
    RR436[i,5] = clone6OrbitData[i,2]
    RR437[i,0] = clone7X[i]
    RR437[i,1] = clone7Y[i]
    RR437[i,2] = clone7Z[i]
    RR437[i,3] = clone7OrbitData[i,0]
    RR437[i,4] = clone7OrbitData[i,1]
    RR437[i,5] = clone7OrbitData[i,2]
    RR438[i,0] = clone8X[i]
    RR438[i,1] = clone8Y[i]
    RR438[i,2] = clone8Z[i]
    RR438[i,3] = clone8OrbitData[i,0]
    RR438[i,4] = clone8OrbitData[i,1]
    RR438[i,5] = clone8OrbitData[i,2]

    
np.savetxt("RR431.csv", RR431, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('RR431.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR431.csv', index=False) 

np.savetxt("RR432.csv", RR432, delimiter=",")
df = pd.read_csv('RR432.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR432.csv', index=False)

np.savetxt("RR433.csv", RR433, delimiter=",")
df = pd.read_csv('RR433.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR433.csv', index=False)
    
np.savetxt("RR434.csv", RR434, delimiter=",")
df = pd.read_csv('RR434.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR434.csv', index=False)
    
np.savetxt("RR435.csv", RR435, delimiter=",")
df = pd.read_csv('RR435.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR435.csv', index=False)
    
np.savetxt("RR436.csv", RR436, delimiter=",")
df = pd.read_csv('RR436.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR436.csv', index=False)
    
np.savetxt("RR437.csv", RR437, delimiter=",")
df = pd.read_csv('RR437.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR437.csv', index=False)
    
np.savetxt("RR438.csv", RR438, delimiter=",")
df = pd.read_csv('RR438.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('RR438.csv', index=False)

np.savetxt("jupiterXYZRR43.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZRR43.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZRR43.csv', index=False)

np.savetxt("saturnXYZRR43.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZRR43.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZRR43.csv', index=False)

np.savetxt("uranusXYZRR43.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZRR43.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZRR43.csv', index=False)

np.savetxt("neptuneXYZRR43.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZRR43.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZRR43.csv', index=False)

print("Finished")

