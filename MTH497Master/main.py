# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:57:02 2020

@author: hecto
"""

from assay import singleWell, allWells, groupWells, concenWells, tripWells


loc1 = "Assay1.xlsx"
loc2 = "Assay2.xlsx"
loc3 = "Assay3.xlsx"
loc4 = "Assay4.xlsx"
loc5 = "Assay5.xlsx"
loc6 = "Assay6.xlsx"
loc7 = "Assay7.xlsx"

file = -1 #set file to a random number in order to initialize it

while file != 'stop':
    file=str(input("Please enter an Assay number\n"))
    if(file == '1'):
        file=str(input("Please enter which graph you would like to see\n"))
        if(file == "single"):
            
            singleWell(loc1)
        elif(file == "all"):
            allWells(loc1)
        elif(file == "groups"):
            groupWells(loc1)
        elif(file == "concentrations"):
            concenWells(loc1)
        elif(file == "triplicate"):
            tripWells(loc1)
        elif(file == "everything"):
            singleWell(loc1)
            allWells(loc1)
            groupWells(loc1)
            concenWells(loc1)
            tripWells(loc1)
        else:
            print('Invalid. Try again')
            
    elif(file == '2'):
        file=str(input("Please enter which graph you would like to see\n"))
        if(file == "single"):
            singleWell(loc2)
        elif(file == "all"):
            allWells(loc2)
        elif(file == "groups"):
            groupWells(loc2)
        elif(file == "concentrations"):
            concenWells(loc2)
        elif(file == "triplicate"):
            tripWells(loc2)
        elif(file == "everything"):
            singleWell(loc2)
            allWells(loc2)
            groupWells(loc2)
            concenWells(loc2)
            tripWells(loc2)
        else:
            print('Invalid. Try again')
            
    elif(file == '3'):
        file=str(input("Please enter which graph you would like to see\n"))
        if(file == "single"):
            singleWell(loc3)
        elif(file == "all"):
            allWells(loc3)
        elif(file == "groups"):
            groupWells(loc3)
        elif(file == "concentrations"):
            concenWells(loc3)
        elif(file == "triplicate"):
            tripWells(loc3)
        elif(file == "everything"):
            singleWell(loc3)
            allWells(loc3)
            groupWells(loc3)
            concenWells(loc3)
            tripWells(loc3)
        else:
            print('Invalid. Try again')
            
    elif(file == '4'):
        file=str(input("Please enter which graph you would like to see\n"))
        if(file == "single"):
            singleWell(loc4)
        elif(file == "all"):
            allWells(loc4)
        elif(file == "groups"):
            groupWells(loc4)
        elif(file == "concentrations"):
            concenWells(loc4)
        elif(file == "triplicate"):
            tripWells(loc4)
        elif(file == "everything"):
            singleWell(loc4)
            allWells(loc4)
            groupWells(loc4)
            concenWells(loc4)
            tripWells(loc4)
        else:
            print('Invalid. Try again')
        
    elif(file == '5'):
        file=str(input("Please enter which graph you would like to see\n"))
        if(file == "single"):
            singleWell(loc5)
        elif(file == "all"):
            allWells(loc5)
        elif(file == "groups"):
            groupWells(loc5)
        elif(file == "concentrations"):
            concenWells(loc5)
        elif(file == "triplicate"):
            tripWells(loc5)
        elif(file == "everything"):
            singleWell(loc5)
            allWells(loc5)
            groupWells(loc5)
            concenWells(loc5)
            tripWells(loc5)
        else:
            print('Invalid. Try again')
        
    elif(file == '6'):
        file=str(input("Please enter which graph you would like to see\n"))
        if(file == "single"):
            singleWell(loc6)
        elif(file == "all"):
            allWells(loc6)
        elif(file == "groups"):
            groupWells(loc6)
        elif(file == "concentrations"):
            concenWells(loc6)
        elif(file == "triplicate"):
            tripWells(loc6)
        elif(file == "everything"):
            singleWell(loc6)
            allWells(loc6)
            groupWells(loc6)
            concenWells(loc6)
            tripWells(loc6)
        else:
            print('Invalid. Try again')
            
    elif(file == '7'):
        file=str(input("Please enter which graph you would like to see\n"))
        if(file == "single"):
            singleWell(loc7)
        elif(file == "all"):
            allWells(loc7)
        elif(file == "groups"):
            groupWells(loc7)
        elif(file == "concentrations"):
            concenWells(loc7)
        elif(file == "triplicate"):
            tripWells(loc7)
        elif(file == "everything"):
            singleWell(loc7)
            allWells(loc7)
            groupWells(loc7)
            concenWells(loc7)
            tripWells(loc7)
        else:
            print('Invalid. Try again')
            
    elif(file == 'stop'):
        break

    else:
        print('Invalid. Try again')