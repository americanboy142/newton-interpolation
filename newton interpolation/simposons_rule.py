import numpy as np
import pandas as pd

class simpsons_rule:
    
    def __init__(self,a,b,n):
        self.a = a
        self.b = b
        self.n = n
        self.h = (self.b-self.a)/self.n
        self.f = lambda x: x
        pass
    
    # will replace both sums
    # input: (upper bound i.e.(n/2,(n-2)/2), special: alows return to very)
    def sigma(self,end,special):
        return sum(self.f(special+2*i*self.h) for i in range(1,int(end)))

    def simpsons(self):
        return(self.h/3*((self.f(self.a)+self.f(self.b))+4*self.sigma(self.n/2,self.a-self.h)+2*self.sigma((self.n-2)/2,self.a)))


n = [16,32,64,128,128*2,128*4,128*6,128*8,128*10,128*12,128*14,128*16,128*18,128*20]
df = pd.DataFrame(columns=['N','Approximation','Error'])

trueValue = 2

for i in n:
    aprox = simpsons_rule(0,2,i).simpsons()
    error = trueValue-aprox
    df = df.append({'N':int(i),'Approximation':aprox,'Error':error}, ignore_index=True)
print(df)