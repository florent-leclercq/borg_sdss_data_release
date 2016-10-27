==============================================
**BORG SDSS data products** / **borg_sdss_origami package**
==============================================

* *Authors*: Florent Leclercq, Jens Jasche, Guilhem Lavaux, Benjamin Wandelt
* *Last update*: 27-10-2016

----------------------
**File Contents**
----------------------

This package consists of four files:
* README.md
* borg_sdss_origami.npz, archived in a .tar.gz file available [here](http://icg.port.ac.uk/~leclercq/data/borg_sdss_origami.tar.gz)
* [borg_sdss_origami.py](borg_sdss_origami.py)
* [borg_sdss_origami.ipynb](borg_sdss_origami.ipynb)

**README.md**:
	This file contains the information you are currently reading.

**borg_sdss_origami.npz**:
	This file contains the maps obtained by [Leclercq et al. (2016a)](https://arxiv.org/abs/1601.00093), who performed a Bayesian analysis of the cosmic web in the SDSS volume. The results are four probabilistic maps of the voids, sheets, filaments, and clusters. Structures are defined using the ORIGAMI algorithm ([Falck et al. 2012](https://arxiv.org/abs/1201.2353)). Data are provided in terms of a standard 3D numpy array and can easily be accessed and processed with the open source Python programming language. For further details on the data and employed methods please consult the manuscript [Leclercq et al. (2016a)](https://arxiv.org/abs/1601.00093), of which the reference is provided below.

**[borg_sdss_origami.py](borg_sdss_origami.py)**:
	This file is an example script to be executed with the Python programming language. The script exemplifies loading and plotting the data contained in borg_sdss_origami.npz. This script can be used to reproduce figure 3 (bottom row) in [Leclercq et al. (2016a)](https://arxiv.org/abs/1601.00093).

**[borg_sdss_origami.ipynb](borg_sdss_origami.ipynb)**:
	This file is an example IPython notebook to load and plot the data in borg_sdss_origami.npz.

----------------------
**Usage**
----------------------

The file borg_sdss_origami.npz contains the probabilistic structure types maps in a standard uncompressed .npz format. To load and process the data with the Python programming language execute the following commands:

```python
import numpy as np
origami=np.load('borg_sdss_origami.npz')
```

To access the 3D structure maps use: 

```python
voids=origami['voids']
sheets=origami['sheets']
filaments=origami['filaments']
clusters=origami['clusters']
```

Individual voxels in this 3D volumetric data cube can be accessed as follows:

```python
voids_ijk=voids[k,j,i]
```

where i,j and k index voxel positions along the x,y and z axes respectively. All indices run from 0 to 255.

The ranges describing the extent of the cubic cartesian volume along the x,y and z axes can be accessed as follows:

```python
xmin=origami['ranges'][0]
xmax=origami['ranges'][1]

ymin=origami['ranges'][2]
ymax=origami['ranges'][3]

zmin=origami['ranges'][4]
zmax=origami['ranges'][5]
```
Units are Mpc/h.

(Note that all the maps that are part of the BORG SDSS data products have consistent consistent coordinate systems. The coordinate transform to change from Cartesian to spherical coordinates and vice versa is given in appendix B of [Jasche et al. 2015](https://arxiv.org/abs/1409.6308)).

A showcase of loading and plotting this data is provided by the files [borg_sdss_origami.py](borg_sdss_origami.py) and [borg_sdss_origami.ipynb](borg_sdss_origami.ipynb).

----------------------
**Credits**
----------------------

If you are using this data in your publications please cite the following publication:

> Leclercq, F. and Jasche, J. and Lavaux, G. and Wandelt, B. (2016a)<br />
> *Inference and classifications of the Lagrangian dark matter sheet in the SDSS*<br />
> [arXiv:1601.00093 [astro-ph.CO]](https://arxiv.org/abs/1601.00093)

As cosmic web analysis is a derived product of the BORG SDSS analysis, we also kindly ask you to cite the following publications:

> Jasche, J. and Wandelt, B. D. (2013)<br />
> *Bayesian physical reconstruction of initial conditions from large-scale structure surveys*<br />
> [Monthly Notices of the Royal Astronomical Society 432, 894-913 (2013)](http://dx.doi.org/10.1093/mnras/stt449)<br />
> [arXiv:1203.3639 [astro-ph.CO]](https://arxiv.org/abs/1203.3639)

and:

> Jasche, J. and Leclercq, F. and Wandelt, B. D. (2015)<br />
> *Past and present cosmic structure in the SDSS DR7 main sample*<br />
> [Journal of Cosmology and Astroparticle Physics 01, 036 (2015)](http://dx.doi.org/10.1088/1475-7516/2013/11/048)<br />
> [arXiv:1409.6308 [astro-ph.CO]](https://arxiv.org/abs/1409.6308)

as well as the 'ORIGAMI' paper:

> Falck, B. L. and Neyrinck, M. C. and Szalay, A. S. (2012)<br />
> *ORIGAMI: Delineating Halos Using Phase-space Folds*<br />
> [The Astrophysical Journal 754, 126 (2012)](http://dx.doi.org/10.1088/0004-637X/754/2/126)<br />
> [arXiv:1201.2353 [astro-ph.CO]](https://arxiv.org/abs/1201.2353)

We suggest, for example, the following sentence:
> 'This work uses the cosmic web maps obtained by Leclercq et al. (2016a), based on the ORIGAMI definition (Falck et al. 2012) and on the analysis of the SDSS (Jasche et al. 2015) by the BORG algorithm (Jasche & Wandelt 2013).'
