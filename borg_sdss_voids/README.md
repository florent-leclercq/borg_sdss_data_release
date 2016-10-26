==============================================
**BORG SDSS data products** / **borg_sdss_voids package**
==============================================

* *Authors*: Florent Leclercq, Jens Jasche, P.M. Sutter, Nico Hamaus, Benjamin Wandelt
* *Last update*: 26-10-2016

----------------------
**File Contents**
----------------------

This package consists of 73 files:
* README.md
* 1dprofile_*.dat.npz (6 files)
* masked3D_untrimmed_centers_central_constrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_centers_central_unconstrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_shapes_central_constrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_shapes_central_unconstrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_sky_positions_central_constrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_sky_positions_central_unconstrained_*_ss1.0_z0.00_d00.out (11 files)

All these files are archived in a .tar.gz file available [here](http://icg.port.ac.uk/~leclercq/data/borg_sdss_voids.tar.gz). Only README.md is available in the GitHub repository.

**README.md**:
	This file contains the information you are currently reading.

**1dprofile_*.dat.npz**:
	These file contain the 1d density profiles of dark matter voids in the SDSS, that permit 	to reproduce figure 6 in [Leclercq et al. (2015)](https://arxiv.org/abs/1410.0355). Data are provided in terms of a standard 3D numpy array and can easily be accessed and processed with the open source Python programming language. For further details on the data and employed methods please consult [Leclercq et al. (2015)](https://arxiv.org/abs/1410.0355) and the [VIDE paper](https://arxiv.org/abs/1406.1191), of which the references are provided below.

**masked3D_untrimmed_centers_central_constrained_*_ss1.0_z0.00_d00.out**:
	These file contain information on void centers for the 11 constrained realizations of dark matter voids in the SDSS. Please refer to the header of these files for documentation.

**masked3D_untrimmed_centers_central_unconstrained_*_ss1.0_z0.00_d00.out**:
	These file contain information on void centers for 11 unconstrained realizations with corresponding setup. Please refer to the header of these files for documentation.

**masked3D_untrimmed_shapes_central_constrained_*_ss1.0_z0.00_d00.out**:
	These file contain information on void shapes for the 11 constrained realizations of dark matter voids in the SDSS. Please refer to the header of these files for documentation.

**masked3D_untrimmed_shapes_central_unconstrained_*_ss1.0_z0.00_d00.out**:
	These file contain information on void shapes for 11 unconstrained realizations with corresponding setup. Please refer to the header of these files for documentation.

**masked3D_untrimmed_sky_positions_central_constrained_*_ss1.0_z0.00_d00.out**:
	These file contain information on void sky positions for the 11 constrained realizations of dark matter voids in the SDSS. Please refer to the header of these files for documentation.

**masked3D_untrimmed_sky_positions_central_unconstrained_*_ss1.0_z0.00_d00.out**:
	These file contain information on void sky positions for 11 unconstrained realizations with corresponding setup. Please refer to the header of these files for documentation.

----------------------
**Credits**
----------------------

If you are using this material in your publications please cite the
following publications:

> Leclercq, F. and Jasche, J. and Sutter, P.M. and Hamaus, N. and Wandelt, B. (2015)<br />
> *Dark matter voids in the SDSS galaxy survey*<br />
> [Journal of Cosmology and Astroparticle Physics 03, 047 (2015)](http://dx.doi.org/10.1088/1475-7516/2015/03/047)<br />
> [arXiv:1410.0355 [astro-ph.CO]](https://arxiv.org/abs/1410.0355)

> Sutter, P.M. and Lavaux, G. and Wandelt, B.D. and Weinberg, D.H. (2012)<br />
> *A public void catalog from the SDSS DR7 Galaxy Redshift Surveys based on the watershed transform*<br />
> [The Astrophysical Journal 761, 44 (2012)](http://dx.doi.org/10.1088/0004-637X/761/1/44)<br />
> [arXiv:1207.2524 [astro-ph.CO]](https://arxiv.org/abs/1207.2524)

As cosmic web analysis is a derived product of the BORG SDSS analysis, we also kindly
ask you to cite the following publications:

> Jasche, J. and Wandelt, B. D. (2013)<br />
> *Bayesian physical reconstruction of initial conditions from large-scale structure surveys*<br />
> [Monthly Notices of the Royal Astronomical Society 432, 894-913 (2013)](http://dx.doi.org/10.1093/mnras/stt449)<br />
> [arXiv:1203.3639 [astro-ph.CO]](https://arxiv.org/abs/1203.3639)

and:

> Jasche, J. and Leclercq, F. and Wandelt, B. D. (2015)<br />
> *Past and present cosmic structure in the SDSS DR7 main sample*<br />
> [Journal of Cosmology and Astroparticle Physics 01, 036 (2015)](http://dx.doi.org/10.1088/1475-7516/2013/11/048)<br />
> [arXiv:1409.6308 [astro-ph.CO]](https://arxiv.org/abs/1409.6308)
