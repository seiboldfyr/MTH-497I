# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:17:05 2020

@author: hecto
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from assay import singleWell, allWells, groupWells, concenWells, tripWells

loc1 = "Assay1.xlsx"
loc2 = "Assay2.xlsx"
loc3 = "Assay3.xlsx"
loc4 = "Assay4.xlsx"
loc5 = "Assay5.xlsx"
loc6 = "Assay6.xlsx"
loc7 = "Assay7.xlsx"

def stddev(location, concentration):
    x=pd.read_excel(location, usecols="B")
    
    g2=pd.read_excel(location, usecols="C:CT")
    nar = g2.to_numpy() #convert g2 to numpy array
    con = concentration
    
    #indices of each column for a given concentration
    indices = [(con-1)*3+0, (con-1)*3+1, (con-1)*3+2, (con-1)*3+24, (con-1)*3+25, (con-1)*3+26, (con-1)*3+48, 
                   (con-1)*3+49, (con-1)*3+50, (con-1)*3+72, (con-1)*3+73, (con-1)*3+74]
    
    #given one specified assay and concentration, plot the mean of that concentration 
    means1 = np.mean(nar[:, indices], axis = 1)
    standev = np.std(nar[:, indices], axis = 1)
    means2 = np.array(means1)
    deriv = np.gradient(means2)
    deriv2 = np.gradient(deriv)
    print(deriv)
    x1=np.linspace(0,240,1)
    #print('Mean =',means1)
    plt.title('Graph for Means')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, means1, color = 'red' ) #plot each concentration 
    plt.show()
    plt.title('Graph for Standard Deviation')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, standev, color = 'green' )
    plt.show()
    plt.title('Graph for Derivatives')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, deriv, color = 'blue' ) #plot the derivative 
    plt.show()
    plt.title('Second derivative graph')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, deriv2, color = 'green')
    plt.show()


    startpoint = 0
    endpoint = 0
    decreasing = False
    for i in range(len(deriv2)-1):
        if (deriv2[i]-deriv2[i+1])<-7:
            #start decreasing
            #print(b2[i]-b2[i+1])
            #print(b2[i+1])
            #print(i)
            decreasing = True
            if startpoint == 0:
                startpoint = i
        print(deriv2[i]-deriv2[i+1])        
        print(i)
        if deriv2[i] <= -10 and startpoint != 0 :#(-10<deriv2[i]-deriv2[i+1]<-5 and startpoint != 0) : #decreasing and deriv2[i] < deriv2[i+1]:
            endpoint = i+1
            
        # if (b2[i+1]-b2[i]) < 1 and startpoint == 0:
        #     #look for the first very small difference
        #     startpoint = i
            
    means1 = [item - (np.min(means1) - 0.0000001) for item in means1] #downshift to 0
    means1 = [item/(np.max(means1)-np.min(means1)) for item in means1] #normalize 
    #print(deriv2)
    #print(len(b2))
    #print(len(nar2))
    print(startpoint)
    print(endpoint)
    print(np.where(deriv2 == startpoint))
    print(np.where(deriv2 == endpoint))
    
    plt.title('Graph for phase2')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, means1, color = 'red' ) #plot each concentration 
    plt.xlim(startpoint, endpoint)
    plt.ylim(0,.8)
    plt.show()
    
    plt.title('Graph for phase1')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, means1, color = 'red' ) #plot each concentration 
    plt.xlim(30, startpoint-6)
    plt.ylim(0,.05)
    plt.show()
    
    
    return

stddev(loc1, 4)
