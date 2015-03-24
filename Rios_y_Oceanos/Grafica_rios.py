# -*- coding: utf-8 -*-
"""

@author: J. Camilo
python 2.7
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("top_300_rios.csv")
#data.head()

#Construir Mapa
plt.figure(figsize=(30,15))
map = Basemap(projection='cea', lat_0=0, lon_0=-100,
              resolution='h', area_thresh=1000.0)
map.drawcoastlines()
map.drawcounties()
map.fillcontinents(color='green')
map.drawmapboundary()
map.drawmeridians(arange(0,360,30))
map.drawparallels(arange(-90,90,30))


n2 = 150
lons = array(data.lonm[1:n2])
lats = array(data.latm[1:n2])
x,y = map(lons, lats)
map.plot(x, y, 'bo', markersize=10)

rates = list(data.m2s_ratio)
names = list(data.River_Name)
labels = []
for i in range(len(names)):
    s = str(str(rates[i]))
    labels.append(s)
#labels = list(data.m2s_ratio)
#labels = [str(l) for l in labels]
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt, ypt, label, bbox=dict(facecolor='blue', alpha=0.3),size=10)

title("Tasa de flujo en los 150 principales rios",size=20)
savefig('Rios_150.png')