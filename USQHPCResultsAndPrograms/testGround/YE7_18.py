#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#YE7
lowerValueXYE7 = 3.071750192391258E+01 - 3.35281277E-04
upperValueXYE7 = 3.071750192391258E+01 + 3.35281277E-04
lowerValueYYE7 = 3.163881649039393E+01 - 4.78783233E-04
upperValueYYE7 = 3.163881649039393E+01 + 4.78783233E-04
lowerValueZYE7 = -2.441278783919285E+01 - 3.27836588E-04
upperValueZYE7 = -2.441278783919285E+01 + 3.27836588E-04
lowerValueVXYE7 = -1.589925734099267E-03 - 4.35590893E-08
upperValueVXYE7 = -1.589925734099267E-03 + 4.35590893E-08
lowerValueVYYE7 = 1.589183581973211E-03 - 6.70023869E-08
upperValueVYYE7 = 1.589183581973211E-03 + 6.70023869E-08
lowerValueVZYE7 = -1.427169341510712E-04 - 4.38171079E-08
upperValueVZYE7 = -1.427169341510712E-04 + 4.38171079E-08

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

YE7XRange = np.linspace(lowerValueXYE7, upperValueXYE7, nClones)
YE7YRange = np.linspace(lowerValueYYE7, upperValueYYE7, nClones)
YE7ZRange = np.linspace(lowerValueZYE7, upperValueZYE7, nClones)
YE7VX = (-1.589925734099267E-03)*365.25      #velocity in au/year
YE7VY = (1.589183581973211E-03)*365.25
YE7VZ = (-1.427169341510712E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=YE7XRange[i], y=YE7YRange[i], z=YE7ZRange[i], vx=YE7VX, vy=YE7VY, vz=YE7VZ)
    
#sim.save("solarSystemYE7.bin")

sim = rebound.Simulation("solarSystemYE7.bin") #The saved file has the corrected units as shown above
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
        
    
YE71 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
YE72 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
YE73 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
YE74 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
YE75 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
YE76 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
YE77 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
YE78 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    YE71[i,0] = clone1X[i]
    YE71[i,1] = clone1Y[i]
    YE71[i,2] = clone1Z[i]
    YE71[i,3] = clone1OrbitData[i,0]
    YE71[i,4] = clone1OrbitData[i,1]
    YE71[i,5] = clone1OrbitData[i,2]
    YE72[i,0] = clone2X[i]
    YE72[i,1] = clone2Y[i]
    YE72[i,2] = clone2Z[i]
    YE72[i,3] = clone2OrbitData[i,0]
    YE72[i,4] = clone2OrbitData[i,1]
    YE72[i,5] = clone2OrbitData[i,2]
    YE73[i,0] = clone3X[i]
    YE73[i,1] = clone3Y[i]
    YE73[i,2] = clone3Z[i]
    YE73[i,3] = clone3OrbitData[i,0]
    YE73[i,4] = clone3OrbitData[i,1]
    YE73[i,5] = clone3OrbitData[i,2]
    YE74[i,0] = clone4X[i]
    YE74[i,1] = clone4Y[i]
    YE74[i,2] = clone4Z[i]
    YE74[i,3] = clone4OrbitData[i,0]
    YE74[i,4] = clone4OrbitData[i,1]
    YE74[i,5] = clone4OrbitData[i,2]
    YE75[i,0] = clone5X[i]
    YE75[i,1] = clone5Y[i]
    YE75[i,2] = clone5Z[i]
    YE75[i,3] = clone5OrbitData[i,0]
    YE75[i,4] = clone5OrbitData[i,1]
    YE75[i,5] = clone5OrbitData[i,2]
    YE76[i,0] = clone6X[i]
    YE76[i,1] = clone6Y[i]
    YE76[i,2] = clone6Z[i]
    YE76[i,3] = clone6OrbitData[i,0]
    YE76[i,4] = clone6OrbitData[i,1]
    YE76[i,5] = clone6OrbitData[i,2]
    YE77[i,0] = clone7X[i]
    YE77[i,1] = clone7Y[i]
    YE77[i,2] = clone7Z[i]
    YE77[i,3] = clone7OrbitData[i,0]
    YE77[i,4] = clone7OrbitData[i,1]
    YE77[i,5] = clone7OrbitData[i,2]
    YE78[i,0] = clone8X[i]
    YE78[i,1] = clone8Y[i]
    YE78[i,2] = clone8Z[i]
    YE78[i,3] = clone8OrbitData[i,0]
    YE78[i,4] = clone8OrbitData[i,1]
    YE78[i,5] = clone8OrbitData[i,2]

    
np.savetxt("YE71.csv", YE71, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('YE71.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE71.csv', index=False) 

np.savetxt("YE72.csv", YE72, delimiter=",")
df = pd.read_csv('YE72.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE72.csv', index=False)

np.savetxt("YE73.csv", YE73, delimiter=",")
df = pd.read_csv('YE73.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE73.csv', index=False)
    
np.savetxt("YE74.csv", YE74, delimiter=",")
df = pd.read_csv('YE74.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE74.csv', index=False)
    
np.savetxt("YE75.csv", YE75, delimiter=",")
df = pd.read_csv('YE75.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE75.csv', index=False)
    
np.savetxt("YE76.csv", YE76, delimiter=",")
df = pd.read_csv('YE76.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE76.csv', index=False)
    
np.savetxt("YE77.csv", YE77, delimiter=",")
df = pd.read_csv('YE77.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE77.csv', index=False)
    
np.savetxt("YE78.csv", YE78, delimiter=",")
df = pd.read_csv('YE78.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('YE78.csv', index=False)

np.savetxt("jupiterXYZYE7.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZYE7.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZYE7.csv', index=False)

np.savetxt("saturnXYZYE7.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZYE7.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZYE7.csv', index=False)

np.savetxt("uranusXYZYE7.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZYE7.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZYE7.csv', index=False)

np.savetxt("neptuneXYZYE7.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZYE7.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZYE7.csv', index=False)

print("Finished")

