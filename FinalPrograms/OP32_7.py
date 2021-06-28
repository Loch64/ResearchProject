#!/usr/bin/env python
# coding: utf-8

# In[2]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#OP32
lowerValueXOP32 = 2.679137738476953E+01 - 1.49946700E-04
upperValueXOP32 = 2.679137738476953E+01 + 1.49946700E-04
lowerValueYOP32 = -2.679059227039274E+01 - 1.32630398E-04
upperValueYOP32 = -2.679059227039274E+01 + 1.32630398E-04
lowerValueZOP32 = 1.444575111658719E+01 - 7.41698790E-05
upperValueZOP32 = 1.444575111658719E+01 + 7.41698790E-05
lowerValueVXOP32 = 2.240991725789243E-03 - 1.36431440E-08
upperValueVXOP32 = 2.240991725789243E-03 + 1.36431440E-08
lowerValueVYOP32 = 1.494712699578223E-03 - 1.46072028E-08
upperValueVYOP32 = 1.494712699578223E-03 + 1.46072028E-08
lowerValueVZOP32 = -7.053763963260085E-04 - 7.93714997E-09
upperValueVZOP32 = -7.053763963260085E-04 + 7.93714997E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

OP32XRange = np.linspace(lowerValueXOP32, upperValueXOP32, nClones)
OP32YRange = np.linspace(lowerValueYOP32, upperValueYOP32, nClones)
OP32ZRange = np.linspace(lowerValueZOP32, upperValueZOP32, nClones)
OP32VX = (2.240991725789243E-03)*365.25      #velocity in au/year
OP32VY = (1.494712699578223E-03)*365.25
OP32VZ = (-7.053763963260085E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=OP32XRange[i], y=OP32YRange[i], z=OP32ZRange[i], vx=OP32VX, vy=OP32VY, vz=OP32VZ)
    
#sim.save("solarSystemOP32.bin")

sim = rebound.Simulation("solarSystemOP32.bin") #The saved file has the corrected units as shown above
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
        
    
OP321 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OP322 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OP323 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OP324 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OP325 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OP326 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OP327 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OP328 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    OP321[i,0] = clone1X[i]
    OP321[i,1] = clone1Y[i]
    OP321[i,2] = clone1Z[i]
    OP321[i,3] = clone1OrbitData[i,0]
    OP321[i,4] = clone1OrbitData[i,1]
    OP321[i,5] = clone1OrbitData[i,2]
    OP322[i,0] = clone2X[i]
    OP322[i,1] = clone2Y[i]
    OP322[i,2] = clone2Z[i]
    OP322[i,3] = clone2OrbitData[i,0]
    OP322[i,4] = clone2OrbitData[i,1]
    OP322[i,5] = clone2OrbitData[i,2]
    OP323[i,0] = clone3X[i]
    OP323[i,1] = clone3Y[i]
    OP323[i,2] = clone3Z[i]
    OP323[i,3] = clone3OrbitData[i,0]
    OP323[i,4] = clone3OrbitData[i,1]
    OP323[i,5] = clone3OrbitData[i,2]
    OP324[i,0] = clone4X[i]
    OP324[i,1] = clone4Y[i]
    OP324[i,2] = clone4Z[i]
    OP324[i,3] = clone4OrbitData[i,0]
    OP324[i,4] = clone4OrbitData[i,1]
    OP324[i,5] = clone4OrbitData[i,2]
    OP325[i,0] = clone5X[i]
    OP325[i,1] = clone5Y[i]
    OP325[i,2] = clone5Z[i]
    OP325[i,3] = clone5OrbitData[i,0]
    OP325[i,4] = clone5OrbitData[i,1]
    OP325[i,5] = clone5OrbitData[i,2]
    OP326[i,0] = clone6X[i]
    OP326[i,1] = clone6Y[i]
    OP326[i,2] = clone6Z[i]
    OP326[i,3] = clone6OrbitData[i,0]
    OP326[i,4] = clone6OrbitData[i,1]
    OP326[i,5] = clone6OrbitData[i,2]
    OP327[i,0] = clone7X[i]
    OP327[i,1] = clone7Y[i]
    OP327[i,2] = clone7Z[i]
    OP327[i,3] = clone7OrbitData[i,0]
    OP327[i,4] = clone7OrbitData[i,1]
    OP327[i,5] = clone7OrbitData[i,2]
    OP328[i,0] = clone8X[i]
    OP328[i,1] = clone8Y[i]
    OP328[i,2] = clone8Z[i]
    OP328[i,3] = clone8OrbitData[i,0]
    OP328[i,4] = clone8OrbitData[i,1]
    OP328[i,5] = clone8OrbitData[i,2]

    
np.savetxt("OP321.csv", OP321, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('OP321.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP321.csv', index=False) 

np.savetxt("OP322.csv", OP322, delimiter=",")
df = pd.read_csv('OP322.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP322.csv', index=False)

np.savetxt("OP323.csv", OP323, delimiter=",")
df = pd.read_csv('OP323.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP323.csv', index=False)
    
np.savetxt("OP324.csv", OP324, delimiter=",")
df = pd.read_csv('OP324.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP324.csv', index=False)
    
np.savetxt("OP325.csv", OP325, delimiter=",")
df = pd.read_csv('OP325.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP325.csv', index=False)
    
np.savetxt("OP326.csv", OP326, delimiter=",")
df = pd.read_csv('OP326.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP326.csv', index=False)
    
np.savetxt("OP327.csv", OP327, delimiter=",")
df = pd.read_csv('OP327.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP327.csv', index=False)
    
np.savetxt("OP328.csv", OP328, delimiter=",")
df = pd.read_csv('OP328.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OP328.csv', index=False)

np.savetxt("jupiterXYZOP32.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZOP32.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZOP32.csv', index=False)

np.savetxt("saturnXYZOP32.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZOP32.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZOP32.csv', index=False)

np.savetxt("uranusXYZOP32.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZOP32.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZOP32.csv', index=False)

np.savetxt("neptuneXYZOP32.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZOP32.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZOP32.csv', index=False)

print("Finished")

