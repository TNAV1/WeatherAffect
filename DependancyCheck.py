# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:41:14 2019

@author: Todd Nelson
"""

#Problem: State if 1st file can be loaded based on the available dependancies

import numpy as np
np.set_printoptions(threshold=99)

order=0

# User input of dependancies
Dep = [[0,1],[1,2],[1,3],[2,3],[3,4],[3,5],[3,6],[5,6],[5,6]]
Deprows=len(Dep)
Depcols=len(Dep[0])

# Find the max value to inorder to define the size of the matrix
DepMax = np.amax(Dep)


#init DepOrder
DepOrder = np.zeros(shape=(DepMax+1))
DepOrder = DepOrder - (DepMax+1)

# Initialize the results matrix
DepTracked = np.zeros(shape=(DepMax+1,DepMax+1))
DepTracked = DepTracked -99
Trackrows = len(DepTracked)
Trackcols = len(DepTracked[0])


# Search the dependancies
for x in range(0,Deprows):
    # Specific file
    SF = Dep[x][0]
    # Specific dependancy
    SD = Dep[x][1]
    # Fill in the matrix
    DepTracked[SF][SD]=SD



for y in range(0,Trackrows):
    # Check for self dependancies
    if DepTracked[y,y]!=-99:
        print ("ERROR - file "+ str(y) + " is dependant on itself")




for f in range(0,100):
    # Check for any that can be installed immediately (no dependancies)
    for a in range (Trackrows-1,0-1,-1):
        AlreadyConsidered=0
        for g in range(0,len(DepOrder)):
            if DepOrder[g] == a:
                AlreadyConsidered=1
        
        if AlreadyConsidered == 0:
            count=0
            for b in range (0,Trackcols):
                if DepTracked[a][b] == -99:
                    count=count+1
            
            if count == Trackcols:            
                    DepOrder[order]=a #TODO fix this
                    order=order+1
                
    
    
    # remove the non dependant files from the list to simplify things
    for e in range (0,len(DepOrder)):
        for c in range (0,Trackrows):
            for d in range (0,Trackcols):
                if DepTracked[c][d] == DepOrder[e]:
                    DepTracked[c][d] = -99
                
    

# Check for circular dependancies
CircError=0
for g in range(0,len(DepOrder)):
    if DepOrder[g] == -7:
        CircError=1
if CircError==1:
    print ("ERROR - Circular Reference")
else:
    # find the install order    
    print ("Files can be installed in this order = ")
    print (DepOrder)