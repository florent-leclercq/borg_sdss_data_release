import numpy as np
from pylab import *
import warnings
warnings.filterwarnings("ignore")

# This script requires the npz files provided in the "borg_sdss_tweb", "borg_sdss_diva" and "borg_sdss_origami" packages of the BORG SDSS data release
tweb = np.load('borg_sdss_tweb.npz')
diva = np.load('borg_sdss_diva.npz')
origami = np.load('borg_sdss_origami.npz')

#Minimum and maximum position along the x-axis in Mpc/h
xmin=tweb['ranges'][0]
xmax=tweb['ranges'][1]

#Minimum and maximum position along the y-axis in Mpc/h
ymin=tweb['ranges'][2]
ymax=tweb['ranges'][3]

#Minimum and maximum position along the z-axis in Mpc/h
zmin=tweb['ranges'][4]
zmax=tweb['ranges'][5]

#3D probabilistic maps for structures
tweb_voids=tweb['voids']
tweb_sheets=tweb['sheets']
tweb_filaments=tweb['filaments']
tweb_clusters=tweb['clusters']
diva_voids=diva['voids']
diva_sheets=diva['sheets']
diva_filaments=diva['filaments']
diva_clusters=diva['clusters']
origami_voids=origami['voids']
origami_sheets=origami['sheets']
origami_filaments=origami['filaments']
origami_clusters=origami['clusters']

#Prior probabilities (numbers given in table III in Leclercq et al. 2016b)
prior_tweb_voids = 0.14261
prior_tweb_sheets = 0.59561
prior_tweb_filaments = 0.24980
prior_tweb_clusters = 0.01198
prior_diva_voids = 0.20216
prior_diva_sheets = 0.54845
prior_diva_filaments = 0.22587
prior_diva_clusters = 0.02352
prior_origami_voids = 0.89459
prior_origami_sheets = 0.06727
prior_origami_filaments = 0.02249
prior_origami_clusters = 0.01565

#Compute the Kullback-Leibler divergence
tweb_VlogV = tweb_voids*np.log2(tweb_voids)
tweb_SlogS = tweb_sheets*np.log2(tweb_sheets)
tweb_FlogF = tweb_filaments*np.log2(tweb_filaments)
tweb_ClogC = tweb_clusters*np.log2(tweb_clusters)
tweb_VlogV[np.isnan(tweb_VlogV)]=0.
tweb_SlogS[np.isnan(tweb_SlogS)]=0.
tweb_FlogF[np.isnan(tweb_FlogF)]=0.
tweb_ClogC[np.isnan(tweb_ClogC)]=0.

tweb_VlogPrior_V = tweb_voids*np.log2(prior_tweb_voids)
tweb_SlogPrior_S = tweb_sheets*np.log2(prior_tweb_sheets)
tweb_FlogPrior_F = tweb_filaments*np.log2(prior_tweb_filaments)
tweb_ClogPrior_C = tweb_clusters*np.log2(prior_tweb_clusters)

tweb_DKL = tweb_VlogV + tweb_SlogS + tweb_FlogF + tweb_ClogC - tweb_ClogPrior_C - tweb_SlogPrior_S - tweb_FlogPrior_F - tweb_VlogPrior_V
del tweb_VlogV, tweb_SlogS, tweb_FlogF, tweb_ClogC, tweb_ClogPrior_C, tweb_SlogPrior_S, tweb_FlogPrior_F, tweb_VlogPrior_V

diva_VlogV = diva_voids*np.log2(diva_voids)
diva_SlogS = diva_sheets*np.log2(diva_sheets)
diva_FlogF = diva_filaments*np.log2(diva_filaments)
diva_ClogC = diva_clusters*np.log2(diva_clusters)
diva_VlogV[np.isnan(diva_VlogV)]=0.
diva_SlogS[np.isnan(diva_SlogS)]=0.
diva_FlogF[np.isnan(diva_FlogF)]=0.
diva_ClogC[np.isnan(diva_ClogC)]=0.

diva_VlogPrior_V = diva_voids*np.log2(prior_diva_voids)
diva_SlogPrior_S = diva_sheets*np.log2(prior_diva_sheets)
diva_FlogPrior_F = diva_filaments*np.log2(prior_diva_filaments)
diva_ClogPrior_C = diva_clusters*np.log2(prior_diva_clusters)

diva_DKL = diva_VlogV + diva_SlogS + diva_FlogF + diva_ClogC - diva_ClogPrior_C - diva_SlogPrior_S - diva_FlogPrior_F - diva_VlogPrior_V
del diva_VlogV, diva_SlogS, diva_FlogF, diva_ClogC, diva_ClogPrior_C, diva_SlogPrior_S, diva_FlogPrior_F, diva_VlogPrior_V

origami_VlogV = origami_voids*np.log2(origami_voids)
origami_SlogS = origami_sheets*np.log2(origami_sheets)
origami_FlogF = origami_filaments*np.log2(origami_filaments)
origami_ClogC = origami_clusters*np.log2(origami_clusters)
origami_VlogV[np.isnan(origami_VlogV)]=0.
origami_SlogS[np.isnan(origami_SlogS)]=0.
origami_FlogF[np.isnan(origami_FlogF)]=0.
origami_ClogC[np.isnan(origami_ClogC)]=0.

origami_VlogPrior_V = origami_voids*np.log2(prior_origami_voids)
origami_SlogPrior_S = origami_sheets*np.log2(prior_origami_sheets)
origami_FlogPrior_F = origami_filaments*np.log2(prior_origami_filaments)
origami_ClogPrior_C = origami_clusters*np.log2(prior_origami_clusters)

origami_DKL = origami_VlogV + origami_SlogS + origami_FlogF + origami_ClogC - origami_ClogPrior_C - origami_SlogPrior_S - origami_FlogPrior_F - origami_VlogPrior_V
del origami_VlogV, origami_SlogS, origami_FlogF, origami_ClogC, origami_ClogPrior_C, origami_SlogPrior_S, origami_FlogPrior_F, origami_VlogPrior_V

#Now make a example plot
imshow(origami_DKL[:,:,128], origin='lower', extent=[ymin,ymax,zmin,zmax], cmap="gist_earth_r")
plt.show()