# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:13:31 2020

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

def section(list):
    #given one specified assay and concentration, plot the mean of that concentration 
    #calculates first derivative
    deriv = np.gradient(list)
    #calculates second derivative
    deriv2 = np.gradient(deriv)  


    startpoint = 0
    endpoint = 0
    for i in range(len(deriv2)-1):
        if (deriv2[i]-deriv2[i+1])<-7:
            #start decreasing
            if startpoint == 0:
                startpoint = i
        if deriv2[i] <= -10 and startpoint != 0 :
            endpoint = i+1
    
    
    phase2 = list[startpoint:endpoint]
    phase1 = list[30:startpoint-6]
    
    
    plt.title('Graph for phase 2')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, list, color = 'red' ) #plot each concentration 
    plt.xlim(startpoint, endpoint)
    plt.ylim(0,.8)
    plt.show()
    
    plt.title('Graph for phase 1')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, list, color = 'red' ) #plot each concentration 
    plt.xlim(30, startpoint-6)
    plt.ylim(0,.05)
    plt.show()
    
    return phase1, phase2



def train(file):
    x=pd.read_excel(location, usecols="B")
    
    g2=pd.read_excel(location, usecols="C:CT")
    nar = g2.to_numpy() #convert g2 to numpy array
    
    #indices of each column for a given concentration
    for con in range (1,9):
        indices = [(con-1)*3+0, (con-1)*3+1, (con-1)*3+2, (con-1)*3+24, (con-1)*3+25, (con-1)*3+26, (con-1)*3+48, 
                   (con-1)*3+49, (con-1)*3+50, (con-1)*3+72, (con-1)*3+73, (con-1)*3+74]
        avglist = np.mean(nar[:, indices], axis = 1)
        avglist = normalize(avglist)
        phase1, phase2 = section(avglist)
        a1[con],b1[con],c1[con],error1[con] = sigmoidtrain(phase1)
        a2[con],b2[con],c2[con],error2[con] = sigmoidtrain(phase2)
        
    
        
        
        