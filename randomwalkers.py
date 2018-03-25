from random import randint
array=[]
narray=range(0,101)
for N in range(0,101):
    count=0
    for  n in range(0,5000):
        pos1=0
        pos2=0
        for x in range(0,N):
            x=(randint(0,5000))/5000
            if(x<=0.5):
                pos1=pos1-1
            else:
                pos1=pos1+1
            y=(randint(0,5000))/5000
            if(y<=0.5):
                pos2=pos2-1
            else:
                pos2=pos2+1
        if(pos1==pos2):
            count+=1
    #print(count/50000)
    array.append(count/5000)
xmax =101
ymax = 1


import matplotlib.pyplot as plt
plt.plot(narray,array, 'b-')
plt.axis([0,xmax,0,ymax])
plt.show()
