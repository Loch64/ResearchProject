#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#CB79
lowerValueXCB79 = -2.353695340050698E+01 - 1.72296432E-04
upperValueXCB79 = -2.353695340050698E+01 + 1.72296432E-04
lowerValueYCB79 = 3.351466979299675E+01 - 2.04480405E-04
upperValueYCB79 = 3.351466979299675E+01 + 2.04480405E-04
lowerValueZCB79 = 4.747219403437520E+00 - 4.86545608E-05
upperValueZCB79 = 4.747219403437520E+00 + 4.86545608E-05
lowerValueVXCB79 = -1.673577996348516E-03 - 1.93783981E-08
upperValueVXCB79 = -1.673577996348516E-03 + 1.93783981E-08
lowerValueVYCB79 = -1.800362572197515E-03 - 2.47968444E-08
upperValueVYCB79 = -1.800362572197515E-03 + 2.47968444E-08
lowerValueVZCB79 = 1.223481112938538E-03 - 7.70097013E-09
upperValueVZCB79 = 1.223481112938538E-03 + 7.70097013E-09

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

CB79XRange = np.linspace(lowerValueXCB79, upperValueXCB79, nClones)
CB79YRange = np.linspace(lowerValueYCB79, upperValueYCB79, nClones)
CB79ZRange = np.linspace(lowerValueZCB79, upperValueZCB79, nClones)
CB79VX = (4.822841731276640e-04)*365.25      #velocity in au/year
CB79VY = (-2.069938387294513e-03)*365.25
CB79VZ = (3.679397601691202e-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=CB79XRange[i], y=CB79YRange[i], z=CB79ZRange[i], vx=CB79VX, vy=CB79VY, vz=CB79VZ)
    
#sim.save("solarSystemCB79.bin")

sim = rebound.Simulation("solarSystemCB79.bin") #The saved file has the corrected units as shown above
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
        
    
CB791 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
CB792 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
CB793 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
CB794 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
CB795 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
CB796 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
CB797 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
CB798 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    CB791[i,0] = clone1X[i]
    CB791[i,1] = clone1Y[i]
    CB791[i,2] = clone1Z[i]
    CB791[i,3] = clone1OrbitData[i,0]
    CB791[i,4] = clone1OrbitData[i,1]
    CB791[i,5] = clone1OrbitData[i,2]
    CB792[i,0] = clone2X[i]
    CB792[i,1] = clone2Y[i]
    CB792[i,2] = clone2Z[i]
    CB792[i,3] = clone2OrbitData[i,0]
    CB792[i,4] = clone2OrbitData[i,1]
    CB792[i,5] = clone2OrbitData[i,2]
    CB793[i,0] = clone3X[i]
    CB793[i,1] = clone3Y[i]
    CB793[i,2] = clone3Z[i]
    CB793[i,3] = clone3OrbitData[i,0]
    CB793[i,4] = clone3OrbitData[i,1]
    CB793[i,5] = clone3OrbitData[i,2]
    CB794[i,0] = clone4X[i]
    CB794[i,1] = clone4Y[i]
    CB794[i,2] = clone4Z[i]
    CB794[i,3] = clone4OrbitData[i,0]
    CB794[i,4] = clone4OrbitData[i,1]
    CB794[i,5] = clone4OrbitData[i,2]
    CB795[i,0] = clone5X[i]
    CB795[i,1] = clone5Y[i]
    CB795[i,2] = clone5Z[i]
    CB795[i,3] = clone5OrbitData[i,0]
    CB795[i,4] = clone5OrbitData[i,1]
    CB795[i,5] = clone5OrbitData[i,2]
    CB796[i,0] = clone6X[i]
    CB796[i,1] = clone6Y[i]
    CB796[i,2] = clone6Z[i]
    CB796[i,3] = clone6OrbitData[i,0]
    CB796[i,4] = clone6OrbitData[i,1]
    CB796[i,5] = clone6OrbitData[i,2]
    CB797[i,0] = clone7X[i]
    CB797[i,1] = clone7Y[i]
    CB797[i,2] = clone7Z[i]
    CB797[i,3] = clone7OrbitData[i,0]
    CB797[i,4] = clone7OrbitData[i,1]
    CB797[i,5] = clone7OrbitData[i,2]
    CB798[i,0] = clone8X[i]
    CB798[i,1] = clone8Y[i]
    CB798[i,2] = clone8Z[i]
    CB798[i,3] = clone8OrbitData[i,0]
    CB798[i,4] = clone8OrbitData[i,1]
    CB798[i,5] = clone8OrbitData[i,2]

    
np.savetxt("CB791.csv", CB791, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('CB791.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB791.csv', index=False) 

np.savetxt("CB792.csv", CB792, delimiter=",")
df = pd.read_csv('CB792.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB792.csv', index=False)

np.savetxt("CB793.csv", CB793, delimiter=",")
df = pd.read_csv('CB793.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB793.csv', index=False)
    
np.savetxt("CB794.csv", CB794, delimiter=",")
df = pd.read_csv('CB794.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB794.csv', index=False)
    
np.savetxt("CB795.csv", CB795, delimiter=",")
df = pd.read_csv('CB795.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB795.csv', index=False)
    
np.savetxt("CB796.csv", CB796, delimiter=",")
df = pd.read_csv('CB796.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB796.csv', index=False)
    
np.savetxt("CB797.csv", CB797, delimiter=",")
df = pd.read_csv('CB797.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB797.csv', index=False)
    
np.savetxt("CB798.csv", CB798, delimiter=",")
df = pd.read_csv('CB798.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('CB798.csv', index=False)

np.savetxt("jupiterXYZCB79.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZCB79.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZCB79.csv', index=False)

np.savetxt("saturnXYZCB79.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZCB79.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZCB79.csv', index=False)

np.savetxt("uranusXYZCB79.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZCB79.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZCB79.csv', index=False)

np.savetxt("neptuneXYZCB79.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZCB79.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZCB79.csv', index=False)

print("Finished")

