import numpy as np
from pylab import *

diva = np.load('borg_sdss_diva.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=diva['ranges'][0]
xmax=diva['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=diva['ranges'][2]
ymax=diva['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=diva['ranges'][4]
zmax=diva['ranges'][5]

#3D probabilistic maps for DIVA structures
voids=diva['voids']
sheets=diva['sheets']
filaments=diva['filaments']
clusters=diva['clusters']

#Now make a example plot
imshow(filaments[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax])
plt.show()