#!/usr/bin/env python
# coding: utf-8

# In[3]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

lowerValueXTO66 = 4.586555571412629E+01 - 4.23119134E-04
upperValueXTO66 = 4.586555571412629E+01 + 4.23119134E-04
lowerValueYTO66 = 1.426396173097061E+00 - 1.87866730E-05
upperValueYTO66 = 1.426396173097061E+00 + 1.87866730E-05
lowerValueZTO66 = 2.720433598355372E+00 - 2.83895699E-05
upperValueZTO66 = 2.720433598355372E+00 + 2.83895699E-05
lowerValueVXTO66 = 1.162655285145088E-04 - 1.91331448E-08
upperValueVXTO66 = 1.162655285145088E-04 + 1.91331448E-08
lowerValueVYTO66 = 2.180083773058136E-03 - 1.90242782E-08
upperValueVYTO66 = 2.180083773058136E-03 + 1.90242782E-08
lowerValueVZTO66 = 1.132336954731640E-03 - 9.76635523E-09
upperValueVZTO66 = 1.132336954731640E-03 + 9.76635523E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

TO66XRange = np.linspace(lowerValueXTO66, upperValueXTO66, nClones)
TO66YRange = np.linspace(lowerValueYTO66, upperValueYTO66, nClones)
TO66ZRange = np.linspace(lowerValueZTO66, upperValueZTO66, nClones)
TO66VX = (1.162655285145088E-04)*365.25      #velocity in au/year
TO66VY = (2.180083773058136E-03)*365.25
TO66VZ = (1.132336954731640E-03)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=TO66XRange[i], y=TO66YRange[i], z=TO66ZRange[i], vx=TO66VX, vy=TO66VY, vz=TO66VZ)
    
#sim.save("solarSystemTO66.bin")

sim = rebound.Simulation("solarSystemTO66.bin") #The saved file has the corrected units as shown above
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
        
    
TO661 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TO662 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TO663 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TO664 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TO665 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TO666 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TO667 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
TO668 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    TO661[i,0] = clone1X[i]
    TO661[i,1] = clone1Y[i]
    TO661[i,2] = clone1Z[i]
    TO661[i,3] = clone1OrbitData[i,0]
    TO661[i,4] = clone1OrbitData[i,1]
    TO661[i,5] = clone1OrbitData[i,2]
    TO662[i,0] = clone2X[i]
    TO662[i,1] = clone2Y[i]
    TO662[i,2] = clone2Z[i]
    TO662[i,3] = clone2OrbitData[i,0]
    TO662[i,4] = clone2OrbitData[i,1]
    TO662[i,5] = clone2OrbitData[i,2]
    TO663[i,0] = clone3X[i]
    TO663[i,1] = clone3Y[i]
    TO663[i,2] = clone3Z[i]
    TO663[i,3] = clone3OrbitData[i,0]
    TO663[i,4] = clone3OrbitData[i,1]
    TO663[i,5] = clone3OrbitData[i,2]
    TO664[i,0] = clone4X[i]
    TO664[i,1] = clone4Y[i]
    TO664[i,2] = clone4Z[i]
    TO664[i,3] = clone4OrbitData[i,0]
    TO664[i,4] = clone4OrbitData[i,1]
    TO664[i,5] = clone4OrbitData[i,2]
    TO665[i,0] = clone5X[i]
    TO665[i,1] = clone5Y[i]
    TO665[i,2] = clone5Z[i]
    TO665[i,3] = clone5OrbitData[i,0]
    TO665[i,4] = clone5OrbitData[i,1]
    TO665[i,5] = clone5OrbitData[i,2]
    TO666[i,0] = clone6X[i]
    TO666[i,1] = clone6Y[i]
    TO666[i,2] = clone6Z[i]
    TO666[i,3] = clone6OrbitData[i,0]
    TO666[i,4] = clone6OrbitData[i,1]
    TO666[i,5] = clone6OrbitData[i,2]
    TO667[i,0] = clone7X[i]
    TO667[i,1] = clone7Y[i]
    TO667[i,2] = clone7Z[i]
    TO667[i,3] = clone7OrbitData[i,0]
    TO667[i,4] = clone7OrbitData[i,1]
    TO667[i,5] = clone7OrbitData[i,2]
    TO668[i,0] = clone8X[i]
    TO668[i,1] = clone8Y[i]
    TO668[i,2] = clone8Z[i]
    TO668[i,3] = clone8OrbitData[i,0]
    TO668[i,4] = clone8OrbitData[i,1]
    TO668[i,5] = clone8OrbitData[i,2]

    
np.savetxt("TO661.csv", TO661, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('TO661.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO661.csv', index=False) 

np.savetxt("TO662.csv", TO662, delimiter=",")
df = pd.read_csv('TO662.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO662.csv', index=False)

np.savetxt("TO663.csv", TO663, delimiter=",")
df = pd.read_csv('TO663.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO663.csv', index=False)
    
np.savetxt("TO664.csv", TO664, delimiter=",")
df = pd.read_csv('TO664.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO664.csv', index=False)
    
np.savetxt("TO665.csv", TO665, delimiter=",")
df = pd.read_csv('TO665.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO665.csv', index=False)
    
np.savetxt("TO666.csv", TO666, delimiter=",")
df = pd.read_csv('TO666.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO666.csv', index=False)
    
np.savetxt("TO667.csv", TO667, delimiter=",")
df = pd.read_csv('TO667.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO667.csv', index=False)
    
np.savetxt("TO668.csv", TO668, delimiter=",")
df = pd.read_csv('TO668.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('TO668.csv', index=False)

np.savetxt("jupiterXYZTO66.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZTO66.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZTO66.csv', index=False)

np.savetxt("saturnXYZTO66.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZTO66.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZTO66.csv', index=False)

np.savetxt("uranusXYZTO66.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZTO66.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZTO66.csv', index=False)

np.savetxt("neptuneXYZTO66.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZTO66.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZTO66.csv', index=False)

print("Finished")

