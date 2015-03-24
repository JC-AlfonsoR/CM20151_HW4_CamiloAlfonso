# -*- coding: utf-8 -*-
"""
@author: J. Camilo
python 2.7
"""
import sys
print(sys.version)
from netCDF4 import Dataset
import numpy as np

file_name = 'air.mon.ltm.nc'
f = Dataset(file_name, mode='r')
print(f)

lons = f.variables['lon'][:]
lats = f.variables['lat'][:]
air = f.variables['air'][11,:,:] #Download only one temporal slice
f.close()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
plt.figure(figsize=(30,10))
lon_0 = lons.mean()
lat_0 = lats.mean()
map = Basemap(projection='cea', lat_0=lat_0, lon_0=lon_0,
              resolution='h', area_thresh=500.0)
map.drawcoastlines()
map.drawcounties()
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
map.fillcontinents(color='coral',lake_color='aqua')
lon, lat = np.meshgrid(lons, lats)
xi,yi = map(lon, lat)
#cs = map.pcolor(xi,yi,air)
cs = map.contour(xi,yi,air,linewidths=1.5)
cbar = map.colorbar(cs,location='bottom')
#map.plot(xi,yi,'bo')
title('Air temperature - Data from ' + file_name,size=20)
plt.savefig('mapa.png')

#---------------------
#Interpolacion
points = array([lat.ravel(),lon.ravel()]).T #Puntos conocidos
values = air.ravel() #Valores conocidos

#Crear malla mas fina en n_lat, n_lon
new_lats = arange(min(lats),max(lats),1)
new_lons = arange(min(lons),max(lons),1)
n_lon,n_lat = meshgrid(new_lons,new_lats)


from scipy.interpolate import griddata
grid_interp = griddata(points, values, (n_lat,n_lon), method='nearest')
shape(grid_interp)

plt.figure(figsize=(30,10))
lon_0 = lons.mean()
lat_0 = lats.mean()
map = Basemap(projection='cea', lat_0=lat_0, lon_0=lon_0,
              resolution='h', area_thresh=500.0)
map.drawcoastlines()
map.drawcounties()
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
map.fillcontinents(color='coral',lake_color='aqua')

xi,yi = map(n_lon, n_lat)
cs = map.contour(xi,yi,grid_interp,linewidths=1.5)
cbar = map.colorbar(cs,location='bottom', pad="10%")
title('Air temperature - Data from ' + file_name,size=20)
plt.savefig('mapa_interpolado.png')