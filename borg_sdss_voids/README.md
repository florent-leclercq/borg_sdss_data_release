==============================================
**BORG SDSS data products**
==============================================

*Authors*: Florent Leclercq, Jens Jasche, P.M. Sutter, Nico Hamaus, Benjamin Wandelt
*Last update*: 26-10-2016

----------------------
**File Contents**
----------------------

Including this file you should have received a copy of in total 73 files:
* README.md
* 1dprofile_*.dat.npz (6 files)
* masked3D_untrimmed_centers_central_constrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_centers_central_unconstrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_shapes_central_constrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_shapes_central_unconstrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_sky_positions_central_constrained_*_ss1.0_z0.00_d00.out (11 files)
* masked3D_untrimmed_sky_positions_central_unconstrained_*_ss1.0_z0.00_d00.out (11 files)

README.md	:
	This file contains the information you are currently reading.

1dprofile_*.dat.npz	:
	These file contain the 1d density profiles of dark matter voids in the SDSS, that permit
	to reproduce figure 6 in Leclercq et al. (2015)
	Data is provided in terms of a standard 3D numpy array and can easily be accessed and
	processed with the open source Python programming language. For further details on
	the data and employed methods please consult Leclercq et al. (2015) and the VIDE paper,
	of which the references are provided below.

masked3D_untrimmed_centers_central_constrained_*_ss1.0_z0.00_d00.out	:
	These file contain information on void centers for the 
	11 constrained realizations of dark matter voids in the SDSS.
	Please see the header of these files for documentation.

masked3D_untrimmed_centers_central_unconstrained_*_ss1.0_z0.00_d00.out	:
	These file contain information on void centers for 
	11 unconstrained realizations with corresponding setup.
	Please see the header of these files for documentation.

masked3D_untrimmed_shapes_central_constrained_*_ss1.0_z0.00_d00.out	:
	These file contain information on void shapes for the 
	11 constrained realizations of dark matter voids in the SDSS.
	Please see the header of these files for documentation.

masked3D_untrimmed_shapes_central_unconstrained_*_ss1.0_z0.00_d00.out	:
	These file contain information on void shapes for 
	11 unconstrained realizations with corresponding setup.
	Please see the header of these files for documentation.

masked3D_untrimmed_sky_positions_central_constrained_*_ss1.0_z0.00_d00.out	:
	These file contain information on void sky positions for the 
	11 constrained realizations of dark matter voids in the SDSS.
	Please see the header of these files for documentation.

masked3D_untrimmed_sky_positions_central_unconstrained_*_ss1.0_z0.00_d00.out	:
	These file contain information on void sky positions for 
	11 unconstrained realizations with corresponding setup.
	Please see the header of these files for documentation.

----------------------
**Credits**
----------------------

If you are using this material in your publications please cite the
following publications:

	Leclercq, F. and Jasche, J. and Sutter, P.M. and Hamaus, N. and Wandelt, B. (2015)
	Dark matter voids in the SDSS galaxy survey
	Journal of Cosmology and Astroparticle Physics 03, 047 (2015)
	arXiv:1410.0355 [astro-ph.CO]

	Sutter, P.M. and Lavaux, G. and Wandelt, B.D. and Weinberg, D.H. (2012)
	A public void catalog from the SDSS DR7 Galaxy Redshift Surveys based on the watershed transform
	The Astrophysical Journal 761, 44 (2012)
	arXiv:1207.2524 [astro-ph.CO]

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
