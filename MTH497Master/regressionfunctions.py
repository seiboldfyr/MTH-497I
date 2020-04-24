# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:21:20 2020

@author: Sydney Wells, Hector Ramos Diaz
@collaborator: Claire Seibold
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
def train(x, g2):
    
    nar = g2.to_numpy() #convert g2 to numpy array
    a1 = [0]*8
    a2 = [0]*8
    b1 = [0]*8
    b2 = [0]*8
    c1 = [0]*8
    c2 = [0]*8
    error1 = [0]*8
    error2 = [0]*8
    #indices of each column for a given concentration
    for con in range (8):
        indices = [(con)*3+0, (con)*3+1, (con)*3+2, (con)*3+24, (con)*3+25, (con)*3+26, (con)*3+48, 
                   (con)*3+49, (con)*3+50, (con)*3+72, (con)*3+73, (con)*3+74]
        avginlist = np.mean(nar[:, indices], axis = 1)
        #avginlist = normalize(avginlist)
        phase1, phase2, x1, x2 = section(x, avginlist)
        phase1 = normalize(phase1)
        phase2 = normalize(phase2)
        if len(phase1) == 0 or len(phase2)==0:
            continue
        a1[con],b1[con],c1[con],error1[con] = sigmoidtrain(x1, phase1)
        a2[con],b2[con],c2[con],error2[con] = sigmoidtrain(x2, phase2)
        
def test(x,g2):
    for i in range(1, len(x)):
         inlist = g2(i)
         #inlist = normalize(inlist)
         phase1, phase2 = section(x, inlist)
         phase1 = normalize(phase1)
         phase2 = normalize(phase2)
         sigmoidtest(x, inlist, aexpec, bexpec, cexpec, errorexpec)
         
def section(x, inlist):
    inlist = np.array(inlist)
    #print(inlist)
    #given one specified assay and concentration, plot the mean of that concentration 
    #calculates first derivative
    deriv = np.gradient(inlist)
    #calculates second derivative
    deriv2 = np.gradient(deriv)  


    startpoint = 0
    endpoint = 0
    for i in range(len(deriv2)-1):
        #print('dif')
        #print(deriv2[i]-deriv2[i+1])  
        #print('i',i, deriv2[i],deriv2[i]-deriv2[i+1])
        #print(i)
        #print('deriv2')
        #print(deriv2[i])
        if (deriv2[i]-deriv2[i+1])<-7:
            #start decreasing
            if startpoint == 0:
                startpoint = i
       
        if deriv2[i] <= -10 and startpoint != 0 :
            endpoint = i+1
    if endpoint == 0:
        endpoint = len(inlist)-1
    print(startpoint)
    print(endpoint)
    phase2 = inlist[startpoint:endpoint]
    phase1 = inlist[30:startpoint-6]
    x1 = x[30:startpoint-6]
    x2 = x[startpoint:endpoint]
    #print(phase1)
    #print(phase2)
    
    plt.title('Graph for phase 2')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x2, phase2, color = 'red' ) #plot each concentration 
    #plt.xlim(startpoint, endpoint)
    plt.ylim(0,.8)
    plt.show()
    
    plt.title('Graph for phase 1')
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x1, phase1, color = 'red' ) #plot each concentration 
    #plt.xlim(30, startpoint-6)
    plt.ylim(0,.05)
    plt.show()
    
    return phase1, phase2, x1, x2

def normalize(inlist):
    newinlist = inlist
    #.to_numpy().reshape(-1) #take input vector and make sure its a numpy array
    newinlist = [item - (np.min(newinlist) - 0.0000001) for item in newinlist] #downshift to 0
    newinlist = [item/(np.max(newinlist)-np.min(newinlist)) for item in newinlist] #normalize
    return newinlist
def sigmoid(x, a, b, c):
     y = 1 / (1 + c*np.exp(-b*(x-a))) 
     return y
 
def predictedsig(x, a, b, c):
    b = 5.16E-2
    c = 1.23E2
    y = sigmoid(x, a, b, c)
    
def sigmoidtrain(x, inlist):
    #x = np.linspace(0, len(inlist), 1)
    #print(x)
    #print(inlist)
    parameters, pcov = curve_fit(sigmoid, x, inlist, p0=[110, 0.001, 100])
    #print(parameters)
    #print(pcov)
    y = sigmoid(x, *parameters)
    a = parameters[0]
    b = parameters[1]
    c = parameters[2]
    error = 0
    for row in range (0,len(inlist)):
        error += (inlist[row] - y[row])**2
    error = np.sqrt(error/len(inlist))
    return error, a, b, c

def sigmoidtest(x, inlist, a,b,c,expectederror):
    #x = np.linspace(0, len(inlist), 1)
    y = predictedsig(x,a,b,c)
    error=0
    for row in range (0,len(inlist)):
        error += (inlist[row] - y[row])**2
        
    error = np.sqrt(error/len(inlist))
	
    if error < expectederror:
        return 'GOOD DATA!'
    return 'Bad data'
