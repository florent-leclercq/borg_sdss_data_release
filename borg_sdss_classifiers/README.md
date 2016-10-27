==============================================
**BORG SDSS data products** / **borg_sdss_classifiers package**
==============================================

* *Authors*: Florent Leclercq, Guilhem Lavaux, Jens Jasche, Benjamin Wandelt
* *Last update*: 27-10-2016

----------------------
**File Contents**
----------------------

This package consists of eight files:
* README.md
* borg_sdss_js_DE.npz
* galaxy_catalog.dat
* [kullback-leibler.py](kullback-leibler.py)
* [jensen-shannon_diva-origami.py](jensen-shannon_diva-origami.py)
* [jensen-shannon_DE.py](jensen-shannon_DE.py)
* [information_gain_galaxies.py](information_gain_galaxies.py)
* [borg_sdss_classifiers.ipynb](borg_sdss_classifiers.ipynb)

The files borg_sdss_js_DE.npz and galaxy_catalog.dat are archived in a .tar.gz file available [here](http://icg.port.ac.uk/~leclercq/data/borg_sdss_classifiers.tar.gz).

**README.md**:
	This file contains the information you are currently reading.

**borg_sdss_js_DE.npz**:
	This file contains some of the maps obtained by [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758), who performed an information-theoretic comparison of cosmic web classifiers. The results are three maps of the Jensen-Shannon divergence between cosmic web-type posteriors for different dark energy models (w=-0.9, w=-1, w=-1.1). Structures are defined using the T-web ([Hahn et al. 2007](https://arxiv.org/abs/astro-ph/0610280)), DIVA ([Lavaux & Wandelt 2010](https://arxiv.org/abs/0906.4101)), or ORIGAMI ([Falck et al. 2012](https://arxiv.org/abs/1201.2353)) algorithms. Data are provided in terms of a standard 3D numpy array and can easily be accessed and processed with the open source Python programming language. For further details on the data and employed methods please consult the manuscript [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758), of which the reference is provided below.

jensen-shannon_DE.py		:This file is an example script to be executed with the Python programming language.
				 The script exemplifies loading and plotting the data contained in borg_sdss_js_DE.npz.
				 This script can be used to reproduce the results of section III.B and figure 5 in [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758).

kullback-leibler.py		:This file is an example script to be executed with the Python programming language.
				 This script requires the files borg_sdss_tweb.npz, borg_sdss_diva.npz and borg_sdss_origami.npz, available
				 from their respective packages of the BORG SDSS data release.
				 The script shows how to compute the three-dimensional information gain on structure types,
				 and can be used to reproduce the results of section III.A and figure 3 in [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758).

jensen-shannon_diva-origami.py	:This file is an example script to be executed with the Python programming language.
				 This script requires the files borg_sdss_diva.npz and borg_sdss_origami.npz, available
				 from their respective packages of the BORG SDSS data release.
				 The script shows how to compute the three-dimensional Jenssen-Shannon divergence between pairs of cosmic
				 web-type posteriors, and can be used to reproduce figure 4 in [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758).

galaxy_catalog.dat		:This file contains the galaxy catalog used in section III.C of [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758).
				 Please see the header of this file for documentation.
				 This catalog can be used to reproduce figure 6 of [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758), using also the decision theory
				 criterion of [Leclercq et al. (2015b)](https://arxiv.org/abs/1503.00730). In particular, please refer to the file decision_tweb.py
				 in the 'borg_sdss_tweb' package of the BORG SDSS data release.

information_gain_galaxies.py	:This file is an example script to be executed with the Python programming language.
				 This script analyzes the galaxy catalog (in particular computing the information gain on color
				 once the environmental cosmic web-type is know). It can be used to reproduce the results 
				 of section III.C of [Leclercq et al. (2016b)](https://arxiv.org/abs/1606.06758), in particular table VI and the utility U3 given in table IV.

----------------------
Credits
----------------------

If you are using this material in your publications please cite the
following publication:

	Leclercq, F. and Lavaux, G. and Jasche, J. and Wandelt, B. (2016b)
	Comparing cosmic web classifiers using information theory
	arXiv:1606:XXXXX [astro-ph.CO]

For a publication using the 'T-web' maps, please cite

	Leclercq, F. and Jasche, J. and Wandelt, B. (2015a)
	Bayesian analysis of the dynamic cosmic web in the SDSS galaxy survey
	Journal of Cosmology and Astroparticle Physics 06, 015 (2015)
	arXiv:1502.02690 [astro-ph.CO]

as well as the 'T-web' paper:

	Hahn, O. and Porciani, C. and Carollo, C. M. and Dekel, A. (2007)
	Properties of dark matter haloes in clusters, filaments, sheets and voids
	Monthly Notices of the Royal Astronomical Society 375, 489-499 (2007)
	arXiv:astro-ph/0610280

For a publication using the 'DIVA' or 'ORIGAMI' maps, please cite

	Leclercq, F. and Jasche, J. and Lavaux, G. and Wandelt, B. (2016a)
	Inference and classifications of the Lagrangian dark matter sheet in the SDSS
	arXiv:1601.00093 [astro-ph.CO]

as well as the 'DIVA' and/or 'ORIGAMI' papers:

	Lavaux, G. and Wandelt, B. D. (2010)
	Precision cosmology with voids: definition, methods, dynamics
	Monthly Notices of the Royal Astronomical Society 403, 1392-1408 (2010)
	arXiv:0906.4101 [astro-ph.CO]

	Falck, B. L. and Neyrinck, M. C. and Szalay, A. S. (2012)
	ORIGAMI: Delineating Halos Using Phase-space Folds
	The Astrophysical Journal 754, 126 (2012)
	arXiv:1201.2353 [astro-ph.CO]

If you use the decision theory formalism (in the file decision_tweb.py of the borg_sdss_tweb package, for example),
please cite the following publication:

	Leclercq, F. and Jasche, J. and Wandelt, B. (2015b)
	Cosmic web-type classification using decision theory
	Astronomy & Astrophysics Letters, 576, L17 (2015)
	arXiv:1503.00730 [astro-ph.CO]

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

We suggest, for example, the following sentences:
'This work uses material from the cosmic web classifiers comparison project performed by Leclercq et al. (2016b) and
the maps obtained by Leclercq et al. (2015a) & Leclercq et al. (2016a). These maps are based on the
T-web (Hahn et al. 2007), DIVA (Lavaux & Wandelt 2010) and ORIGAMI (Falck et al. 2012) definitions. They
build upon the analysis of the SDSS (Jasche et al. 2015) by the BORG algorithm (Jasche & Wandelt 2013).'

'This work uses the formalism introduced by Leclercq et al. (2015b) for cosmic web classification using decision theory.'
