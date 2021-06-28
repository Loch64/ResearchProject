#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#OY3
lowerValueXOY3 = 2.138391311777151E+01 - 1.91968330E-04
upperValueXOY3 = 2.138391311777151E+01 + 1.91968330E-04
lowerValueYOY3 = -3.253212057402644E+01 - 2.88519402E-04
upperValueYOY3 = -3.253212057402644E+01 + 2.88519402E-04
lowerValueZOY3 = 4.568665722258198E-01 - 1.78374508E-05
upperValueZOY3 = 4.568665722258198E-01 + 1.78374508E-05
lowerValueVXOY3 = 2.397350769752150E-03 - 1.39608702E-08
upperValueVXOY3 = 2.397350769752150E-03 + 1.39608702E-08
lowerValueVYOY3 = 1.141805391803288E-03 - 2.69827714E-08
upperValueVYOY3 = 1.141805391803288E-03 + 2.69827714E-08
lowerValueVZOY3 = 1.187729454834759E-03 - 8.89684366E-09
upperValueVZOY3 = 1.187729454834759E-03 + 8.89684366E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

OY3XRange = np.linspace(lowerValueXOY3, upperValueXOY3, nClones)
OY3YRange = np.linspace(lowerValueYOY3, upperValueYOY3, nClones)
OY3ZRange = np.linspace(lowerValueZOY3, upperValueZOY3, nClones)
OY3VX = (2.397350769752150E-03)*365.25      #velocity in au/year
OY3VY = (1.141805391803288E-03)*365.25
OY3VZ = (1.187729454834759E-03)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Jupiter", "Saturn", "Uranus", "Neptune"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=OY3XRange[i], y=OY3YRange[i], z=OY3ZRange[i], vx=OY3VX, vy=OY3VY, vz=OY3VZ)
    
#sim.save("solarSystemOY3.bin")

sim = rebound.Simulation("solarSystemOY3.bin") #The saved file has the corrected units as shown above
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
        
    
OY31 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OY32 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OY33 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OY34 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OY35 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OY36 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OY37 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
OY38 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    OY31[i,0] = clone1X[i]
    OY31[i,1] = clone1Y[i]
    OY31[i,2] = clone1Z[i]
    OY31[i,3] = clone1OrbitData[i,0]
    OY31[i,4] = clone1OrbitData[i,1]
    OY31[i,5] = clone1OrbitData[i,2]
    OY32[i,0] = clone2X[i]
    OY32[i,1] = clone2Y[i]
    OY32[i,2] = clone2Z[i]
    OY32[i,3] = clone2OrbitData[i,0]
    OY32[i,4] = clone2OrbitData[i,1]
    OY32[i,5] = clone2OrbitData[i,2]
    OY33[i,0] = clone3X[i]
    OY33[i,1] = clone3Y[i]
    OY33[i,2] = clone3Z[i]
    OY33[i,3] = clone3OrbitData[i,0]
    OY33[i,4] = clone3OrbitData[i,1]
    OY33[i,5] = clone3OrbitData[i,2]
    OY34[i,0] = clone4X[i]
    OY34[i,1] = clone4Y[i]
    OY34[i,2] = clone4Z[i]
    OY34[i,3] = clone4OrbitData[i,0]
    OY34[i,4] = clone4OrbitData[i,1]
    OY34[i,5] = clone4OrbitData[i,2]
    OY35[i,0] = clone5X[i]
    OY35[i,1] = clone5Y[i]
    OY35[i,2] = clone5Z[i]
    OY35[i,3] = clone5OrbitData[i,0]
    OY35[i,4] = clone5OrbitData[i,1]
    OY35[i,5] = clone5OrbitData[i,2]
    OY36[i,0] = clone6X[i]
    OY36[i,1] = clone6Y[i]
    OY36[i,2] = clone6Z[i]
    OY36[i,3] = clone6OrbitData[i,0]
    OY36[i,4] = clone6OrbitData[i,1]
    OY36[i,5] = clone6OrbitData[i,2]
    OY37[i,0] = clone7X[i]
    OY37[i,1] = clone7Y[i]
    OY37[i,2] = clone7Z[i]
    OY37[i,3] = clone7OrbitData[i,0]
    OY37[i,4] = clone7OrbitData[i,1]
    OY37[i,5] = clone7OrbitData[i,2]
    OY38[i,0] = clone8X[i]
    OY38[i,1] = clone8Y[i]
    OY38[i,2] = clone8Z[i]
    OY38[i,3] = clone8OrbitData[i,0]
    OY38[i,4] = clone8OrbitData[i,1]
    OY38[i,5] = clone8OrbitData[i,2]

    
np.savetxt("OY31.csv", OY31, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('OY31.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY31.csv', index=False) 

np.savetxt("OY32.csv", OY32, delimiter=",")
df = pd.read_csv('OY32.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY32.csv', index=False)

np.savetxt("OY33.csv", OY33, delimiter=",")
df = pd.read_csv('OY33.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY33.csv', index=False)
    
np.savetxt("OY34.csv", OY34, delimiter=",")
df = pd.read_csv('OY34.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY34.csv', index=False)
    
np.savetxt("OY35.csv", OY35, delimiter=",")
df = pd.read_csv('OY35.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY35.csv', index=False)
    
np.savetxt("OY36.csv", OY36, delimiter=",")
df = pd.read_csv('OY36.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY36.csv', index=False)
    
np.savetxt("OY37.csv", OY37, delimiter=",")
df = pd.read_csv('OY37.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY37.csv', index=False)
    
np.savetxt("OY38.csv", OY38, delimiter=",")
df = pd.read_csv('OY38.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('OY38.csv', index=False)

np.savetxt("jupiterXYZOY3.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZOY3.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZOY3.csv', index=False)

np.savetxt("saturnXYZOY3.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZOY3.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZOY3.csv', index=False)

np.savetxt("uranusXYZOY3.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZOY3.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZOY3.csv', index=False)

np.savetxt("neptuneXYZOY3.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZOY3.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZOY3.csv', index=False)

print("Finished")

