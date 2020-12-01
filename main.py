from Reglas import *
from Defuzzy import *
from Reglas import pyplot
import Pertenencias as mf
from matplotlib import pyplot

salario_malo=Categoria("Malo",mf.Trapezoide(200,225,275,300))
salario_medio=Categoria("Medio",mf.Trapezoide(299,325,375,400))
salario_bueno=Categoria("Bueno",mf.Trapezoide(399,425,475,500))
salario=Variable([salario_malo,salario_medio,salario_bueno])
#salario.Grafica()

estimulo_malo=Categoria("Bajo",mf.Triangular(0,10,20))
estimulo_medio=Categoria("Medio",mf.Triangular(20,25,35))
estimulo_alto=Categoria("Alto",mf.Triangular(35,40,50))
estimulo=Variable([estimulo_malo,estimulo_medio,estimulo_alto])
#estimulo.Grafica()

satisfaccion_mala=Categoria("Mala",mf.Triangular(1,1.5,2))
satisfaccion_media=Categoria("Media",mf.Triangular(2,3,4))
satisfaccion_alta=Categoria("Perfecta",mf.Triangular(4,4.5,5))
satisfaccion=Variable([satisfaccion_mala,satisfaccion_media,satisfaccion_alta])
#satisfaccion.Grafica()

r1=salario_malo+estimulo_malo>=satisfaccion_mala
r2=salario_medio+estimulo_malo>=satisfaccion_mala
r3=salario_bueno+estimulo_malo>=satisfaccion_media
r4=salario_malo+estimulo_medio>=satisfaccion_media
r5=salario_medio+estimulo_medio>=satisfaccion_media
r6=salario_bueno+estimulo_medio>=satisfaccion_media
r7=salario_malo+estimulo_alto>=satisfaccion_media
r8=salario_medio+estimulo_alto>=satisfaccion_alta
r9=salario_bueno+estimulo_alto>=satisfaccion_alta


infer=Mamdani_A
desf=Centroid

s=float(input('Escriba el valor del Salario\n'))
h=float(input('Escriba el valor del estimulo\n'))
rls=desf(infer(r1,r2,r3,r4,r5,r6,r7,r8,r9))
n= rls((s,h),(s,h),(s,h),(s,h),(s,h),(s,h),(s,h),(s,h),(s,h))
print('El Trabajador tendra una satisfaccion de {0}'.format(n))
