# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:47:53 2020

@author: hecto
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

loc1 = "Assay1.xlsx"
loc2 = "Assay2.xlsx"
loc3 = "Assay3.xlsx"
loc4 = "Assay4.xlsx"
loc5 = "Assay5.xlsx"
loc6 = "Assay6.xlsx"
loc7 = "Assay7.xlsx"

file = -1 #set file to a random number in order to initialize it

#graphs single well, all wells, and all wells for each group by color
def assay(location):
    print('Here are the graphs for '+file)     
    x=pd.read_excel(location, usecols="B")
    g=pd.read_excel(location, usecols="C")
    
    plt.plot(x,g)
    plt.show()
    
    g2=pd.read_excel(location, usecols="C:CT")
        
    plt.plot(x,g2)
    plt.show()
        
    y1=pd.read_excel(location, usecols="C:Z")
    y2=pd.read_excel(location, usecols="AA:AX")
    y3=pd.read_excel(location, usecols="AY:BV")
    y4=pd.read_excel(location, usecols="BW:CT")
    
    #plt.plot(x,y1,y2,y3,y4)
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x,y1,color='red')
    plt.plot(x,y2,color='green')
    plt.plot(x,y3,color='yellow')
    plt.plot(x,y4,color='blue')
    #plt.xlim(0,100)
    #plt.ylim(2000,4000)
    plt.show()
    
    nar = g2.to_numpy() #convert g2 to numpy array
    
    #make an array of colors to play with
    colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "teal", "goldenrod"]
    
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    for k in range(8):
        #indices of each column for a given concentration
        indices = [k*3+0, k*3+1, k*3+2, k*3+24, k*3+25, k*3+26, k*3+48, k*3+49, k*3+50, k*3+72, k*3+73, k*3+74]
        plt.plot(x, nar[:, indices], color = colors[k] ) #plot each concentration 
    plt.show()
    
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
        
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, wells)
    plt.show()
    
    print('---------------------------------------------------------------')
    
    
    
    return


while file != 'stop':
    file=str(input("Please enter the Assay you would like to see\n"))

    if(file == 'assay1'):
        assay(loc1)
    
    elif(file == 'assay2'):
        assay(loc2)
        
    elif(file == 'assay3'):
        assay(loc3)
    
    elif(file == 'assay4'):
        assay(loc4)
    
    elif(file == 'assay5'):
        assay(loc5)
    
    elif(file == 'assay6'):
        assay(loc6)
    
    elif(file == 'assay7'):
        assay(loc7)
    else:
        print('Invalid assay. Try again')