# -*- coding: utf-8 -*-
"""
@author: J. Camilo
python 2.7
Probado en Spyder
"""

from sys import version
print("Version ",version)

import urllib

#En python 2.7
response = urllib.urlopen("http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt")
F = open("data.dat","w")
for line in response:
    l = str(line)
    s = l.split()
    ss = s[1]
    for i in range(2,14):
        ss = ss + " " + s[i]
    F.write(ss + "\n")
F.close()

import pandas as pd
data = pd.read_table("data.dat",sep=" ") #Leer datos
data = data.sort(['m2s_ratio'], ascending=False) #Ordenar datos en orden descendente acorede al flujo
#data.head()

#Seleccionar los 300 mayores y guardarlos aparte
n = 300
n_data = data[1:n+1] #Seleccionar los n primero rios de los datos ordenados
n_data.River_Name.str.decode(encoding='latin-1',errors='strict')
n_data.to_csv("top_300_rios.csv", index=False)