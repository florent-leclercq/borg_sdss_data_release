==============================================
**BORG SDSS data products** / **borg_sdss_diva package**
==============================================

* *Authors*: Florent Leclercq, Jens Jasche, Guilhem Lavaux, Benjamin Wandelt
* *Last update*: 27-10-2016

----------------------
**File Contents**
----------------------

This package consists of four files:
* README.md
* borg_sdss_diva.npz, archived in a .tar.gz file available [here](http://icg.port.ac.uk/~leclercq/data/borg_sdss_diva.tar.gz)
* [borg_sdss_diva.py](borg_sdss_diva.py)
* [borg_sdss_diva.ipynb](borg_sdss_diva.ipynb)

**README.md**:
	This file contains the information you are currently reading.

**borg_sdss_diva.npz**:
	This file contains the maps obtained by Leclercq et al. (2016a), who performed a Bayesian analysis of the cosmic web in the SDSS volume. The results are four probabilistic maps of the voids, sheets, filaments, and clusters. Structures are defined using the DIVA algorithm ([Lavaux & Wandelt 2010](https://arxiv.org/abs/0906.4101)). Data are provided in terms of a standard 3D numpy array and can easily be accessed and processed with the open source Python programming language. For further details on the data and employed methods please consult the manuscript [Leclercq et al. (2016a)](https://arxiv.org/abs/1601.00093), of which the reference is provided below.

**[borg_sdss_diva.py](borg_sdss_diva.py)**:
	This file is an example script to be executed with the Python programming language. The script exemplifies loading and plotting the data contained in borg_sdss_diva.npz. This script can be used to reproduce figure 8 (top row) in [Leclercq et al. (2016a)](https://arxiv.org/abs/1601.00093).

**[borg_sdss_diva.ipynb](borg_sdss_diva.ipynb)**:
	This file is an example IPython notebook to load and plot the data in borg_sdss_diva.npz.

----------------------
**Usage**
----------------------

The file borg_sdss_diva.npz contains the probabilistic structure types maps in a standard uncompressed .npz format. To load and process the data with the Python programming language execute the following commands:

```python
import numpy as np
diva=np.load('borg_sdss_diva.npz')
```

To access the 3D structure maps use: 

```python
voids=diva['voids']
sheets=diva['sheets']
filaments=diva['filaments']
clusters=diva['clusters']
```

Individual voxels in this 3D volumetric data cube can be accessed as follows:

```python
voids_ijk=voids[k,j,i]
```

where i,j and k index voxel positions along the x,y and z axes respectively. All indices run from 0 to 255.

The ranges describing the extent of the cubic cartesian volume along the x,y and z axes can be accessed as follows:

```python
xmin=diva['ranges'][0]
xmax=diva['ranges'][1]

ymin=diva['ranges'][2]
ymax=diva['ranges'][3]

zmin=diva['ranges'][4]
zmax=diva['ranges'][5]
```
Units are Mpc/h.

(Note that all the maps that are part of the BORG SDSS data products have consistent consistent coordinate systems. The coordinate transform to change from Cartesian to spherical coordinates and vice versa is given in appendix B of [Jasche et al. 2015](https://arxiv.org/abs/1409.6308)).

A showcase of loading and plotting this data is provided by the files [borg_sdss_diva.py](borg_sdss_diva.py) and [borg_sdss_diva.ipynb](borg_sdss_diva.ipynb).

----------------------
**Credits**
----------------------

If you are using this data in your publications please cite the
following publication:

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

as well as the 'DIVA' paper:

> Lavaux, G. and Wandelt, B. D. (2010)
> *Precision cosmology with voids: definition, methods, dynamics*<br />
> [Monthly Notices of the Royal Astronomical Society 403, 1392-1408 (2010)](http://dx.doi.org/10.1111/j.1365-2966.2010.16197.x)<br />
> [arXiv:0906.4101 [astro-ph.CO]](https://arxiv.org/abs/0906.4101)

We suggest, for example, the following sentence:
> 'This work uses the cosmic web maps obtained by Leclercq et al. (2016a), based on the DIVA definition (Lavaux & Wandelt 2010) and on the analysis of the SDSS (Jasche et al. 2015) by the BORG algorithm (Jasche & Wandelt 2013).'
