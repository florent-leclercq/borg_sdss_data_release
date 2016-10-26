==============================================
BORG SDSS data products
==============================================

:Authors: Florent Leclercq, Jens Jasche, Benjamin Wandelt
:Last update: 16-06-2016

----------------------
File Contents
----------------------

Including this file you should have received a copy of in total six files:

		README.rst

		borg_sdss_tweb.npz

		example.py

		entropy_tweb.py

		kullback-leibler_tweb.py

		decision_tweb.py


README.rst		:This file contains the information you are currently reading.

borg_sdss_tweb.npz	:This file contains the maps obtained by Leclercq et al. (2015a), who performed
			 a Bayesian analysis of the cosmic web in the SDSS volume. The results are four
			 probabilistic maps of the voids, sheets, filaments, and clusters.
			 Structures are defined using the T-web algorithm (Hahn et al. 2007)
			 Data is provided in terms of a standard 3D numpy array and can easily be accessed and
			 processed with the open source Python programming language. For further details on
			 the data and employed methods please consult the manuscript Leclercq et al. (2015a),
			 of which the reference is provided below.

example.py		:This file is an example script to be executed with the Python programming language.
			 The script exemplifies loading and plotting the data contained in borg_sdss_tweb.npz.
			 This script can be used to reproduce figure 3 in Leclercq et al. (2015a).

entropy_tweb.py		:This file is an example script to be executed with the Python programming language.
			 The script shows how to compute the three-dimensional entropy of the structure types
			 posterior, and can be used to reproduce figure 4 (left) in Leclercq et al. (2015a).

kullback-leibler_tweb.py:This file is an example script to be executed with the Python programming language.
			 The script shows how to compute the three-dimensional information gain on structure types,
			 and can be used to reproduce figure 4 (right) in Leclercq et al. (2015a).

decision_tweb.py	:This file is an example script to be executed with the Python programming language.
			 The script shows how to implement the formalism described in Leclercq et al. (2015b)
			 and can be used to reproduce figure 1 in Leclercq et al. (2015b).

----------------------
Usage
----------------------

The file borg_sdss_tweb.npz contains the probabilistic structure types maps in a standard uncompressed .npz format.
To load and process the data with the Python programming language execute the following commands:

		import numpy as np
		tweb=np.load('borg_sdss_tweb.npz')

To access the 3D structure maps use: 

		voids=tweb['voids']
		sheets=tweb['sheets']
		filaments=tweb['filaments']
		clusters=tweb['clusters']

Individual voxels in this 3D volumetric data cube can be accessed as follows:

		voids_ijk=voids[k,j,i],

where i,j and k index voxel positions along the x,y and z axes respectively.
All indices run from 0 to 255.

The ranges describing the extent of the cubic cartesian volume along
the x,y and z axes can be accessed as follows:

		xmin=tweb['ranges'][0]
		xmax=tweb['ranges'][1]

		ymin=tweb['ranges'][2]
		ymax=tweb['ranges'][3]

		zmin=tweb['ranges'][4]
		zmax=tweb['ranges'][5]

Units are Mpc/h.

(Note that all the maps that are part of the BORG SDSS data products have consistent consistent
coordinate systems. The coordinate transform to change from Cartesian to spherical coordinates
and vice versa is given in appendix B of Jasche et al. 2015)

A showcase of loading and plotting this data is provided by the file example.py,
a copy of which you should have received along with this file.

----------------------
Credits
----------------------

If you are using this data in your publications please cite the
following publication:

	Leclercq, F. and Jasche, J. and Wandelt, B. (2015a)
	Bayesian analysis of the dynamic cosmic web in the SDSS galaxy survey
	Journal of Cosmology and Astroparticle Physics 06, 015 (2015)
	arXiv:1502.02690 [astro-ph.CO]

As cosmic web analysis is a derived product of the BORG SDSS analysis, we also kindly
ask you to cite the following publications:

	Jasche, J. and Wandelt, B. D. (2013)
	Bayesian physical reconstruction of initial conditions from large-scale structure surveys
	Monthly Notices of the Royal Astronomical Society 432, 894-913 (2013)
	arXiv:1203.3639 [astro-ph.CO]

and:

	Jasche, J. and Leclercq, F. and Wandelt, B. D. (2015)
	Past and present cosmic structure in the SDSS DR7 main sample
	Journal of Cosmology and Astroparticle Physics 01, 036 (2015)
	arXiv:1409.6308 [astro-ph.CO]

as well as the 'T-web' paper:

	Hahn, O. and Porciani, C. and Carollo, C. M. and Dekel, A. (2007)
	Properties of dark matter haloes in clusters, filaments, sheets and voids
	Monthly Notices of the Royal Astronomical Society 375, 489-499 (2007)
	arXiv:astro-ph/0610280

If you use the decision theory formalism (in the file decision_tweb.py, for example),
please cite the following publication:

	Leclercq, F. and Jasche, J. and Wandelt, B. (2015b)
	Cosmic web-type classification using decision theory
	Astronomy & Astrophysics Letters, 576, L17 (2015)
	arXiv:1503.00730 [astro-ph.CO]

We suggest, for example, the following sentences:
'This work uses the cosmic web maps obtained by Leclercq et al. (2015a), based on the T-web definition (Hahn et al. 2007)
and on the analysis of the SDSS (Jasche et al. 2015) by the BORG algorithm (Jasche & Wandelt 2013).'

'This work uses the formalism introduced by Leclercq et al. (2015b) for cosmic web classification using decision theory.'
