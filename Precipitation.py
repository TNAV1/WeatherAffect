# Random snow / dust / rain generator
# Todd Nelson  18 Dec 2019
#---------------------------------------------

# Assumes single return, 1st return

import matplotlib.pyplot as plt
import numpy as np 
import random

# Define partile size
# Rain 0.5-5mm Diameter
# Snow
# Hail
# Dust 
# Fog 

ParticleSize = 2 # (mm)


# Define density
# Rain 2/24-30mm/hr
# Snow 0-25.4 mm/hr 
# Hail
# Dust 
# Fog 

ParticleDensity = 25.4 # (mm/hr)
DropStack = ParticleDensity/ParticleSize # (drops/hr)
SheetRate = 60/DropStack  # (min/drop)


# Define fall rate
# Rain 9-13m/s
# Snow 
# Hail
# Dust 0 m/s
# Fog 0 m/s

ParticleRate = 4.7 # (m/s)
SheetDist = ParticleRate * SheetRate * 1000 * 60 # (mm)
NumLayers = SheetDist / ParticleSize

# Define Lidar Volume
# Assume drop dia and 200m long
LidarDist = 200 * 1000 # (mm)

# How many particles to fill the volume
DropFill = LidarDist / ParticleSize
print ("DropFill ",DropFill)

# Ratio of possible to actual layesr population
LayersPerDrop = NumLayers / DropFill

# how fast to create a simulated rain drop
PopRate = SheetRate/NumLayers * LayersPerDrop 

print ("Populate Rate ",PopRate)

plt.ion() # turn interactive plot on
x = (np.arange(128)) # init x
y = (np.arange(128)) # init y
#print (x)
#print (y)
fig = plt.figure() # create a figure
ax = fig.add_subplot(111) # add plot to the figure
line1, = ax.plot(x, y, 'ro') # add a line to the plot

RainDrop = np.full((1,128),200,dtype='int')
#print (RainDrop)
# print (RainDrop[0,1])

for j in range(0,int(NumLayers),1): # loop thru random rain drop locations
    print (j)
    #print (NumLayers)
    for k in range(1,128,1): # step thru each lidar channel
        #print (k)
        GaussLayersPerDrop = random.gauss(LayersPerDrop,1) #gauss distribute the drop timing
        #Need to protect against GaussLayerPerDrop = 0
        # print ("GaussLayersPerDrop ",int(GaussLayersPerDrop))
        rmndr = ((j/int(GaussLayersPerDrop))-int(j/int(GaussLayersPerDrop))) # create var that holds the remainder
        #print (rmndr)
        if rmndr == 0: # if the remainder is zero then put a drop on that layer
            Dropy = random.randrange(DropFill + 1) # create random point along the lidar lenght
            # print (Dropy)
        else:
            Dropy = DropFill # if no rain drop interference return the last point in the lidar return distance
        #print (RainDrop[0,k])
        #print (type(RainDrop[0,k]))
        #print ("Dropy ",Dropy)
        #print (type(Dropy))
        np.put(RainDrop,[0,k],[Dropy])
        #RainDrop[0,k] = [Dropy] 
        #print (RainDrop)
    plt.ylabel('Lidar Return')
    plt.xlabel('Lidar Rain Points')
    plt.axis([0,128,0,DropFill]) # set xaxis 0-2 and yaxis 0-lenght of lidar in drops
    line1.set_ydata(RainDrop) # update y values, 0&2 set at the max, 1 set as random
    fig.canvas.draw()
    fig.canvas.flush_events()

plt.ioff() # turn interactive plot off
plt.show() # needed to keep the plot on the screen


# Define Lidar roof FOV - init random on this surface

# Init volume fill

# propogate falling particles

# Check if each Lidar ray would hit a particle

# Is this before hitting a target then keep otherwise keep target

# replace Lidar return with particle position