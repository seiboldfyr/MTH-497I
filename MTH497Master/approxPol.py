# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:27:07 2020

@author: hecto
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def approxP(location):
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