import numpy as np
import scipy as sci
import math
from matplotlib import pyplot

# La definicion de un sistema difuso trapezoidal
class Trapezoide:
    def __init__(self,x1:int,x2:int,x3:int,x4:int):
        self.a=x1
        self.b=x2
        self.c=x3
        self.d=x4
        self.min=x1
        self.max=x4

    def __call__(self,x):
        if type(x)==list:
            return [self.__call__(i)  for i in x]
        if  x<=self.a:
            return 0
        elif self.a <=x<=self.b:
            return (x-self.a)/(self.b-self.a)
        elif self.b <=x<=self.c:
            return 1
        elif self.c <=x<=self.d:
            return (self.d-x)/(self.d-self.c)
        else:
            return 0

    def Grafico(self,limit:tuple=None,key=None):
        if limit is None:
            x=np.linspace(self.a,self.d,1000)
        else:
            (xmin,xmax)=limit
            x=np.linspace(xmin,xmax,1000)
        y=[self.__call__(i) for i in x]
        pyplot.plot(x,y,label=key)



class Triangular(Trapezoide):
    def __init__(self,x1:int,x2:int,x3:int):
        super().__init__(x1,x2,x2,x3)
        
class Gamma(Trapezoide):
    def __init__(self,x1:int,x2:int):
        super().__init__(x1,x2,math.inf,math.inf)
        self.min=x1
        self.max=x2

    def Grafico(self,limit:tuple=None,key=None):
        if limit is None:
            super(2*self.a -self.b,2*self.b-self.a).Grafico(key)
        else:
            super().Grafico(limit,key)

