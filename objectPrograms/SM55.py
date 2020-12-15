#!/usr/bin/env python
# coding: utf-8

# In[2]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

lowerValueXSM55 = 3.466754213760977e+01 - 1.97088657e-04
upperValueXSM55 = 3.466754213760977e+01 + 1.97088657e-04
lowerValueYSM55 = 1.869478787002355e+01 - 1.07304518e-04
upperValueYSM55 = 1.869478787002355e+01 + 1.07304518e-04
lowerValueZSM55 = 2.554807387315789e+00 - 1.84447131e-05
upperValueZSM55 = 2.554807387315789e+00 - 1.84447131e-05
lowerValueVXSM55 = -1.479018053114583e-03 - 1.78387597e-08
upperValueVXSM55 = -1.479018053114583e-03 + 1.78387597e-08
lowerValueVYSM55 = 2.045881424967931e-03 - 8.68093816e-09
upperValueVYSM55 = 2.045881424967931e-03 + 8.68093816e-09
lowerValueVZSM55 = 1.245851657551014E-03 - 6.46399164E-09
lowerValueVZSM55 = 1.245851657551014E-03 + 6.46399164E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

SM55XRange = np.linspace(lowerValueXSM55, upperValueXSM55, nClones)
SM55YRange = np.linspace(lowerValueYSM55, upperValueYSM55, nClones)
SM55ZRange = np.linspace(lowerValueZSM55, upperValueZSM55, nClones)
SM55VX = (-1.479018053114583e-03)*365.25      #velocity in au/year
SM55VY = (2.045881424967931e-03)*365.25
SM55VZ = (1.245851657551014E-03)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=SM55XRange[i], y=SM55YRange[i], z=SM55ZRange[i], vx=SM55VX, vy=SM55VY, vz=SM55VZ)
    
#sim.save("solarSystemSM55.bin")

sim = rebound.Simulation("solarSystemSM55.bin") #The saved file has the corrected units as shown above
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
        
    
SM551 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SM552 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SM553 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SM554 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SM555 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SM556 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SM557 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
SM558 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    SM551[i,0] = clone1X[i]
    SM551[i,1] = clone1Y[i]
    SM551[i,2] = clone1Z[i]
    SM551[i,3] = clone1OrbitData[i,0]
    SM551[i,4] = clone1OrbitData[i,1]
    SM551[i,5] = clone1OrbitData[i,2]
    SM552[i,0] = clone2X[i]
    SM552[i,1] = clone2Y[i]
    SM552[i,2] = clone2Z[i]
    SM552[i,3] = clone2OrbitData[i,0]
    SM552[i,4] = clone2OrbitData[i,1]
    SM552[i,5] = clone2OrbitData[i,2]
    SM553[i,0] = clone3X[i]
    SM553[i,1] = clone3Y[i]
    SM553[i,2] = clone3Z[i]
    SM553[i,3] = clone3OrbitData[i,0]
    SM553[i,4] = clone3OrbitData[i,1]
    SM553[i,5] = clone3OrbitData[i,2]
    SM554[i,0] = clone4X[i]
    SM554[i,1] = clone4Y[i]
    SM554[i,2] = clone4Z[i]
    SM554[i,3] = clone4OrbitData[i,0]
    SM554[i,4] = clone4OrbitData[i,1]
    SM554[i,5] = clone4OrbitData[i,2]
    SM555[i,0] = clone5X[i]
    SM555[i,1] = clone5Y[i]
    SM555[i,2] = clone5Z[i]
    SM555[i,3] = clone5OrbitData[i,0]
    SM555[i,4] = clone5OrbitData[i,1]
    SM555[i,5] = clone5OrbitData[i,2]
    SM556[i,0] = clone6X[i]
    SM556[i,1] = clone6Y[i]
    SM556[i,2] = clone6Z[i]
    SM556[i,3] = clone6OrbitData[i,0]
    SM556[i,4] = clone6OrbitData[i,1]
    SM556[i,5] = clone6OrbitData[i,2]
    SM557[i,0] = clone7X[i]
    SM557[i,1] = clone7Y[i]
    SM557[i,2] = clone7Z[i]
    SM557[i,3] = clone7OrbitData[i,0]
    SM557[i,4] = clone7OrbitData[i,1]
    SM557[i,5] = clone7OrbitData[i,2]
    SM558[i,0] = clone8X[i]
    SM558[i,1] = clone8Y[i]
    SM558[i,2] = clone8Z[i]
    SM558[i,3] = clone8OrbitData[i,0]
    SM558[i,4] = clone8OrbitData[i,1]
    SM558[i,5] = clone8OrbitData[i,2]

    
np.savetxt("SM551.csv", SM551, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('SM551.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM551.csv', index=False) 

np.savetxt("SM552.csv", SM552, delimiter=",")
df = pd.read_csv('SM552.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM552.csv', index=False)

np.savetxt("SM553.csv", SM553, delimiter=",")
df = pd.read_csv('SM553.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM553.csv', index=False)
    
np.savetxt("SM554.csv", SM554, delimiter=",")
df = pd.read_csv('SM554.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM554.csv', index=False)
    
np.savetxt("SM555.csv", SM555, delimiter=",")
df = pd.read_csv('SM555.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM555.csv', index=False)
    
np.savetxt("SM556.csv", SM556, delimiter=",")
df = pd.read_csv('SM556.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM556.csv', index=False)
    
np.savetxt("SM557.csv", SM557, delimiter=",")
df = pd.read_csv('SM557.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM557.csv', index=False)
    
np.savetxt("SM558.csv", SM558, delimiter=",")
df = pd.read_csv('SM558.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('SM558.csv', index=False)

np.savetxt("jupiterXYZSM55.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZSM55.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZSM55.csv', index=False)

np.savetxt("saturnXYZSM55.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZSM55.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZSM55.csv', index=False)

np.savetxt("uranusXYZSM55.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZSM55.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZSM55.csv', index=False)

np.savetxt("neptuneXYZSM55.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZSM55.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZSM55.csv', index=False)

print("Finished")

