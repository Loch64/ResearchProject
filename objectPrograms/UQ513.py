#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#UQ513
lowerValueXUQ513 = 4.552155346827396E+01 - 2.62113232E-04
upperValueXUQ513 = 4.552155346827396E+01 + 2.62113232E-04
lowerValueYUQ513 = 3.804499392354625E+00 - 5.37926566E-05
upperValueYUQ513 = 3.804499392354625E+00 + 5.37926566E-05
lowerValueZUQ513 = 1.845627417177453E+01 - 1.17256757E-04
upperValueZUQ513 = 1.845627417177453E+01 + 1.17256757E-04
lowerValueVXUQ513 = -4.961371143332699E-04 - 2.81842246E-08
upperValueVXUQ513 = -4.961371143332699E-04 + 2.81842246E-08
lowerValueVYUQ513 = 2.176783849792099E-03 - 9.06981418E-09
upperValueVYUQ513 = 2.176783849792099E-03 + 9.06981418E-09
lowerValueVZUQ513 = 4.529460505296327E-04 - 1.25250324E-08
upperValueVZUQ513 = 4.529460505296327E-04 + 1.25250324E-08

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

UQ513XRange = np.linspace(lowerValueXUQ513, upperValueXUQ513, nClones)
UQ513YRange = np.linspace(lowerValueYUQ513, upperValueYUQ513, nClones)
UQ513ZRange = np.linspace(lowerValueZUQ513, upperValueZUQ513, nClones)
UQ513VX = (-4.961371143332699E-04)*365.25      #velocity in au/year
UQ513VY = (2.176783849792099E-03)*365.25
UQ513VZ = (4.529460505296327E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=UQ513XRange[i], y=UQ513YRange[i], z=UQ513ZRange[i], vx=UQ513VX, vy=UQ513VY, vz=UQ513VZ)
    
#sim.save("solarSystemUQ513.bin")

sim = rebound.Simulation("solarSystemUQ513.bin") #The saved file has the corrected units as shown above
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
        
    
UQ5131 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UQ5132 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UQ5133 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UQ5134 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UQ5135 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UQ5136 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UQ5137 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
UQ5138 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    UQ5131[i,0] = clone1X[i]
    UQ5131[i,1] = clone1Y[i]
    UQ5131[i,2] = clone1Z[i]
    UQ5131[i,3] = clone1OrbitData[i,0]
    UQ5131[i,4] = clone1OrbitData[i,1]
    UQ5131[i,5] = clone1OrbitData[i,2]
    UQ5132[i,0] = clone2X[i]
    UQ5132[i,1] = clone2Y[i]
    UQ5132[i,2] = clone2Z[i]
    UQ5132[i,3] = clone2OrbitData[i,0]
    UQ5132[i,4] = clone2OrbitData[i,1]
    UQ5132[i,5] = clone2OrbitData[i,2]
    UQ5133[i,0] = clone3X[i]
    UQ5133[i,1] = clone3Y[i]
    UQ5133[i,2] = clone3Z[i]
    UQ5133[i,3] = clone3OrbitData[i,0]
    UQ5133[i,4] = clone3OrbitData[i,1]
    UQ5133[i,5] = clone3OrbitData[i,2]
    UQ5134[i,0] = clone4X[i]
    UQ5134[i,1] = clone4Y[i]
    UQ5134[i,2] = clone4Z[i]
    UQ5134[i,3] = clone4OrbitData[i,0]
    UQ5134[i,4] = clone4OrbitData[i,1]
    UQ5134[i,5] = clone4OrbitData[i,2]
    UQ5135[i,0] = clone5X[i]
    UQ5135[i,1] = clone5Y[i]
    UQ5135[i,2] = clone5Z[i]
    UQ5135[i,3] = clone5OrbitData[i,0]
    UQ5135[i,4] = clone5OrbitData[i,1]
    UQ5135[i,5] = clone5OrbitData[i,2]
    UQ5136[i,0] = clone6X[i]
    UQ5136[i,1] = clone6Y[i]
    UQ5136[i,2] = clone6Z[i]
    UQ5136[i,3] = clone6OrbitData[i,0]
    UQ5136[i,4] = clone6OrbitData[i,1]
    UQ5136[i,5] = clone6OrbitData[i,2]
    UQ5137[i,0] = clone7X[i]
    UQ5137[i,1] = clone7Y[i]
    UQ5137[i,2] = clone7Z[i]
    UQ5137[i,3] = clone7OrbitData[i,0]
    UQ5137[i,4] = clone7OrbitData[i,1]
    UQ5137[i,5] = clone7OrbitData[i,2]
    UQ5138[i,0] = clone8X[i]
    UQ5138[i,1] = clone8Y[i]
    UQ5138[i,2] = clone8Z[i]
    UQ5138[i,3] = clone8OrbitData[i,0]
    UQ5138[i,4] = clone8OrbitData[i,1]
    UQ5138[i,5] = clone8OrbitData[i,2]

    
np.savetxt("UQ5131.csv", UQ5131, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('UQ5131.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5131.csv', index=False) 

np.savetxt("UQ5132.csv", UQ5132, delimiter=",")
df = pd.read_csv('UQ5132.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5132.csv', index=False)

np.savetxt("UQ5133.csv", UQ5133, delimiter=",")
df = pd.read_csv('UQ5133.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5133.csv', index=False)
    
np.savetxt("UQ5134.csv", UQ5134, delimiter=",")
df = pd.read_csv('UQ5134.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5134.csv', index=False)
    
np.savetxt("UQ5135.csv", UQ5135, delimiter=",")
df = pd.read_csv('UQ5135.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5135.csv', index=False)
    
np.savetxt("UQ5136.csv", UQ5136, delimiter=",")
df = pd.read_csv('UQ5136.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5136.csv', index=False)
    
np.savetxt("UQ5137.csv", UQ5137, delimiter=",")
df = pd.read_csv('UQ5137.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5137.csv', index=False)
    
np.savetxt("UQ5138.csv", UQ5138, delimiter=",")
df = pd.read_csv('UQ5138.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('UQ5138.csv', index=False)

np.savetxt("jupiterXYZUQ513.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZUQ513.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZUQ513.csv', index=False)

np.savetxt("saturnXYZUQ513.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZUQ513.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZUQ513.csv', index=False)

np.savetxt("uranusXYZUQ513.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZUQ513.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZUQ513.csv', index=False)

np.savetxt("neptuneXYZUQ513.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZUQ513.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZUQ513.csv', index=False)

print("Finished")

