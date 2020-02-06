# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

loc1 = "Assay1.xlsx"
loc2 = "Assay2.xlsx"
loc3 = "Assay3.xlsx"
loc4 = "Assay4.xlsx"
loc5 = "Assay5.xlsx"
loc6 = "Assay6.xlsx"
loc7 = "Assay7.xlsx"

#wb = xlrd.open_workbook(loc)
#sheet =  wb.sheet_by_index(0)

# For row 0 and column 0
#sheet.cell_value(0, 0)
#sheet.nrows

#for row in range(sheet.nrows):
  #  print(sheet.cell_value(row, 2))


#data = pd.read_excel(excel_file)

#Graphs first column of assay. Just one concentration
  
  
#for file in ox.listdir("C:/Users/hecto/Downloads/AssayData/Assay1.xlsx"):
  
#FOR ASSAY1  
assarray = [loc1, loc2, loc3, loc4, loc5, loc6, loc7]
for loc in assarray:
    
    print(loc)#tell us which assay this is
    x=pd.read_excel(loc, usecols="B")
    g=pd.read_excel(loc, usecols="C")
    
    plt.plot(x,g)
    plt.show()
    
    g2=pd.read_excel(loc, usecols="C:CT")
    
    plt.plot(x,g2)
    plt.show()
    
    y1=pd.read_excel(loc, usecols="C:Z")
    y2=pd.read_excel(loc, usecols="AA:AX")
    y3=pd.read_excel(loc, usecols="AY:BV")
    y4=pd.read_excel(loc, usecols="BW:CT")
    
    #plt.plot(x,y1,y2,y3,y4)
    plt.xlabel('Cycle number')
    plt.ylabel('Concentration')
    plt.plot(x,y1,color='red')
    plt.plot(x,y2,color='green')
    plt.plot(x,y3,color='yellow')
    plt.plot(x,y4,color='blue')
    plt.xlim(0,100)
    plt.ylim(2000,4000)
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
    print('------------------------------------------------------------------')

"""
print('Assay 2')

x=pd.read_excel(loc2, usecols="B")
g=pd.read_excel(loc2, usecols="C")

plt.plot(x,g)
plt.show()

g2=pd.read_excel(loc2, usecols="C:CT")

plt.plot(x,g2)
plt.show()

y1=pd.read_excel(loc2, usecols="C:Z")
y2=pd.read_excel(loc2, usecols="AA:AX")
y3=pd.read_excel(loc2, usecols="AY:BV")
y4=pd.read_excel(loc2, usecols="BW:CT")

#plt.plot(x,y1,y2,y3,y4)
plt.xlabel('Cycle number')
plt.ylabel('Concentration')
plt.plot(x,y1,color='red')
plt.plot(x,y2,color='green')
plt.plot(x,y3,color='yellow')
plt.plot(x,y4,color='blue')
plt.show()

print('-----------------------------------------------------------------')

print('Assay 3')
x=pd.read_excel(loc3, usecols="B")
g=pd.read_excel(loc3, usecols="C")

plt.plot(x,g)
plt.show()

g2=pd.read_excel(loc3, usecols="C:CT")

plt.plot(x,g2)
plt.show()

y1=pd.read_excel(loc3, usecols="C:Z")
y2=pd.read_excel(loc3, usecols="AA:AX")
y3=pd.read_excel(loc3, usecols="AY:BV")
y4=pd.read_excel(loc3, usecols="BW:CT")

#plt.plot(x,y1,y2,y3,y4)
plt.xlabel('Cycle number')
plt.ylabel('Concentration')
plt.plot(x,y1,color='red')
plt.plot(x,y2,color='green')
plt.plot(x,y3,color='yellow')
plt.plot(x,y4,color='blue')
plt.show()

print('------------------------------------------------------------------')

print('Assay 4')

x=pd.read_excel(loc4, usecols="B")
g=pd.read_excel(loc4, usecols="C")

plt.plot(x,g)
plt.show()

g2=pd.read_excel(loc4, usecols="C:CT")

plt.plot(x,g2)
plt.show()

y1=pd.read_excel(loc4, usecols="C:Z")
y2=pd.read_excel(loc4, usecols="AA:AX")
y3=pd.read_excel(loc4, usecols="AY:BV")
y4=pd.read_excel(loc4, usecols="BW:CT")

#plt.plot(x,y1,y2,y3,y4)
plt.xlabel('Cycle number')
plt.ylabel('Concentration')
plt.plot(x,y1,color='red')
plt.plot(x,y2,color='green')
plt.plot(x,y3,color='yellow')
plt.plot(x,y4,color='blue')
plt.show()

print('------------------------------------------------------------------')

print('Assay 5')

x=pd.read_excel(loc5, usecols="B")
g=pd.read_excel(loc5, usecols="C")

plt.plot(x,g)
plt.show()

g2=pd.read_excel(loc5, usecols="C:CT")

plt.plot(x,g2)
plt.show()

y1=pd.read_excel(loc5, usecols="C:Z")
y2=pd.read_excel(loc5, usecols="AA:AX")
y3=pd.read_excel(loc5, usecols="AY:BV")
y4=pd.read_excel(loc5, usecols="BW:CT")

#plt.plot(x,y1,y2,y3,y4)
plt.xlabel('Cycle number')
plt.ylabel('Concentration')
plt.plot(x,y1,color='red')
plt.plot(x,y2,color='green')
plt.plot(x,y3,color='yellow')
plt.plot(x,y4,color='blue')
plt.show()

print('------------------------------------------------------------------')

print('Assay 6')

x=pd.read_excel(loc6, usecols="B")
g=pd.read_excel(loc6, usecols="C")

plt.plot(x,g)
plt.show()

g2=pd.read_excel(loc6, usecols="C:CT")

plt.plot(x,g2)
plt.show()

y1=pd.read_excel(loc6, usecols="C:Z")
y2=pd.read_excel(loc6, usecols="AA:AX")
y3=pd.read_excel(loc6, usecols="AY:BV")
y4=pd.read_excel(loc6, usecols="BW:CT")

#plt.plot(x,y1,y2,y3,y4)
plt.xlabel('Cycle number')
plt.ylabel('Concentration')
plt.plot(x,y1,color='red')
plt.plot(x,y2,color='green')
plt.plot(x,y3,color='yellow')
plt.plot(x,y4,color='blue')
plt.show()

print('------------------------------------------------------------------')

print('Assay 7')

x=pd.read_excel(loc7, usecols="B")
g=pd.read_excel(loc7, usecols="C")

plt.plot(x,g)
plt.show()

g2=pd.read_excel(loc7, usecols="C:CT")

plt.plot(x,g2)
plt.show()

y1=pd.read_excel(loc7, usecols="C:Z")
y2=pd.read_excel(loc7, usecols="AA:AX")
y3=pd.read_excel(loc7, usecols="AY:BV")
y4=pd.read_excel(loc7, usecols="BW:CT")

#plt.plot(x,y1,y2,y3,y4)
plt.xlabel('Cycle number')
plt.ylabel('Concentration')
plt.plot(x,y1,color='red')
plt.plot(x,y2,color='green')
plt.plot(x,y3,color='yellow')
plt.plot(x,y4,color='blue')
plt.show()

print('------------------------------------------------------------------')
"""
