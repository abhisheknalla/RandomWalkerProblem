import random
import numpy as np
import math
import matplotlib.pyplot as plt
x=0
N=100
array=[]
array2=[]
array3=[]
array.append(0)
array.append(0)
array.append(0)
r = 100
count=0
array[0]=0
for t in range(0,r+1):
    for i in range(N):
        array[0]=0
        array[1]=0
        array[2]=0
        for j in range(N):
            for k in range(3):
                if random.random()<=0.5:
                    array[k]=array[k]-1
                else:
                    array[k]=array[k]+1
        if k*k<=(array[0]*array[0])+(array[1]*array[1])+(array[2]*array[2]):
            count=count+1
    p = count
    array2.append(t)
    array3.append(p)
plt.plot(array2,array3,'r-')
plt.show()
