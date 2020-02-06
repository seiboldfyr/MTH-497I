# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:15:08 2020

@author: hecto
"""

import pandas as pd
import matplotlib.pyplot as plt

loc1 = "C:/Users/hecto/Downloads/AssayData/Assay1.xlsx"
loc2 = "C:/Users/hecto/Downloads/AssayData/Assay2.xlsx"
loc3 = "C:/Users/hecto/Downloads/AssayData/Assay3.xlsx"
loc4 = "C:/Users/hecto/Downloads/AssayData/Assay4.xlsx"
loc5 = "C:/Users/hecto/Downloads/AssayData/Assay5.xlsx"
loc6 = "C:/Users/hecto/Downloads/AssayData/Assay6.xlsx"
loc7 = "C:/Users/hecto/Downloads/AssayData/Assay7.xlsx"

file = -1 #set file to a random number in order to initialize it

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
    
    
    
    
    
