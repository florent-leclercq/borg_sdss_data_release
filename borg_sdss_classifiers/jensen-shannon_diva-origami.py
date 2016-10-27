import numpy as np
from pylab import *
import warnings
warnings.filterwarnings("ignore")

# This script requires the npz files provided in the "borg_sdss_diva" and "borg_sdss_origami" packages of the BORG SDSS data release
# A similar script can be used with the T-web maps provided in the "borg_sdss_tweb" package
diva = np.load('borg_sdss_diva.npz')
origami = np.load('borg_sdss_origami.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=diva['ranges'][0]
xmax=diva['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=diva['ranges'][2]
ymax=diva['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=diva['ranges'][4]
zmax=diva['ranges'][5]

#3D probabilistic maps for structures
V1=diva['voids']
S1=diva['sheets']
F1=diva['filaments']
C1=diva['clusters']
V2=origami['voids']
S2=origami['sheets']
F2=origami['filaments']
C2=origami['clusters']

# Jensen-Shannon divergence
Vm=1/2.*(V1+V2)
Sm=1/2.*(S1+S2)
Fm=1/2.*(F1+F2)
Cm=1/2.*(C1+C2)

V1logV1 = V1*np.log2(V1)
S1logS1 = S1*np.log2(S1)
F1logF1 = F1*np.log2(F1)
C1logC1 = C1*np.log2(C1)
V1logV1[np.isnan(V1logV1)]=0.
S1logS1[np.isnan(S1logS1)]=0.
F1logF1[np.isnan(F1logF1)]=0.
C1logC1[np.isnan(C1logC1)]=0.

V1logVm = V1*np.log2(Vm)
S1logSm = S1*np.log2(Sm)
F1logFm = F1*np.log2(Fm)
C1logCm = C1*np.log2(Cm)
V1logVm[np.isnan(V1logVm)]=0.
S1logSm[np.isnan(S1logSm)]=0.
F1logFm[np.isnan(F1logFm)]=0.
C1logCm[np.isnan(C1logCm)]=0.

DKL1m = V1logV1 + S1logS1 + F1logF1 + C1logC1 - V1logVm - S1logSm - F1logFm - C1logCm
del V1logV1, S1logS1, F1logF1, C1logC1, V1logVm, S1logSm, F1logFm, C1logCm

V2logV2 = V2*np.log2(V2)
S2logS2 = S2*np.log2(S2)
F2logF2 = F2*np.log2(F2)
C2logC2 = C2*np.log2(C2)
V2logV2[np.isnan(V2logV2)]=0.
S2logS2[np.isnan(S2logS2)]=0.
F2logF2[np.isnan(F2logF2)]=0.
C2logC2[np.isnan(C2logC2)]=0.

V2logVm = V2*np.log2(Vm)
S2logSm = S2*np.log2(Sm)
F2logFm = F2*np.log2(Fm)
C2logCm = C2*np.log2(Cm)
V2logVm[np.isnan(V2logVm)]=0.
S2logSm[np.isnan(S2logSm)]=0.
F2logFm[np.isnan(F2logFm)]=0.
C2logCm[np.isnan(C2logCm)]=0.

DKL2m = V2logV2 + S2logS2 + F2logF2 + C2logC2 - V2logVm - S2logSm - F2logFm - C2logCm
del V2logV2, S2logS2, F2logF2, C2logC2, V2logVm, S2logSm, F2logFm, C2logCm

DJS = 1/2.*(DKL1m + DKL2m)

#Now make a example plot
imshow(DJS[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax], cmap="PuRd")
plt.show()