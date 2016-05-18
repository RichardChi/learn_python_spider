#!/usr/bin/env python
import string
import matplotlib.pyplot as plt  
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
 
if __name__ == '__main__':    
    #file = open('/home/richard/data/guangliu_data1 .txt', 'r')
    file = open('/home/richard/data/1/odom_data2.txt', 'r')
    #file = open('/home/richard/data/opticflowdata.txt', 'r')
    linesList = file.readlines()
#     print(linesList)
    linesList = [line.strip().split() for line in linesList]
    #linesList = [line.rstrip('\n').split(' ') for line in linesList]
    file.close()    
    #print(linesList:)
    #print(linesList)
#     years = [string.atof(x[0]) for x in linesList]
    x1 = [float(x[0]) for x in linesList]
    #print len(x1)#x1
    y1 = [float(x[1]) for x in linesList]
    #print len(y1)#y1
    z = [float(x[2]) for x in linesList]
    #print len(z)#z
    #index = y1.index(min(y1))
    #print index
    #distence = math.sqrt((x1[0] - x1[index]) **2 + (y1[0] - y1[index])**2)
    #distence = y1[0] - y1[-1]
    #print distence
    #plt.plot(x, y, 'b*')#,label=$cos(x^2)$)
    plt.grid()
    plt.plot(x1, y1,'r')
    plt.axis('equal')
    #3D trajectory
    fig = figure()
    ax = Axes3D(fig)
    ax.plot3D(x1, y1, z)
    ax.axis('equal')
    #plt.xlabel(years(+2000))
    #plt.ylabel(housing average price(*2000 yuan))
    #plt.ylim(0, 15)
    #plt.title('line_regression & gradient decrease')
    
    plt.legend()
    plt.show()
