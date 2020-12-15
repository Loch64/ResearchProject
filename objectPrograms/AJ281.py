#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#AJ281
lowerValueXAJ281 = -3.400873020303294E+01 - 5.82596773E-04
upperValueXAJ281 = -3.400873020303294E+01 + 5.82596773E-04
lowerValueYAJ281 = 2.208538874851113E+01 - 2.26246143E-04
upperValueYAJ281 = 2.208538874851113E+01 + 2.26246143E-04
lowerValueZAJ281 = -1.938106939624426E+01 - 3.18599280E-04
upperValueZAJ281 = -1.938106939624426E+01 + 3.18599280E-04
lowerValueVXAJ281 = -9.809557088563661E-04 - 7.77820915E-08
upperValueVXAJ281 = -9.809557088563661E-04 + 7.77820915E-08
lowerValueVYAJ281 = -2.310039740248234E-03 - 3.44511607E-08
upperValueVYAJ281 = -2.310039740248234E-03 + 3.44511607E-08
lowerValueVZAJ281 = -1.979109370719406E-04 - 4.23865706E-08
upperValueVZAJ281 = -1.979109370719406E-04 + 4.23865706E-08

nClones = 8 #Only need to change this value to increase of decrease the amount of clones

AJ281XRange = np.linspace(lowerValueXAJ281, upperValueXAJ281, nClones)
AJ281YRange = np.linspace(lowerValueYAJ281, upperValueYAJ281, nClones)
AJ281ZRange = np.linspace(lowerValueZAJ281, upperValueZAJ281, nClones)
AJ281VX = (-9.809557088563661E-04)*365.25      #velocity in au/year
AJ281VY = (-2.310039740248234E-03)*365.25
AJ281VZ = (-1.979109370719406E-04)*365.25

#sim = rebound.Simulation()
#sim.units = ('yr', 'AU', 'Msun')
#sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], date="2000-01-01 00:00")
#for i in range(nClones):
    #sim.add(x=AJ281XRange[i], y=AJ281YRange[i], z=AJ281ZRange[i], vx=AJ281VX, vy=AJ281VY, vz=AJ281VZ)
    
#sim.save("solarSystemAJ281.bin")

sim = rebound.Simulation("solarSystemAJ281.bin") #The saved file has the corrected units as shown above
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
        
    
AJ2811 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AJ2812 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AJ2813 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AJ2814 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AJ2815 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AJ2816 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AJ2817 = np.zeros(nOutputs*6).reshape(nOutputs, 6)
AJ2818 = np.zeros(nOutputs*6).reshape(nOutputs, 6)

for i in range(nOutputs):
    AJ2811[i,0] = clone1X[i]
    AJ2811[i,1] = clone1Y[i]
    AJ2811[i,2] = clone1Z[i]
    AJ2811[i,3] = clone1OrbitData[i,0]
    AJ2811[i,4] = clone1OrbitData[i,1]
    AJ2811[i,5] = clone1OrbitData[i,2]
    AJ2812[i,0] = clone2X[i]
    AJ2812[i,1] = clone2Y[i]
    AJ2812[i,2] = clone2Z[i]
    AJ2812[i,3] = clone2OrbitData[i,0]
    AJ2812[i,4] = clone2OrbitData[i,1]
    AJ2812[i,5] = clone2OrbitData[i,2]
    AJ2813[i,0] = clone3X[i]
    AJ2813[i,1] = clone3Y[i]
    AJ2813[i,2] = clone3Z[i]
    AJ2813[i,3] = clone3OrbitData[i,0]
    AJ2813[i,4] = clone3OrbitData[i,1]
    AJ2813[i,5] = clone3OrbitData[i,2]
    AJ2814[i,0] = clone4X[i]
    AJ2814[i,1] = clone4Y[i]
    AJ2814[i,2] = clone4Z[i]
    AJ2814[i,3] = clone4OrbitData[i,0]
    AJ2814[i,4] = clone4OrbitData[i,1]
    AJ2814[i,5] = clone4OrbitData[i,2]
    AJ2815[i,0] = clone5X[i]
    AJ2815[i,1] = clone5Y[i]
    AJ2815[i,2] = clone5Z[i]
    AJ2815[i,3] = clone5OrbitData[i,0]
    AJ2815[i,4] = clone5OrbitData[i,1]
    AJ2815[i,5] = clone5OrbitData[i,2]
    AJ2816[i,0] = clone6X[i]
    AJ2816[i,1] = clone6Y[i]
    AJ2816[i,2] = clone6Z[i]
    AJ2816[i,3] = clone6OrbitData[i,0]
    AJ2816[i,4] = clone6OrbitData[i,1]
    AJ2816[i,5] = clone6OrbitData[i,2]
    AJ2817[i,0] = clone7X[i]
    AJ2817[i,1] = clone7Y[i]
    AJ2817[i,2] = clone7Z[i]
    AJ2817[i,3] = clone7OrbitData[i,0]
    AJ2817[i,4] = clone7OrbitData[i,1]
    AJ2817[i,5] = clone7OrbitData[i,2]
    AJ2818[i,0] = clone8X[i]
    AJ2818[i,1] = clone8Y[i]
    AJ2818[i,2] = clone8Z[i]
    AJ2818[i,3] = clone8OrbitData[i,0]
    AJ2818[i,4] = clone8OrbitData[i,1]
    AJ2818[i,5] = clone8OrbitData[i,2]

    
np.savetxt("AJ2811.csv", AJ2811, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('AJ2811.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2811.csv', index=False) 

np.savetxt("AJ2812.csv", AJ2812, delimiter=",")
df = pd.read_csv('AJ2812.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2812.csv', index=False)

np.savetxt("AJ2813.csv", AJ2813, delimiter=",")
df = pd.read_csv('AJ2813.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2813.csv', index=False)
    
np.savetxt("AJ2814.csv", AJ2814, delimiter=",")
df = pd.read_csv('AJ2814.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2814.csv', index=False)
    
np.savetxt("AJ2815.csv", AJ2815, delimiter=",")
df = pd.read_csv('AJ2815.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2815.csv', index=False)
    
np.savetxt("AJ2816.csv", AJ2816, delimiter=",")
df = pd.read_csv('AJ2816.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2816.csv', index=False)
    
np.savetxt("AJ2817.csv", AJ2817, delimiter=",")
df = pd.read_csv('AJ2817.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2817.csv', index=False)
    
np.savetxt("AJ2818.csv", AJ2818, delimiter=",")
df = pd.read_csv('AJ2818.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z', 3: 'a', 4: 'i', 5: 'e'}, inplace=True)
df.to_csv('AJ2818.csv', index=False)

np.savetxt("jupiterXYZAJ281.csv", jupiterXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('jupiterXYZAJ281.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('jupiterXYZAJ281.csv', index=False)

np.savetxt("saturnXYZAJ281.csv", saturnXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('saturnXYZAJ281.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('saturnXYZAJ281.csv', index=False)

np.savetxt("uranusXYZAJ281.csv", uranusXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('uranusXYZAJ281.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('uranusXYZAJ281.csv', index=False)

np.savetxt("neptuneXYZAJ281.csv", neptuneXYZ, delimiter=",") #Currently saving to current directory but path can be changed
df = pd.read_csv('neptuneXYZAJ281.csv', header=None)
df.rename(columns={0: 'x', 1: 'y', 2: 'z'}, inplace=True)
df.to_csv('neptuneXYZAJ281.csv', index=False)

print("Finished")

