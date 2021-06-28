#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#LO28
lowerValueXLO28 = 2.315879353260684E+01 - 2.24801222E-04
upperValueXLO28 = 2.315879353260684E+01 + 2.24801222E-04
lowerValueYLO28 = -3.491588722118052E+01 - 2.46486115E-04
upperValueYLO28 = -3.491588722118052E+01 + 2.46486115E-04
lowerValueZLO28 = 5.647148023034489E+00 - 7.48386379E-05
upperValueZLO28 = 5.647148023034489E+00 + 7.48386379E-05
lowerValueVXLO28 = 1.756111933858958E-03 - 3.27047079E-08
upperValueVXLO28 = 1.756111933858958E-03 + 3.27047079E-08
lowerValueVYLO28 = 1.713654978434355E-03 - 3.08432127E-08
upperValueVYLO28 = 1.713654978434355E-03 + 3.08432127E-08
lowerValueVZLO28 = 1.046607086808728E-03 - 1.26089754E-08
upperValueVZLO28 = 1.046607086808728E-03 + 1.26089754E-08

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

LO28XRange = np.linspace(lowerValueXLO28, upperValueXLO28, nClones)
LO28YRange = np.linspace(lowerValueYLO28, upperValueYLO28, nClones)
LO28ZRange = np.linspace(lowerValueZLO28, upperValueZLO28, nClones)
LO28VX = (1.756111933858958E-03)*365.25      #velocity in au/year
LO28VY = (1.713654978434355E-03)*365.25
LO28VZ = (1.046607086808728E-03)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=LO28XRange[i], y=LO28YRange[i], z=LO28ZRange[i], vx=LO28VX, vy=LO28VY, vz=LO28VZ)
    
#sim.save("solarSystemLO28.bin")

sim = rebound.Simulation("solarSystemLO28.bin") #The saved file has the corrected units as shown above
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
        
    
LO281 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
LO282 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
LO283 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
LO284 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
LO285 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
LO286 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
LO287 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
LO288 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    LO281[i,0] = clone1X[i]
    LO281[i,1] = clone1Y[i]
    LO281[i,2] = clone1Z[i]
    LO281[i,3] = clone1OrbitData[i,0]
    LO281[i,4] = clone1OrbitData[i,1]
    LO281[i,5] = clone1OrbitData[i,2]
    LO282[i,0] = clone2X[i]
    LO282[i,1] = clone2Y[i]
    LO282[i,2] = clone2Z[i]
    LO282[i,3] = clone2OrbitData[i,0]
    LO282[i,4] = clone2OrbitData[i,1]
    LO282[i,5] = clone2OrbitData[i,2]
    LO283[i,0] = clone3X[i]
    LO283[i,1] = clone3Y[i]
    LO283[i,2] = clone3Z[i]
    LO283[i,3] = clone3OrbitData[i,0]
    LO283[i,4] = clone3OrbitData[i,1]
    LO283[i,5] = clone3OrbitData[i,2]
    LO284[i,0] = clone4X[i]
    LO284[i,1] = clone4Y[i]
    LO284[i,2] = clone4Z[i]
    LO284[i,3] = clone4OrbitData[i,0]
    LO284[i,4] = clone4OrbitData[i,1]
    LO284[i,5] = clone4OrbitData[i,2]
    LO285[i,0] = clone5X[i]
    LO285[i,1] = clone5Y[i]
    LO285[i,2] = clone5Z[i]
    LO285[i,3] = clone5OrbitData[i,0]
    LO285[i,4] = clone5OrbitData[i,1]
    LO285[i,5] = clone5OrbitData[i,2]
    LO286[i,0] = clone6X[i]
    LO286[i,1] = clone6Y[i]
    LO286[i,2] = clone6Z[i]
    LO286[i,3] = clone6OrbitData[i,0]
    LO286[i,4] = clone6OrbitData[i,1]
    LO286[i,5] = clone6OrbitData[i,2]
    LO287[i,0] = clone7X[i]
    LO287[i,1] = clone7Y[i]
    LO287[i,2] = clone7Z[i]
    LO287[i,3] = clone7OrbitData[i,0]
    LO287[i,4] = clone7OrbitData[i,1]
    LO287[i,5] = clone7OrbitData[i,2]
    LO288[i,0] = clone8X[i]
    LO288[i,1] = clone8Y[i]
    LO288[i,2] = clone8Z[i]
    LO288[i,3] = clone8OrbitData[i,0]
    LO288[i,4] = clone8OrbitData[i,1]
    LO288[i,5] = clone8OrbitData[i,2]

    
np.savetxt("LO281.csv", LO281, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('LO281.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO281.csv', index=False) 

np.savetxt("LO282.csv", LO282, delimiter=",")
df = pd.read_csv('LO282.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO282.csv', index=False)

np.savetxt("LO283.csv", LO283, delimiter=",")
df = pd.read_csv('LO283.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO283.csv', index=False)
    
np.savetxt("LO284.csv", LO284, delimiter=",")
df = pd.read_csv('LO284.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO284.csv', index=False)
    
np.savetxt("LO285.csv", LO285, delimiter=",")
df = pd.read_csv('LO285.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO285.csv', index=False)
    
np.savetxt("LO286.csv", LO286, delimiter=",")
df = pd.read_csv('LO286.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO286.csv', index=False)
    
np.savetxt("LO287.csv", LO287, delimiter=",")
df = pd.read_csv('LO287.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO287.csv', index=False)
    
np.savetxt("LO288.csv", LO288, delimiter=",")
df = pd.read_csv('LO288.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('LO288.csv', index=False)

np.savetxt("jupiterXYZLO28.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZLO28.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZLO28.csv', index=False)

np.savetxt("saturnXYZLO28.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZLO28.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZLO28.csv', index=False)

np.savetxt("uranusXYZLO28.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZLO28.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZLO28.csv', index=False)

np.savetxt("neptuneXYZLO28.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZLO28.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZLO28.csv', index=False)

print("Finished")

