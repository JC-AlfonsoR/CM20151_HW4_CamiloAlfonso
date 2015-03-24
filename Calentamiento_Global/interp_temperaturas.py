# -*- coding: utf-8 -*-
"""

@author: J. Camilo
python 3.4
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d

import sys
print("\nPandas Version",pd.__version__)
print("Python version",sys.version)

plt.style.use('ggplot')

Data= pd.read_csv("Data.csv")
Data = Data[['anno','mes','fecha','ciudad','temperatura']] #Quitar columna de indices
Data['date'] = pd.to_datetime(Data['fecha']) #convertir fecha a TimeStamp
#print(Data.head())

ciudades = ['Barranquilla', 'Ipiales', 'Bucaramanga', 'Bogota','Cali']
n = len(ciudades)
plt.figure(figsize=(12,7))
i  = 0

for c in ciudades:
    C = Data[Data['ciudad'] == c]
    #subplot(n, 1, i)
    plt.plot(C['date'], C['temperatura'], 'o',alpha=0.7,label=c)
    #title(c)
    #ylabel('Temperatura [°c]')
    #xlabel('Fecha')
    #i += 1
plt.title('Temperatura en ciudades de Colombia')
plt.xlabel('Fecha')
plt.ylabel('Temperatura °c')
plt.legend(loc=3)
plt.savefig('Temperatura_ciudades.png')

#Interpolacion
for c in ciudades:
    #Extraer datos de ciudad
    D = Data[Data['ciudad']==c]
    D['date'] = pd.to_datetime(D['fecha'])
    D.sort(['date'],ascending=True)
    date = D['fecha']
    T = np.array(D['temperatura'])
    #date = np.array([datestr2num(s) for s in date])
    
    #Crear dominio mas fino para fechas
    d0 = min(D['date'])
    df = max(D['date'])
    n = len(date)
    rang = np.linspace(min(date), max(date),len(date)*2)
    #print(type(rang[0]))
    
    # Interpolaciones
    f = interp1d(date,T,kind='linear')
    T_f = f(date)

    f_spl = interp1d(date, T, kind = "cubic")
    T_spl = f_spl(date)

    poly2 = polyfit(date, T, deg=2)
    T_poly2 = poly2[0]**2*date + poly2[1]*date +  poly2[2]
    
    plt.figure(figsize=(30,5))
    plt.subplot(1,3,1)
    plt.plot_date(date,T,'o')
    plt.plot_date(date,T_f,'-')
    plt.title(c+' Interpolacion Lineal')
    plt.xlabel('Fehca')
    plt.ylabel('Temperatura [°c]')
    plt.subplot(1,3,2)
    plt.plot_date(date,T,'o')
    plt.plot_date(date, T_spl,'-')
    plt.title(c+ ' Interpolacion por splines orden 3')
    plt.xlabel('Fehca')
    plt.ylabel('Temperatura [°c]')
    plt.subplot(1,3,3)
    plt.plot_date(date,T,'o')
    plt.plot_date(date, T_poly2,'-')
    plt.title(c+ ' Interpolacion con polinomio orden 2')
    plt.xlabel('Fehca')
    plt.ylabel('Temperatura [°c]')
    s = c + '_Interp.png'
    plt.savefig(s)
