import numpy as np
from matplotlib import pyplot
import math

class Reglas(object):
    
    def __init__(self,agreg):
        self.agreg=agreg
        self.min=agreg.min
        self.max=agreg.max
    def __call__(self,*args):
        return (self.max-self.min)/2

    def TomaValor(self,*args):
        value=list(np.linspace(self.min,self.max,1000))
        funct=self.agreg(*args)
        y=[funct(i) for i in value]
        return value,y
    
    def Grafico(self,*args):
        funct=self.agreg(*args)
        x=np.linspace(self.min,self.max,1000)
        y=[funct(i) for i in x]
        pyplot.plot(x,y)
        xvalue=self.__call__(*args)
        yvalue=funct(xvalue)
        pyplot.plot([xvalue,xvalue],[0,yvalue])
        # pyplot.show()

class Centroid(Reglas):
    def __call__(self,*args):
        x,y= self.TomaValor(*args)
        return sum([ x[i]*y[i] for i in range(len(x))])/sum([ y[i] for i in range(len(x))])

class Bisectriz(Reglas):
    def __call__(self,*args):
        x,y= self.TomaValor(*args)
        return x[self.BusquedaBinaria(y)]
   
    def BusquedaBinaria(self,y):
        a=0
        b=0
        f=0
        l=len(y)-1
        while f<l:
            m=(f+l)//2
            a1=sum(y[f:m+1])+a
            b1=sum(y[m+1:l+1])+b
            if a1>=b1:
                l=m
                b=b1
            else:
                f=m+1
                a=a1
        return f


# Middle of Maximum
class MOM(Reglas):
    def __call__(self,*args):
        x,y=self.TomaValor(*args)
        maximum=max(y)
        maximums=list(filter(lambda i:y[i]==maximum,range(len(y))))
        return x[maximums[len(maximums)//2]]

        
