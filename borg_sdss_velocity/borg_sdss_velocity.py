import numpy as np
from pylab import *

velocity = np.load('borg_sdss_velocity.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=velocity['ranges'][0]
xmax=velocity['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=velocity['ranges'][2]
ymax=velocity['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=velocity['ranges'][4]
zmax=velocity['ranges'][5]

#3D probabilistic maps for velocity field
vx_mean=velocity['vx_mean']
vx_var=velocity['vx_var']
vy_mean=velocity['vy_mean']
vy_var=velocity['vy_var']
vz_mean=velocity['vz_mean']
vz_var=velocity['vz_var']

#Now make a example plot
f, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.imshow(vx_mean[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax], cmap="magma")
ax1.set_title('$v_x$')
ax2.imshow(vy_mean[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax], cmap="magma")
ax2.set_title('$v_y$')
ax3.imshow(vz_mean[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax], cmap="magma")
ax3.set_title('$v_z$')
plt.show()