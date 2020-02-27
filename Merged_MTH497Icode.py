# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:47:53 2020

@author: hecto
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#initialize variables according to assay file
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
    #reads excel file and plots graphs according to columns
    x=pd.read_excel(location, usecols="B")
    g=pd.read_excel(location, usecols="C")
    
    #plots single well
    plt.title('Graph for Single Well')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x,g)
    plt.show()
    
    #reads columns C throught CT from excel file which is all wells in data
    g2=pd.read_excel(location, usecols="C:CT")
    
    plt.title('Graph for all wells')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x,g2)
    plt.show()
    
    #seperates y values into the 4 different groups
    y1=pd.read_excel(location, usecols="C:Z")
    y2=pd.read_excel(location, usecols="AA:AX")
    y3=pd.read_excel(location, usecols="AY:BV")
    y4=pd.read_excel(location, usecols="BW:CT")
    
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.title('Graph for 4 groups')
    plt.plot(x,y1,color='red')#labels groups according to color
    plt.plot(x,y2,color='green')
    plt.plot(x,y3,color='yellow')
    plt.plot(x,y4,color='blue')
    #plt.xlim(0,100)
    #plt.ylim(2000,4000)
    plt.show()
    
    nar = g2.to_numpy() #convert g2 to numpy array
    
    #make an array of colors to play with
    colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "teal", "goldenrod"]
    
    plt.title('Graph for 8 concentrations')
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
        
    plt.title('Graph for Triplicates')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x, wells)
    plt.show()
    
    print('---------------------------------------------------------------')
    return

##build some regression lines
def approx(location):
    x=pd.read_excel(location, usecols= "B")
    ##take our boring pandas array and make it a numpy array, then kick out the extra dimension
    x1 = np.reshape(np.array(x), -1) 
    g=pd.read_excel(location, usecols="C")
    ##take our boring pandas array and make it a numpy array, then kick out the extra dimension
    g2 = np.reshape(np.array(g), -1)
    print(x1.shape)
    print(g2.shape)
    regline= np.poly1d(np.polyfit(x1,g2,5))##we have a regression line! 
    ##its not very good tho
    myline = np.linspace(1,251)
    
    plt.plot(x,g)##actual graph
    plt.plot(myline, regline(myline))##regression line 
    plt.show()
    return
approx(loc1)

#will always ask for input unless user types 'stop'
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
    elif(file == 'all'):
        print('ASSAY 1')
        assay(loc1)
        print('ASSAY 2')
        assay(loc2)
        print('ASSAY 3')
        assay(loc3)
        print('ASSAY 4')
        assay(loc4)
        print('ASSAY 5')
        assay(loc5)
        print('ASSAY 6')
        assay(loc6)
        print('ASSAY 7')
        assay(loc7)
    else:
        print('Invalid assay. Try again')