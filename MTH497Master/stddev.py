# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:19:28 2020

@author: hecto
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    #print('Mean =',means1)
    plt.plot(x, means1, color = 'red' ) #plot each concentration 
    plt.show()
    plt.plot(x, standev, color = 'green' )
    plt.show()
    return