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
Posterior_l0=tweb['voids']
Posterior_l1=tweb['sheets']
Posterior_l2=tweb['filaments']
Posterior_l3=tweb['clusters']

#Prior probabilities (numbers given in table II in Leclercq et al. 2015a)
Prior_l0 = 0.14261
Prior_l1 = 0.59561
Prior_l2 = 0.24980
Prior_l3 = 0.01198

#Decision theory framework introduced in Leclercq et al. (2015b)
alpha = 1.5	# The free parameter here corresponding to the "cost of the game"

G_a0l0 = 1./Prior_l0-alpha
G_awl0 = -alpha
G_a4l0 = 0.

G_a1l1 = 1./Prior_l1-alpha
G_awl1 = -alpha
G_a4l1 = 0.

G_a2l2 = 1./Prior_l2-alpha
G_awl2 = -alpha
G_a4l2 = 0.

G_a3l3 = 1./Prior_l3-alpha
G_awl3 = -alpha
G_a4l3 = 0.

# define the utility functions
U_a0 = G_a0l0*Posterior_l0 + G_awl1*Posterior_l1 + G_awl2*Posterior_l2 + G_awl3*Posterior_l3
U_a1 = G_awl0*Posterior_l0 + G_a1l1*Posterior_l1 + G_awl2*Posterior_l2 + G_awl3*Posterior_l3
U_a2 = G_awl0*Posterior_l0 + G_awl1*Posterior_l1 + G_a2l2*Posterior_l2 + G_awl3*Posterior_l3
U_a3 = G_awl0*Posterior_l0 + G_awl1*Posterior_l1 + G_awl3*Posterior_l2 + G_a3l3*Posterior_l3
U_a4 = G_a4l0*Posterior_l0 + G_a4l1*Posterior_l1 + G_a4l2*Posterior_l2 + G_a4l3*Posterior_l3

# make the decision maximizing the utility function
MAP = np.copy(U_a4)
MAP[np.where((U_a0>U_a1) * (U_a0>U_a2) * (U_a0>U_a3) * (U_a0>U_a4))] = 0.;		#voids
MAP[np.where((U_a1>U_a0) * (U_a1>U_a2) * (U_a1>U_a3) * (U_a1>U_a4))] = 1.;		#sheets
MAP[np.where((U_a2>U_a0) * (U_a2>U_a1) * (U_a2>U_a3) * (U_a2>U_a4))] = 2.;		#filaments
MAP[np.where((U_a3>U_a0) * (U_a3>U_a1) * (U_a3>U_a2) * (U_a3>U_a4))] = 3.;		#clusters
MAP[np.where((U_a4>=U_a0) * (U_a4>=U_a1) * (U_a4>=U_a2) * (U_a4>=U_a3))] = -1.;		#undecided

#Now make a example plot
imshow(MAP[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax])
plt.show()