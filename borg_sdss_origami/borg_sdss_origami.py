import numpy as np
from pylab import *

origami = np.load('borg_sdss_origami.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=origami['ranges'][0]
xmax=origami['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=origami['ranges'][2]
ymax=origami['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=origami['ranges'][4]
zmax=origami['ranges'][5]

#3D probabilistic maps for ORIGAMI structures
voids=origami['voids']
sheets=origami['sheets']
filaments=origami['filaments']
clusters=origami['clusters']

#Now make a example plot
imshow(voids[:,:,128],origin='lower', extent=[ymin,ymax,zmin,zmax])
plt.show()