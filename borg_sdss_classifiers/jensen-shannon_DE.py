import numpy as np
from pylab import *

js_DE = np.load('borg_sdss_js_DE.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=js_DE['ranges'][0]
xmax=js_DE['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=js_DE['ranges'][2]
ymax=js_DE['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=js_DE['ranges'][4]
zmax=js_DE['ranges'][5]

#3D maps of Jensen-Shannon divergence between cosmic web-type posteriors for different dark energy models
tweb_js_DE=js_DE['tweb']
diva_js_DE=js_DE['diva']
origami_js_DE=js_DE['origami']

#Now make a example plot
imshow(diva_js_DE[:,:,128],origin='lower', extent=[ymin,ymax,zmin,zmax])
plt.show()