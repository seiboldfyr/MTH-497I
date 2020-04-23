# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:21:20 2020

@author: Sydney's PC
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def normalize(list):
    newlist = list.to_numpy().reshape(-1) #take input vector and make sure its a numpy array
    newlist = [item - (np.min(newlist) - 0.0000001) for item in newlist] #downshift to 0
    newlist = [item/(np.max(newlist)-np.min(newlist)) for item in newlist] #normalize
    return newlist
def sigmoid(x, a, b, c):
     y = 1 / (1 + c*np.exp(-b*(x-a))) 
     return y
 
 def predictedsig(x, a, b, c):
    b = 5.16E-2
    c = 1.23E2
    y1 = sigmoid(x, a, b, c)
    
def sigmoidtrain(list):
    x = np.linspace(0, len(list), 1)
    parameters, pcov = curve_fit(sigmoid, x, list, p0=[110, 0.001, 100])
    print(parameters)
    print(pcov)
    y = sigmoid(x, *parameters)
    error = 0
    for row in range (0,len(list)):
        error += (list[row] - y[row])**2
    error = np.sqrt(error/len(list))
    return error, parameters

def sigmoidtest(list, a,b,c,expectederror):
    x = np.linspace(0, len(list), 1)
    y1 = predictedsig(x,a,b,c)
    error=0
    for row in range (0,len(list)):
        error += (list[row] - y[row])**2
    error = np.sqrt(error/len(list))
	
	if error < expectederror:
		return 'GOOD DATA!'
	return 'Bad data'

def test(file):
    x=pd.read_excel(file, usecols="B")
    g2=pd.read_excel(file, usecols="C:CT")
     for i in range(1, len(x)):
         list = g2(i)
         list = normalize(list)
         phase1, phase2 = section(list)
         sigmoidtest(list, aexpec, bexpec, cexpec, errorexpec)