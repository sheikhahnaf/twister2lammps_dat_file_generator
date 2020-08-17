# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:45:22 2020

@author: Sheikh Ahnaf Alvi
"""

import numpy as np
import os
import sys

#load the twister file

cwd=os.getcwd()
print(cwd)
file=sys.argv[1]
out="lammps_"+file[:-4]+".txt"
print(os.path.join(cwd,file))
atom,x,y,z=np.genfromtxt(file,delimiter=' ',unpack=True)

# getting the z co-ordinates
zed=np.unique(z)
print(zed)
zed.sort()
print(zed)
layer_num=list(range(len(z)))

def layer(z,zed,file,out):
    for x in range(len(z)):
        if z[x]==zed[0]:
            layer_num[x]=1
        elif z[x]==zed[1]:
            layer_num[x]=2
        elif z[x]==zed[2]:
            layer_num[x]=3
        elif z[x]==zed[3]:
            layer_num[x]=4
        elif z[x]==zed[4]:
            layer_num[x]=5
        else :
            layer_num[x]=6
            
    
    with open(file,"r") as f:
        lines=f.readlines()
    count=0    
    for line in lines:
        atom_id=count+1
        print(line)
        list_line=line.split(" ")
        print(list_line)
        list_line[0]=str(layer_num[count])
        list_line.insert(0,str(atom_id))
        lin=  ' '.join(list_line)
        
        print(lin)
        with open(out,"a") as fo:
             fo.writelines(lin)
        
        count=count+1
        
       
layer(z,zed,file,out)
        
        
        


