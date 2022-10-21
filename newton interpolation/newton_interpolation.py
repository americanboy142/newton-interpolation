import numpy as np
import matplotlib.pyplot as plt

x = np.array((-2,0,1))
y = np.array((0,1,-1))
order = len(x)-1

coef = np.zeros((len(x),1))

# divided difference
#{ 0  1  y[1]-y[0]  
#  1  1  x[1]-x[0]  dif[0]-dif[1]
#  2  2             x[0]-x[2]
#  3  3             x[1]-x[3]
#}
dif = []
a=[]
for i in range(len(x)-1):
    dif.append((y[i+1]-y[i])/(x[i+1]-x[i]))

a.append(dif[0])

for i in range(len(dif)-1):
    dif.append((dif[i+1]-dif[i])/(x[i+2]-x[i]))

a.append(dif[2])

p = lambda z: y[0]+a[0]*(z-x[0])+a[1]*(z-x[1])*(z-x[2])

points=10
cc = np.zeros((points,2))

for i in range(points):
    cc[i][0]=i
    cc[i][1]=p(i)

plt.scatter(cc[:,0],cc[:,1])
plt.savefig("img.pdf", format="pdf", bbox_inches="tight")
plt.show()