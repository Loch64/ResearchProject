#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#HZ199
lowerValueXHZ199 = -3.466465160206073E+01 - 1.77833600E-04
upperValueXHZ199 = -3.466465160206073E+01 + 1.77833600E-04
lowerValueYHZ199 = -1.226486461031242E+01 - 8.34622860E-05
upperValueYHZ199 = -1.226486461031242E+01 + 8.34622860E-05
lowerValueZHZ199 = 1.186334926922240E+01 - 6.03320937E-05
upperValueZHZ199 = 1.186334926922240E+01 + 6.03320937E-05
lowerValueVXHZ199 = 2.816099782438075E-04 - 1.73213119E-08
upperValueVXHZ199 = 2.816099782438075E-04 + 1.73213119E-08
lowerValueVYHZ199 = -2.747919258311651E-03 - 1.39138072E-08
upperValueVYHZ199 = -2.747919258311651E-03 + 1.39138072E-08
lowerValueVZHZ199 = -9.150858143095169E-04 - 7.69852750E-09
upperValueVZHZ199 = -9.150858143095169E-04 + 7.69852750E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

HZ199XRange = np.linspace(lowerValueXHZ199, upperValueXHZ199, nClones)
HZ199YRange = np.linspace(lowerValueYHZ199, upperValueYHZ199, nClones)
HZ199ZRange = np.linspace(lowerValueZHZ199, upperValueZHZ199, nClones)
HZ199VX = (2.816099782438075E-04)*365.25      #velocity in au/year
HZ199VY = (-2.747919258311651E-03)*365.25
HZ199VZ = (-9.150858143095169E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=HZ199XRange[i], y=HZ199YRange[i], z=HZ199ZRange[i], vx=HZ199VX, vy=HZ199VY, vz=HZ199VZ)
    
#sim.save("solarSystemHZ199.bin")

sim = rebound.Simulation("solarSystemHZ199.bin") #The saved file has the corrected units as shown above
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
        
    
HZ1991 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
HZ1992 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
HZ1993 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
HZ1994 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
HZ1995 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
HZ1996 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
HZ1997 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
HZ1998 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    HZ1991[i,0] = clone1X[i]
    HZ1991[i,1] = clone1Y[i]
    HZ1991[i,2] = clone1Z[i]
    HZ1991[i,3] = clone1OrbitData[i,0]
    HZ1991[i,4] = clone1OrbitData[i,1]
    HZ1991[i,5] = clone1OrbitData[i,2]
    HZ1992[i,0] = clone2X[i]
    HZ1992[i,1] = clone2Y[i]
    HZ1992[i,2] = clone2Z[i]
    HZ1992[i,3] = clone2OrbitData[i,0]
    HZ1992[i,4] = clone2OrbitData[i,1]
    HZ1992[i,5] = clone2OrbitData[i,2]
    HZ1993[i,0] = clone3X[i]
    HZ1993[i,1] = clone3Y[i]
    HZ1993[i,2] = clone3Z[i]
    HZ1993[i,3] = clone3OrbitData[i,0]
    HZ1993[i,4] = clone3OrbitData[i,1]
    HZ1993[i,5] = clone3OrbitData[i,2]
    HZ1994[i,0] = clone4X[i]
    HZ1994[i,1] = clone4Y[i]
    HZ1994[i,2] = clone4Z[i]
    HZ1994[i,3] = clone4OrbitData[i,0]
    HZ1994[i,4] = clone4OrbitData[i,1]
    HZ1994[i,5] = clone4OrbitData[i,2]
    HZ1995[i,0] = clone5X[i]
    HZ1995[i,1] = clone5Y[i]
    HZ1995[i,2] = clone5Z[i]
    HZ1995[i,3] = clone5OrbitData[i,0]
    HZ1995[i,4] = clone5OrbitData[i,1]
    HZ1995[i,5] = clone5OrbitData[i,2]
    HZ1996[i,0] = clone6X[i]
    HZ1996[i,1] = clone6Y[i]
    HZ1996[i,2] = clone6Z[i]
    HZ1996[i,3] = clone6OrbitData[i,0]
    HZ1996[i,4] = clone6OrbitData[i,1]
    HZ1996[i,5] = clone6OrbitData[i,2]
    HZ1997[i,0] = clone7X[i]
    HZ1997[i,1] = clone7Y[i]
    HZ1997[i,2] = clone7Z[i]
    HZ1997[i,3] = clone7OrbitData[i,0]
    HZ1997[i,4] = clone7OrbitData[i,1]
    HZ1997[i,5] = clone7OrbitData[i,2]
    HZ1998[i,0] = clone8X[i]
    HZ1998[i,1] = clone8Y[i]
    HZ1998[i,2] = clone8Z[i]
    HZ1998[i,3] = clone8OrbitData[i,0]
    HZ1998[i,4] = clone8OrbitData[i,1]
    HZ1998[i,5] = clone8OrbitData[i,2]

    
np.savetxt("HZ1991.csv", HZ1991, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('HZ1991.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1991.csv', index=False) 

np.savetxt("HZ1992.csv", HZ1992, delimiter=",")
df = pd.read_csv('HZ1992.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1992.csv', index=False)

np.savetxt("HZ1993.csv", HZ1993, delimiter=",")
df = pd.read_csv('HZ1993.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1993.csv', index=False)
    
np.savetxt("HZ1994.csv", HZ1994, delimiter=",")
df = pd.read_csv('HZ1994.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1994.csv', index=False)
    
np.savetxt("HZ1995.csv", HZ1995, delimiter=",")
df = pd.read_csv('HZ1995.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1995.csv', index=False)
    
np.savetxt("HZ1996.csv", HZ1996, delimiter=",")
df = pd.read_csv('HZ1996.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1996.csv', index=False)
    
np.savetxt("HZ1997.csv", HZ1997, delimiter=",")
df = pd.read_csv('HZ1997.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1997.csv', index=False)
    
np.savetxt("HZ1998.csv", HZ1998, delimiter=",")
df = pd.read_csv('HZ1998.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('HZ1998.csv', index=False)

np.savetxt("jupiterXYZHZ199.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZHZ199.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZHZ199.csv', index=False)

np.savetxt("saturnXYZHZ199.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZHZ199.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZHZ199.csv', index=False)

np.savetxt("uranusXYZHZ199.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZHZ199.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZHZ199.csv', index=False)

np.savetxt("neptuneXYZHZ199.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZHZ199.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZHZ199.csv', index=False)

print("Finished")

