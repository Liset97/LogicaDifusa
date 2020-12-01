import Pertenencias as mf
from Pertenencias import *
from Defuzzy import *
from matplotlib import pyplot

#Aqui se definen las dos operaciones de ^ y v
# Esta clase representa la operacion de and entre dos fuzzy-set
class And:
    def __init__(self,op):
        self.op=op
    def __call__(self,x,y):
        return self.op(x,y)
    def __str__(self):
        return '+'
    def __repr__(self):
        return self.__str__()
# Esta clase representa la operacion de or entre dos fuzzy-set
class Or:
    def __init__(self,op):
        self.op=op
    def __call__(self,x,y):
        return self.op(x,y)
    def __str__(self):
        return '-'
    def __repr__(self):
        return self.__str__()

Max=And(max)
Min=Or(min)




class Variable:
    def __init__(self,L:list):
        self.L=L
    
    def Grafica(self,keys=None):
        intv=self.Intervalos(keys)
        if keys is None:
            for l in self.L:
                l.fuzzy_set.Grafico(intv,l.name)
        else:
            for k in keys:
                list(filter(lambda x:x.name==k,self.L))[0].fuzzy_set.graph(intv,k)
        pyplot.legend(loc='center')
        pyplot.show()
    
    
    def Intervalos(self,keys=None):
        xmin=math.inf
        xmax=-math.inf
        if keys is None:
            for l in self.L:
                xmin= l.fuzzy_set.min if l.fuzzy_set.min<xmin else xmin
                xmax= l.fuzzy_set.max if l.fuzzy_set.max>xmax else xmax
        else:
            for k in keys:#itero por cada nombre
                # Selecciono en L los valores linguisticos que le corresponden al nonbre k correspondiente
                fs= list(filter(lambda x:x.name==k,self.L))[0].fuzzy_set
                print(fs)
                xmin= fs.min if fs.min<xmin else xmin
                xmax= fs.max if fs.max>xmax else xmax
        return xmin,xmax

class Antecedente(object):
    def __init__(self,rule1,op=None,rule2=None):
        self.rule1=rule1
        self.op=op
        self.rule2=rule2
    def __call__(self,*args):
        return self.op(self.rule1(args[0]),self.rule2(args[1:len(args)]))
    def __str__(self):
        return '{0} {1} {2}'.format(self.rule1,self.op,self.rule2)
    def __repr__(self):
        return self.__str__()
    def __add__(self,other):
        return Antecedente(self,Max,other)
    def __sub__(self,other):
        return Antecedente(self,Min,other)
    def __ge__(self,other):
        return Regla(self,other)  



class Categoria(Antecedente):
    def __init__(self,name,fuzzy_set:mf.Trapezoide):
        self.name=name
        self.fuzzy_set=fuzzy_set
        self.min=fuzzy_set.min
        self.max=fuzzy_set.max
    def __call__(self,x):
        if type(x) == tuple:
            return self.fuzzy_set(x[0])
        return self.fuzzy_set(x)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()



class Consecuente(object):
    def __init__(self,category:Categoria):
        self.cat=category
        self.min=category.min
        self.max=category.max

class Mamdani(Consecuente):
    def __call__(self,v):
        return lambda x: min(self.cat.fuzzy_set(x),v)

class Larsen(Consecuente):
    def __call__(self,v):
        return lambda x: self.cat.fuzzy_set(x)*v


class Regla(object):
    def __init__(self,predecessor:Antecedente,consecuent:Consecuente):
        self.predecessor=predecessor
        self.consecuent=consecuent
        self.min=consecuent.min
        self.max=consecuent.max

    def __call__(self,func,*args):
        return func(self.consecuent)(self.predecessor(*args))

class Metodos(object):
    def __init__(self,*rules):
        self.rules=rules
        self.min=math.inf
        self.max=-math.inf
        for r in rules:
            self.min=min(self.min,r.min)
            self.max=max(self.max,r.max)
    def __call__(self,func,*args):
        return lambda x: max([self.rules[i](func,*(args[i]))(x) for i in range(len(self.rules))])

class Larsen_A(Metodos):
    def __call__(self,*args):
        return super().__call__(Larsen,*args)

class Mamdani_A(Metodos):
    def __call__(self,*args):
        return super().__call__(Mamdani,*args)



