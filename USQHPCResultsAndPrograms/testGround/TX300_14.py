#!/usr/bin/env python
# coding: utf-8

# In[2]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

lowerValueXTX300 = 3.826827197171765E+01 - 7.36819279E-05
upperValueXTX300 = 3.826827197171765E+01 + 7.36819279E-05
lowerValueYTX300 = 4.136717926582796E+00 - 1.83626944E-05
upperValueYTX300 = 4.136717926582796E+00 + 1.83626944E-05
lowerValueZTX300 = 1.238085910103358E+01 - 2.58798505E-05
upperValueZTX300 = 1.238085910103358E+01 + 2.58798505E-05
lowerValueVXTX300 = -2.808583586510024E-04 - 6.29750289E-09
upperValueVXTX300 = -2.808583586510024E-04 + 6.29750289E-09
lowerValueVYTX300 = 2.611581915156017E-03 - 7.96294760E-09
upperValueVYTX300 = 2.611581915156017E-03 + 7.96294760E-09
lowerValueVZTX300 = 9.524354933903657E-04 - 4.38714266E-09
lowerValueVZTX300 = 9.524354933903657E-04 - 4.38714266E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

TX300XRange = np.linspace(lowerValueXTX300, upperValueXTX300, nClones)
TX300YRange = np.linspace(lowerValueYTX300, upperValueYTX300, nClones)
TX300ZRange = np.linspace(lowerValueZTX300, upperValueZTX300, nClones)
TX300VX = (-2.808583586510024E-04)*365.25      #velocity in au/year
TX300VY = (2.611581915156017E-03)*365.25
TX300VZ = (9.524354933903657E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=TX300XRange[i], y=TX300YRange[i], z=TX300ZRange[i], vx=TX300VX, vy=TX300VY, vz=TX300VZ)
    
#sim.save("solarSystemTX300.bin")

sim = rebound.Simulation("solarSystemTX300.bin") #The saved file has the corrected units as shown above
sim.move_to_com() #move to centre of momentum frame. Is it necessary?
sim.integrator = "mercurius"
#Jupiter's sidereal orbit: 11.86 years. dt = 11.86/30 = 0.395333333    From NASA Cosmos
sim.dt = 0.395333333
nOutputs = 180000 #The correct number of outputs over 4.5billion years would be approx 11,382,799,355 (4.5Gyr/dt)
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
        
    
TX3001 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TX3002 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TX3003 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TX3004 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TX3005 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TX3006 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TX3007 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TX3008 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    TX3001[i,0] = clone1X[i]
    TX3001[i,1] = clone1Y[i]
    TX3001[i,2] = clone1Z[i]
    TX3001[i,3] = clone1OrbitData[i,0]
    TX3001[i,4] = clone1OrbitData[i,1]
    TX3001[i,5] = clone1OrbitData[i,2]
    TX3002[i,0] = clone2X[i]
    TX3002[i,1] = clone2Y[i]
    TX3002[i,2] = clone2Z[i]
    TX3002[i,3] = clone2OrbitData[i,0]
    TX3002[i,4] = clone2OrbitData[i,1]
    TX3002[i,5] = clone2OrbitData[i,2]
    TX3003[i,0] = clone3X[i]
    TX3003[i,1] = clone3Y[i]
    TX3003[i,2] = clone3Z[i]
    TX3003[i,3] = clone3OrbitData[i,0]
    TX3003[i,4] = clone3OrbitData[i,1]
    TX3003[i,5] = clone3OrbitData[i,2]
    TX3004[i,0] = clone4X[i]
    TX3004[i,1] = clone4Y[i]
    TX3004[i,2] = clone4Z[i]
    TX3004[i,3] = clone4OrbitData[i,0]
    TX3004[i,4] = clone4OrbitData[i,1]
    TX3004[i,5] = clone4OrbitData[i,2]
    TX3005[i,0] = clone5X[i]
    TX3005[i,1] = clone5Y[i]
    TX3005[i,2] = clone5Z[i]
    TX3005[i,3] = clone5OrbitData[i,0]
    TX3005[i,4] = clone5OrbitData[i,1]
    TX3005[i,5] = clone5OrbitData[i,2]
    TX3006[i,0] = clone6X[i]
    TX3006[i,1] = clone6Y[i]
    TX3006[i,2] = clone6Z[i]
    TX3006[i,3] = clone6OrbitData[i,0]
    TX3006[i,4] = clone6OrbitData[i,1]
    TX3006[i,5] = clone6OrbitData[i,2]
    TX3007[i,0] = clone7X[i]
    TX3007[i,1] = clone7Y[i]
    TX3007[i,2] = clone7Z[i]
    TX3007[i,3] = clone7OrbitData[i,0]
    TX3007[i,4] = clone7OrbitData[i,1]
    TX3007[i,5] = clone7OrbitData[i,2]
    TX3008[i,0] = clone8X[i]
    TX3008[i,1] = clone8Y[i]
    TX3008[i,2] = clone8Z[i]
    TX3008[i,3] = clone8OrbitData[i,0]
    TX3008[i,4] = clone8OrbitData[i,1]
    TX3008[i,5] = clone8OrbitData[i,2]

    
np.savetxt("TX3001.csv", TX3001, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('TX3001.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3001.csv', index=False) 

np.savetxt("TX3002.csv", TX3002, delimiter=",")
df = pd.read_csv('TX3002.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3002.csv', index=False)

np.savetxt("TX3003.csv", TX3003, delimiter=",")
df = pd.read_csv('TX3003.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3003.csv', index=False)
    
np.savetxt("TX3004.csv", TX3004, delimiter=",")
df = pd.read_csv('TX3004.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3004.csv', index=False)
    
np.savetxt("TX3005.csv", TX3005, delimiter=",")
df = pd.read_csv('TX3005.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3005.csv', index=False)
    
np.savetxt("TX3006.csv", TX3006, delimiter=",")
df = pd.read_csv('TX3006.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3006.csv', index=False)
    
np.savetxt("TX3007.csv", TX3007, delimiter=",")
df = pd.read_csv('TX3007.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3007.csv', index=False)
    
np.savetxt("TX3008.csv", TX3008, delimiter=",")
df = pd.read_csv('TX3008.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TX3008.csv', index=False)

np.savetxt("jupiterXYZTX300.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZTX300.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZTX300.csv', index=False)

np.savetxt("saturnXYZTX300.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZTX300.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZTX300.csv', index=False)

np.savetxt("uranusXYZTX300.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZTX300.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZTX300.csv', index=False)

np.savetxt("neptuneXYZTX300.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZTX300.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZTX300.csv', index=False)

print("Finished")

