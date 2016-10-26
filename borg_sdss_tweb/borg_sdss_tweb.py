import numpy as np
from pylab import *

tweb = np.load('borg_sdss_tweb.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=tweb['ranges'][0]
xmax=tweb['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=tweb['ranges'][2]
ymax=tweb['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=tweb['ranges'][4]
zmax=tweb['ranges'][5]

#3D probabilistic maps for T-web structures
voids=tweb['voids']
sheets=tweb['sheets']
filaments=tweb['filaments']
clusters=tweb['clusters']

#Now make a example plot
imshow(filaments[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax])
plt.show()