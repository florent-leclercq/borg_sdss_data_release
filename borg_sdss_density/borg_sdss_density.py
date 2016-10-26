import numpy as np
from pylab import *

data = np.load('borg_sdss_density.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=data['ranges'][0]
xmax=data['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=data['ranges'][2]
ymax=data['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=data['ranges'][4]
zmax=data['ranges'][5]

#3D ensemble mean for the final density contrast 
mean=data['mean']

#3D pixelwise standartdeviation for the final density contrast
stdv=data['stdv']

#Now make a example plot
imshow(mean[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax])
plt.show()