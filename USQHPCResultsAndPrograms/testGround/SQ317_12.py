#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#SQ317
lowerValueXSQ317 = 3.878244728675305E+01 - 5.67633573E-04
upperValueXSQ317 = 3.878244728675305E+01 + 5.67633573E-04
lowerValueYSQ317 = -6.667158452011587E+00 - 8.30734653E-05
upperValueYSQ317 = -6.667158452011587E+00 + 8.30734653E-05
lowerValueZSQ317 = 2.262374059177815E+00 - 4.02579391E-05
upperValueZSQ317 = 2.262374059177815E+00 + 4.02579391E-05
lowerValueVXSQ317 = 4.296326778907280E-04 - 5.51461223E-08
upperValueVXSQ317 = 4.296326778907280E-04 + 5.51461223E-08
lowerValueVYSQ317 = 2.463955501440543E-03 - 2.86817575E-08
upperValueVYSQ317 = 2.463955501440543E-03 + 2.86817575E-08
lowerValueVZSQ317 = -1.353793728190497E-03 - 1.50321558E-08
upperValueVZSQ317 = -1.353793728190497E-03 + 1.50321558E-08

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

SQ317XRange = np.linspace(lowerValueXSQ317, upperValueXSQ317, nClones)
SQ317YRange = np.linspace(lowerValueYSQ317, upperValueYSQ317, nClones)
SQ317ZRange = np.linspace(lowerValueZSQ317, upperValueZSQ317, nClones)
SQ317VX = (4.296326778907280E-04)*365.25      #velocity in au/year
SQ317VY = (2.463955501440543E-03)*365.25
SQ317VZ = (-1.353793728190497E-03)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=SQ317XRange[i], y=SQ317YRange[i], z=SQ317ZRange[i], vx=SQ317VX, vy=SQ317VY, vz=SQ317VZ)
    
#sim.save("solarSystemSQ317.bin")

sim = rebound.Simulation("solarSystemSQ317.bin") #The saved file has the corrected units as shown above
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
        
    
SQ3171 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SQ3172 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SQ3173 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SQ3174 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SQ3175 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SQ3176 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SQ3177 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SQ3178 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    SQ3171[i,0] = clone1X[i]
    SQ3171[i,1] = clone1Y[i]
    SQ3171[i,2] = clone1Z[i]
    SQ3171[i,3] = clone1OrbitData[i,0]
    SQ3171[i,4] = clone1OrbitData[i,1]
    SQ3171[i,5] = clone1OrbitData[i,2]
    SQ3172[i,0] = clone2X[i]
    SQ3172[i,1] = clone2Y[i]
    SQ3172[i,2] = clone2Z[i]
    SQ3172[i,3] = clone2OrbitData[i,0]
    SQ3172[i,4] = clone2OrbitData[i,1]
    SQ3172[i,5] = clone2OrbitData[i,2]
    SQ3173[i,0] = clone3X[i]
    SQ3173[i,1] = clone3Y[i]
    SQ3173[i,2] = clone3Z[i]
    SQ3173[i,3] = clone3OrbitData[i,0]
    SQ3173[i,4] = clone3OrbitData[i,1]
    SQ3173[i,5] = clone3OrbitData[i,2]
    SQ3174[i,0] = clone4X[i]
    SQ3174[i,1] = clone4Y[i]
    SQ3174[i,2] = clone4Z[i]
    SQ3174[i,3] = clone4OrbitData[i,0]
    SQ3174[i,4] = clone4OrbitData[i,1]
    SQ3174[i,5] = clone4OrbitData[i,2]
    SQ3175[i,0] = clone5X[i]
    SQ3175[i,1] = clone5Y[i]
    SQ3175[i,2] = clone5Z[i]
    SQ3175[i,3] = clone5OrbitData[i,0]
    SQ3175[i,4] = clone5OrbitData[i,1]
    SQ3175[i,5] = clone5OrbitData[i,2]
    SQ3176[i,0] = clone6X[i]
    SQ3176[i,1] = clone6Y[i]
    SQ3176[i,2] = clone6Z[i]
    SQ3176[i,3] = clone6OrbitData[i,0]
    SQ3176[i,4] = clone6OrbitData[i,1]
    SQ3176[i,5] = clone6OrbitData[i,2]
    SQ3177[i,0] = clone7X[i]
    SQ3177[i,1] = clone7Y[i]
    SQ3177[i,2] = clone7Z[i]
    SQ3177[i,3] = clone7OrbitData[i,0]
    SQ3177[i,4] = clone7OrbitData[i,1]
    SQ3177[i,5] = clone7OrbitData[i,2]
    SQ3178[i,0] = clone8X[i]
    SQ3178[i,1] = clone8Y[i]
    SQ3178[i,2] = clone8Z[i]
    SQ3178[i,3] = clone8OrbitData[i,0]
    SQ3178[i,4] = clone8OrbitData[i,1]
    SQ3178[i,5] = clone8OrbitData[i,2]

    
np.savetxt("SQ3171.csv", SQ3171, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('SQ3171.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3171.csv', index=False) 

np.savetxt("SQ3172.csv", SQ3172, delimiter=",")
df = pd.read_csv('SQ3172.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3172.csv', index=False)

np.savetxt("SQ3173.csv", SQ3173, delimiter=",")
df = pd.read_csv('SQ3173.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3173.csv', index=False)
    
np.savetxt("SQ3174.csv", SQ3174, delimiter=",")
df = pd.read_csv('SQ3174.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3174.csv', index=False)
    
np.savetxt("SQ3175.csv", SQ3175, delimiter=",")
df = pd.read_csv('SQ3175.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3175.csv', index=False)
    
np.savetxt("SQ3176.csv", SQ3176, delimiter=",")
df = pd.read_csv('SQ3176.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3176.csv', index=False)
    
np.savetxt("SQ3177.csv", SQ3177, delimiter=",")
df = pd.read_csv('SQ3177.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3177.csv', index=False)
    
np.savetxt("SQ3178.csv", SQ3178, delimiter=",")
df = pd.read_csv('SQ3178.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SQ3178.csv', index=False)

np.savetxt("jupiterXYZSQ317.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZSQ317.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZSQ317.csv', index=False)

np.savetxt("saturnXYZSQ317.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZSQ317.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZSQ317.csv', index=False)

np.savetxt("uranusXYZSQ317.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZSQ317.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZSQ317.csv', index=False)

np.savetxt("neptuneXYZSQ317.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZSQ317.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZSQ317.csv', index=False)

print("Finished")

