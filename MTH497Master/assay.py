# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:03:27 2020

@author: hecto
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from phase import phase1


def singleWell(location):
    print('Here are the graphs for - '+location)  
    #reads excel file and plots graphs according to columns
    x=pd.read_excel(location, usecols="B")
    g=pd.read_excel(location, usecols="C")
    #plots single well
    plt.title('Graph for Single Well - '+location)
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x,g)
    plt.show()
    return

def allWells(location):
    #reads columns C throught CT from excel file which is all wells in data
    x=pd.read_excel(location, usecols="B")
    g2=pd.read_excel(location, usecols="C:CT")
    
    plt.title('Graph for all wells - '+location)
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x,g2)
    plt.show()
    return

def groupWells(location):
    x=pd.read_excel(location, usecols="B")
    #seperates y values into the 4 different groups
    y1=pd.read_excel(location, usecols="C:Z")
    y2=pd.read_excel(location, usecols="AA:AX")
    y3=pd.read_excel(location, usecols="AY:BV")
    y4=pd.read_excel(location, usecols="BW:CT")
    
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.title('Graph for 4 groups - '+location)
    plt.plot(x,y1,color='red')#labels groups according to color
    plt.plot(x,y2,color='green')
    plt.plot(x,y3,color='yellow')
    plt.plot(x,y4,color='blue')
    #plt.xlim(0,100)
    #plt.ylim(2000,4000)
    plt.show()
    return
    
def concenWells(location):
    x=pd.read_excel(location, usecols="B")
    g2=pd.read_excel(location, usecols="C:CT")
    nar = g2.to_numpy() #convert g2 to numpy array
    
    #make an array of colors to play with
    colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "teal", "goldenrod"]
    
    plt.title('Graph for 8 concentrations - '+location)
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    for k in range(8):
        #indices of each column for a given concentration
        indices = [k*3+0, k*3+1, k*3+2, k*3+24, k*3+25, k*3+26, k*3+48, 
                   k*3+49, k*3+50, k*3+72, k*3+73, k*3+74]
        plt.plot(x, nar[:, indices], color = colors[k] ) #plot each concentration 
    plt.show()
    return
    
def tripWells(location):
    x=pd.read_excel(location, usecols="B")
    g2=pd.read_excel(location, usecols="C:CT")
    nar = g2.to_numpy()
    #make an empty array of wells
    wells = np.zeros((nar.shape[0], int(nar.shape[1]/3)))
    
    #to graph averaged triplicates as one well
    #start at 0, go to the last column, skip by 3s
    for j in range(0, nar.shape[1], 3):
        triplicate = nar[:, j: j + 3] #get all the rows in a slice of 3 cols
        means = np.mean(triplicate, axis=1) #find the mean of all the rows
        meansupright = np.vstack(means) # shift the horizontal array into vert
        #take our means and stick it in our empty array
        wells[:, int(j/3): int(j/3) + 1] = meansupright 
        
    plt.title('Graph for Triplicates - '+location)
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, wells)
    plt.show()
    
    return