from re import L
import numpy as np
import matplotlib.pyplot as plt

x = np.array((-2,0,1))
y = np.array((0,1,-1))
z = np.linspace(-3,3,10)
order = len(x)


def f(z,xv,p):
    #print(xv[(p-len(xv)+1)])
    return z-xv[(p-len(xv)+1)]

def bot(xv,p,i):
    #print(xv[i])
    return xv[i]-xv[(p-len(xv)+1)]

#def p(y,li):
#    return y*li

px = np.zeros((len(z),1))
for u in range(len(z)):
    li = np.zeros((order,1))
    for i in range(order):
        currtop = 1
        currbot = 1
        for p in range(order-1):
            currtop = currtop * f(z[u],x,i+p)
            #print(f(z,x,p))
            currbot = currbot * bot(x,i+p,i)
        
        li[i] = currtop/currbot
    px[u] = y[i]*li[i]




print(px)
points = len(px)
cc = np.zeros((points,2))
for i in range(points):
    cc[i][0]=z[i]
    cc[i][1]=px[i]

plt.scatter(cc[:,0],cc[:,1])
plt.savefig("img.pdf", format="pdf", bbox_inches="tight")
plt.show()



#print(li)


