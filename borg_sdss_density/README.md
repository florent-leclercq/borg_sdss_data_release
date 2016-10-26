==============================================
**BORG SDSS data products**
==============================================
**borg_sdss_density**

* *Authors*: Jens Jasche, Florent Leclercq, Benjamin Wandelt
* *Last update*: 26-10-2016

----------------------
**File Contents**
----------------------

Including this file you should have received a copy of in total four files:
* README.md
* borg_sdss_density.npz
* borg_sdss_density.py
* borg_sdss_density.ipynb

README.md	:
	This file contains the information you are currently reading.

borg_sdss_density.npz	:
	This file contains some of the results obtained by Jasche et al. (2015), who performed
	a fully Bayesian analysis of the 3D large scale structure as traced by SDSS main
	sample galaxies. In particular it contains the ensemble mean density contrast for the
	observed present day large scale structure in terms of a 3D volumetric data cube.
	Data is provided in terms of a standard 3D numpy array and can easily be accessed and
	processed with the open source Python programming language. The file further provides an
	additional 3D numpy array with corresponding uncertainty quantification in terms of 
	voxel-wise standard deviations. For further details on the data and employed inference
	methodologies please consult the manuscript Jasche et al. (2015), of which the reference
	is provided below.

borg_sdss_density.py	:
	This file is an example script to be executed with the Python programming language.
	The script exemplifies loading and plotting the data contained in borg_sdss_density.npz.

borg_sdss_density.ipynb	:
	This file is an example IPython notebook to load and plot the data.

----------------------
**Usage**
----------------------

The file borg_sdss_density.npz contains inferred large scale structure data in a standard uncompressed .npz format.
To load and process the data with the Python programming language execute the following commands:

>>> import numpy as np
>>> data=np.load('borg_sdss_density.npz')

To access the 3D ensemble mean final density contrast use: 

>>> mean=data['mean']

Individual voxels in this 3D volumetric data cube can be accessed as follows:

>>> delta_ijk=mean[k,j,i],

where i,j and k index voxel positions along the x,y and z axes respectively.
All indices run from 0 to 255.

Similarly, to access voxel-wise standard deviations use: 

>>> stdv=data['stdv']

Individual voxels of this 3D volumetric data cube can be accessed as described above.

The ranges describing the extent of the cubic cartesian volume along
the x,y and z axes can be accessed as follows:

>>> xmin=data['ranges'][0]
>>> xmax=data['ranges'][1]

>>> ymin=data['ranges'][2]
>>> ymax=data['ranges'][3]

>>> zmin=data['ranges'][4]
>>> zmax=data['ranges'][5]

Units are Mpc/h.

(Note, the coordinate transform to change from Cartesian to spherical
coordinates and vice versa is given in appendix B of Jasche et al. 2015)

A showcase of loading and plotting this data is provided by the file example.py,
a copy of which you should have received along with this file.

----------------------
**Credits**
----------------------

If you are using this data in your publications please cite the
following publications:

	Jasche, J. and Wandelt, B. D. (2013)
	Bayesian physical reconstruction of initial conditions from large-scale structure surveys
	Monthly Notices of the Royal Astronomical Society 432, 894-913 (2013)
	arXiv:1203.3639 [astro-ph.CO]

and:

	Jasche, J. and Leclercq, F. and Wandelt, B. D. (2015)
	Past and present cosmic structure in the SDSS DR7 main sample
	Journal of Cosmology and Astroparticle Physics 01, 036 (2015)
	arXiv:1409.6308 [astro-ph.CO]
