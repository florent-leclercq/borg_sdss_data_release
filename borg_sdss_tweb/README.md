==============================================
**BORG SDSS data products** / **borg_sdss_tweb package**
==============================================

* *Authors*: Florent Leclercq, Jens Jasche, Benjamin Wandelt
* *Last update*: 26-10-2016

----------------------
**File Contents**
----------------------

This package consists of seven files:
* README.rst
* borg_sdss_tweb.npz, archived in a .tar.gz file available [here](http://icg.port.ac.uk/~leclercq/data/borg_sdss_tweb.tar.gz)
* [borg_sdss_tweb.py](borg_sdss_tweb.py)
* [borg_sdss_tweb.ipynb](borg_sdss_tweb.ipynb)
* [entropy_tweb.py](entropy_tweb.py)
* [kullback-leibler_tweb.py](kullback-leibler_tweb.py)
* [decision_tweb.py](decision_tweb.py)

**README.md**:
	This file contains the information you are currently reading.

**borg_sdss_tweb.npz**:
	This file contains the maps obtained by [Leclercq et al. (2015a)](https://arxiv.org/abs/1502.02690), who performed a Bayesian analysis of the cosmic web in the SDSS volume. The results are four probabilistic maps of the voids, sheets, filaments, and clusters. Structures are defined using the T-web algorithm ([Hahn et al. 2007](https://arxiv.org/abs/astro-ph/0610280)). Data are provided in terms of a standard 3D numpy array and can easily be accessed and processed with the open source Python programming language. For further details on the data and employed methods please consult the manuscript [Leclercq et al. (2015a)](https://arxiv.org/abs/1502.02690), of which the reference is provided below.

**[borg_sdss_tweb.py](borg_sdss_tweb.py)**:
	This file is an example script to be executed with the Python programming language. The script exemplifies loading and plotting the data contained in borg_sdss_tweb.npz. This script can be used to reproduce figure 3 in [Leclercq et al. (2015a)](https://arxiv.org/abs/1502.02690).

**[borg_sdss_tweb.ipynb](borg_sdss_tweb.ipynb)**:
	This file is an example IPython notebook to load and plot the data, compute and plot the entropy and the information gain, and implement the decision theory framework of [Leclercq et al. (2015b)](https://arxiv.org/abs/1503.00730) (all the content of the Python scripts).

**[entropy_tweb.py](entropy_tweb.py)**:
	This file is an example script to be executed with the Python programming language. The script shows how to compute the three-dimensional entropy of the structure types posterior, and can be used to reproduce figure 4 (left) in [Leclercq et al. (2015a)](https://arxiv.org/abs/1502.02690).

**[kullback-leibler_tweb.py](kullback-leibler_tweb.py)**:
	This file is an example script to be executed with the Python programming language. The script shows how to compute the three-dimensional information gain on structure types, and can be used to reproduce figure 4 (right) in [Leclercq et al. (2015a)](https://arxiv.org/abs/1502.02690).

**[decision_tweb.py](decision_tweb.py)**:
	This file is an example script to be executed with the Python programming language. The script shows how to implement the formalism described in [Leclercq et al. (2015b)](https://arxiv.org/abs/1503.00730) and can be used to reproduce figure 1 in [Leclercq et al. (2015b)](https://arxiv.org/abs/1503.00730).

----------------------
**Usage**
----------------------

The file borg_sdss_tweb.npz contains the probabilistic structure types maps in a standard uncompressed .npz format. To load and process the data with the Python programming language execute the following commands:

```python
import numpy as np
tweb=np.load('borg_sdss_tweb.npz')
```

To access the 3D structure maps use: 

```python
voids=tweb['voids']
sheets=tweb['sheets']
filaments=tweb['filaments']
clusters=tweb['clusters']
```

Individual voxels in this 3D volumetric data cube can be accessed as follows:

```python
voids_ijk=voids[k,j,i]
```

where i,j and k index voxel positions along the x,y and z axes respectively. All indices run from 0 to 255.

The ranges describing the extent of the cubic cartesian volume along the x,y and z axes can be accessed as follows:

```python
xmin=tweb['ranges'][0]
xmax=tweb['ranges'][1]

ymin=tweb['ranges'][2]
ymax=tweb['ranges'][3]

zmin=tweb['ranges'][4]
zmax=tweb['ranges'][5]
```

Units are Mpc/h.

(Note that all the maps that are part of the BORG SDSS data products have consistent consistent coordinate systems. The coordinate transform to change from Cartesian to spherical coordinates and vice versa is given in appendix B of [Jasche et al. 2015](https://arxiv.org/abs/1409.6308)).

A showcase of loading and plotting this data is provided by the files [borg_sdss_tweb.py](borg_sdss_tweb.py) and [borg_sdss_tweb.ipynb](borg_sdss_tweb.ipynb).

----------------------
**Credits**
----------------------

If you are using this data in your publications please cite the
following publication:

> Leclercq, F. and Jasche, J. and Wandelt, B. (2015a)<br />
> *Bayesian analysis of the dynamic cosmic web in the SDSS galaxy survey*<br />
> [Journal of Cosmology and Astroparticle Physics 06, 015 (2015)](http://dx.doi.org/10.1088/1475-7516/2015/06/015)<br />
> [arXiv:1502.02690 [astro-ph.CO]](https://arxiv.org/abs/1502.02690)

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

as well as the 'T-web' paper:

> Hahn, O. and Porciani, C. and Carollo, C. M. and Dekel, A. (2007)<br />
> *Properties of dark matter haloes in clusters, filaments, sheets and voids*<br />
> [Monthly Notices of the Royal Astronomical Society 375, 489-499 (2007)](http://dx.doi.org/10.1111/j.1365-2966.2006.11318.x)<br />
> [arXiv:astro-ph/0610280](https://arxiv.org/abs/astro-ph/0610280)

If you use the decision theory formalism (in the file [decision_tweb.py](decision_tweb.py), for example), please cite the following publication:

> Leclercq, F. and Jasche, J. and Wandelt, B. (2015b)<br />
> *Cosmic web-type classification using decision theory*<br />
> [Astronomy & Astrophysics Letters, 576, L17 (2015)](http://dx.doi.org/10.1051/0004-6361/201526006)<br />
> [arXiv:1503.00730 [astro-ph.CO]](https://arxiv.org/abs/1503.00730)

We suggest, for example, the following sentences:
> 'This work uses the cosmic web maps obtained by Leclercq et al. (2015a), based on the T-web definition (Hahn et al. 2007) and on the analysis of the SDSS (Jasche et al. 2015) by the BORG algorithm (Jasche & Wandelt 2013).'

> 'This work uses the formalism introduced by Leclercq et al. (2015b) for cosmic web classification using decision theory.'
