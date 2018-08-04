#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
import numpy as np


lista1 = [11,20,35,48,60,18]
lista2 = [22,50,3,15,40,30]
lista3 = [15,80,25]
plt.ylabel ("ej y")
plt.xlabel ("eje x")
plt.plot(lista1,marker = "p",color = "r",label = "enero")
plt.plot(lista2,marker = "p",color = "b",label = "febrero")
plt.plot(lista3,marker = "p",color= "y",label = "marzo")
plt.title("grafico")
plt.legend()
plt.show()
