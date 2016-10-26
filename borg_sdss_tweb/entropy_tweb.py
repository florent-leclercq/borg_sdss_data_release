import numpy as np
from pylab import *
import warnings
warnings.filterwarnings("ignore")

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
V=tweb['voids']
S=tweb['sheets']
F=tweb['filaments']
C=tweb['clusters']

#Compute the entropy
VlogV = V*np.log2(V)
SlogS = S*np.log2(S)
FlogF = F*np.log2(F)
ClogC = C*np.log2(C)
VlogV[np.isnan(VlogV)]=0.
SlogS[np.isnan(SlogS)]=0.
FlogF[np.isnan(FlogF)]=0.
ClogC[np.isnan(ClogC)]=0.

H = - VlogV - SlogS - FlogF - ClogC

#Now make a example plot
imshow(H[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax])
plt.show()