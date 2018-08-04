#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
#definimos el periodo de la grafica semoidal
periodo= 2 
# definimos el array dimensional
x = np.linspace(0,10,1000)
# definimos la funcion semoidal
y = np.sin(2*np.pi*x/periodo)
# creamos la figura 
plt.figure()
# primera grafica 
plt.subplot(2,2,1)
plt.title("Grafica 1")
plt.plot(x,y,"r:",marker="o")
# segunda grafica
plt.subplot(2,2,2)
plt.title("Grafica 2")
plt.plot(x,y,"g-")
# tercera grafica 
plt.subplot(2,2,3)
plt.plot(x,y,"b:")
plt.title("Grafica 3")
# cuarta grafica 
plt.subplot(2,2,4)
plt.plot(x,y,"k-")
plt.title("Grafica 4")
# mostramos en pantalla
plt.show()