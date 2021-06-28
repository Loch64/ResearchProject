#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#VK201
lowerValueXVK201 = 3.529039488482533E+01 - 5.55488607E-04
upperValueXVK201 = 3.529039488482533E+01 + 5.55488607E-04
lowerValueYVK201 = 2.444953451396031E+01 - 5.87716711E-04
upperValueYVK201 = 2.444953451396031E+01 + 5.87716711E-04
lowerValueZVK201 = -2.010933751121756E+01 - 4.24369205E-04
upperValueZVK201 = -2.010933751121756E+01 + 4.24369205E-04
lowerValueVXVK201 = -1.415880389465270E-03 - 7.85261562E-08
upperValueVXVK201 = -1.415880389465270E-03 + 7.85261562E-08
lowerValueVYVK201 = 1.809381747538853E-03 - 8.41714596E-08
upperValueVYVK201 = 1.809381747538853E-03 + 8.41714596E-08
lowerValueVZVK201 = -6.021429424906332E-04 - 5.99876789E-08
upperValueVZVK201 = -6.021429424906332E-04 + 5.99876789E-08

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

VK201XRange = np.linspace(lowerValueXVK201, upperValueXVK201, nClones)
VK201YRange = np.linspace(lowerValueYVK201, upperValueYVK201, nClones)
VK201ZRange = np.linspace(lowerValueZVK201, upperValueZVK201, nClones)
VK201VX = (-1.415880389465270E-03)*365.25      #velocity in au/year
VK201VY = (1.809381747538853E-03)*365.25
VK201VZ = (-6.021429424906332E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=VK201XRange[i], y=VK201YRange[i], z=VK201ZRange[i], vx=VK201VX, vy=VK201VY, vz=VK201VZ)
    
#sim.save("solarSystemVK201.bin")

sim = rebound.Simulation("solarSystemVK201.bin") #The saved file has the corrected units as shown above
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
        
    
VK2011 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
VK2012 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
VK2013 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
VK2014 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
VK2015 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
VK2016 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
VK2017 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
VK2018 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    VK2011[i,0] = clone1X[i]
    VK2011[i,1] = clone1Y[i]
    VK2011[i,2] = clone1Z[i]
    VK2011[i,3] = clone1OrbitData[i,0]
    VK2011[i,4] = clone1OrbitData[i,1]
    VK2011[i,5] = clone1OrbitData[i,2]
    VK2012[i,0] = clone2X[i]
    VK2012[i,1] = clone2Y[i]
    VK2012[i,2] = clone2Z[i]
    VK2012[i,3] = clone2OrbitData[i,0]
    VK2012[i,4] = clone2OrbitData[i,1]
    VK2012[i,5] = clone2OrbitData[i,2]
    VK2013[i,0] = clone3X[i]
    VK2013[i,1] = clone3Y[i]
    VK2013[i,2] = clone3Z[i]
    VK2013[i,3] = clone3OrbitData[i,0]
    VK2013[i,4] = clone3OrbitData[i,1]
    VK2013[i,5] = clone3OrbitData[i,2]
    VK2014[i,0] = clone4X[i]
    VK2014[i,1] = clone4Y[i]
    VK2014[i,2] = clone4Z[i]
    VK2014[i,3] = clone4OrbitData[i,0]
    VK2014[i,4] = clone4OrbitData[i,1]
    VK2014[i,5] = clone4OrbitData[i,2]
    VK2015[i,0] = clone5X[i]
    VK2015[i,1] = clone5Y[i]
    VK2015[i,2] = clone5Z[i]
    VK2015[i,3] = clone5OrbitData[i,0]
    VK2015[i,4] = clone5OrbitData[i,1]
    VK2015[i,5] = clone5OrbitData[i,2]
    VK2016[i,0] = clone6X[i]
    VK2016[i,1] = clone6Y[i]
    VK2016[i,2] = clone6Z[i]
    VK2016[i,3] = clone6OrbitData[i,0]
    VK2016[i,4] = clone6OrbitData[i,1]
    VK2016[i,5] = clone6OrbitData[i,2]
    VK2017[i,0] = clone7X[i]
    VK2017[i,1] = clone7Y[i]
    VK2017[i,2] = clone7Z[i]
    VK2017[i,3] = clone7OrbitData[i,0]
    VK2017[i,4] = clone7OrbitData[i,1]
    VK2017[i,5] = clone7OrbitData[i,2]
    VK2018[i,0] = clone8X[i]
    VK2018[i,1] = clone8Y[i]
    VK2018[i,2] = clone8Z[i]
    VK2018[i,3] = clone8OrbitData[i,0]
    VK2018[i,4] = clone8OrbitData[i,1]
    VK2018[i,5] = clone8OrbitData[i,2]

    
np.savetxt("VK2011.csv", VK2011, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('VK2011.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2011.csv', index=False) 

np.savetxt("VK2012.csv", VK2012, delimiter=",")
df = pd.read_csv('VK2012.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2012.csv', index=False)

np.savetxt("VK2013.csv", VK2013, delimiter=",")
df = pd.read_csv('VK2013.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2013.csv', index=False)
    
np.savetxt("VK2014.csv", VK2014, delimiter=",")
df = pd.read_csv('VK2014.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2014.csv', index=False)
    
np.savetxt("VK2015.csv", VK2015, delimiter=",")
df = pd.read_csv('VK2015.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2015.csv', index=False)
    
np.savetxt("VK2016.csv", VK2016, delimiter=",")
df = pd.read_csv('VK2016.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2016.csv', index=False)
    
np.savetxt("VK2017.csv", VK2017, delimiter=",")
df = pd.read_csv('VK2017.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2017.csv', index=False)
    
np.savetxt("VK2018.csv", VK2018, delimiter=",")
df = pd.read_csv('VK2018.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('VK2018.csv', index=False)

np.savetxt("jupiterXYZVK201.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZVK201.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZVK201.csv', index=False)

np.savetxt("saturnXYZVK201.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZVK201.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZVK201.csv', index=False)

np.savetxt("uranusXYZVK201.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZVK201.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZVK201.csv', index=False)

np.savetxt("neptuneXYZVK201.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZVK201.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZVK201.csv', index=False)

print("Finished")

