import numpy as np

#Load galaxy catalog
ra,dec,redshift,u,g,r,i,z,ugModelColor,grModelColor,riModelColor,izModelColor,Mr,is_red,tweb,diva,origami = np.loadtxt("galaxy_catalog.dat", comments="#", unpack=True)
is_red=is_red.astype(int)
tweb=tweb.astype(int)
diva=diva.astype(int)
origami=origami.astype(int)

# ----------------------------------------------------------------------------------
# -------------------- INFORMATION GAIN (PARENT) -----------------------------------
# ----------------------------------------------------------------------------------

Ntot=float(is_red.size)
Nred=float(np.sum(is_red==1))
Nblue=Ntot-Nred
H_parent = -Nred/Ntot*np.log2(Nred/Ntot) -Nblue/Ntot*np.log2(Nblue/Ntot)

# ----------------------------------------------------------------------------------
# -------------------- INFORMATION GAIN (TWEB) -------------------------------------
# ----------------------------------------------------------------------------------

is_red_voids_tweb=is_red[np.where(tweb==0)]
Nvoids_tweb=float(is_red_voids_tweb.size)
Nred_voids_tweb=float(np.sum(is_red_voids_tweb==1))
Nblue_voids_tweb=Nvoids_tweb-Nred_voids_tweb
H_tweb_voids = -Nred_voids_tweb/Nvoids_tweb*np.log2(Nred_voids_tweb/Nvoids_tweb) -Nblue_voids_tweb/Nvoids_tweb*np.log2(Nblue_voids_tweb/Nvoids_tweb)

is_red_sheets_tweb=is_red[np.where(tweb==1)]
Nsheets_tweb=float(is_red_sheets_tweb.size)
Nred_sheets_tweb=float(np.sum(is_red_sheets_tweb==1))
Nblue_sheets_tweb=Nsheets_tweb-Nred_sheets_tweb
H_tweb_sheets = -Nred_sheets_tweb/Nsheets_tweb*np.log2(Nred_sheets_tweb/Nsheets_tweb) -Nblue_sheets_tweb/Nsheets_tweb*np.log2(Nblue_sheets_tweb/Nsheets_tweb)

is_red_filaments_tweb=is_red[np.where(tweb==2)]
Nfilaments_tweb=float(is_red_filaments_tweb.size)
Nred_filaments_tweb=float(np.sum(is_red_filaments_tweb==1))
Nblue_filaments_tweb=Nfilaments_tweb-Nred_filaments_tweb
H_tweb_filaments = -Nred_filaments_tweb/Nfilaments_tweb*np.log2(Nred_filaments_tweb/Nfilaments_tweb) -Nblue_filaments_tweb/Nfilaments_tweb*np.log2(Nblue_filaments_tweb/Nfilaments_tweb)

is_red_clusters_tweb=is_red[np.where(tweb==3)]
Nclusters_tweb=float(is_red_clusters_tweb.size)
Nred_clusters_tweb=float(np.sum(is_red_clusters_tweb==1))
Nblue_clusters_tweb=Nclusters_tweb-Nred_clusters_tweb
H_tweb_clusters = -Nred_clusters_tweb/Nclusters_tweb*np.log2(Nred_clusters_tweb/Nclusters_tweb) -Nblue_clusters_tweb/Nclusters_tweb*np.log2(Nblue_clusters_tweb/Nclusters_tweb)

# information gain, weighting using galaxies
H_tweb = Nvoids_tweb/Ntot*H_tweb_voids + Nsheets_tweb/Ntot*H_tweb_sheets + Nfilaments_tweb/Ntot*H_tweb_filaments + Nclusters_tweb/Ntot*H_tweb_clusters
IG_tweb = H_parent - H_tweb

print("Information gain TWEB: %f" % IG_tweb)

# ----------------------------------------------------------------------------------
# -------------------- INFORMATION GAIN (DIVA) -------------------------------------
# ----------------------------------------------------------------------------------

is_red_voids_diva=is_red[np.where(diva==0)]
Nvoids_diva=float(is_red_voids_diva.size)
Nred_voids_diva=float(np.sum(is_red_voids_diva==1))
Nblue_voids_diva=Nvoids_diva-Nred_voids_diva
H_diva_voids = -Nred_voids_diva/Nvoids_diva*np.log2(Nred_voids_diva/Nvoids_diva) -Nblue_voids_diva/Nvoids_diva*np.log2(Nblue_voids_diva/Nvoids_diva)

is_red_sheets_diva=is_red[np.where(diva==1)]
Nsheets_diva=float(is_red_sheets_diva.size)
Nred_sheets_diva=float(np.sum(is_red_sheets_diva==1))
Nblue_sheets_diva=Nsheets_diva-Nred_sheets_diva
H_diva_sheets = -Nred_sheets_diva/Nsheets_diva*np.log2(Nred_sheets_diva/Nsheets_diva) -Nblue_sheets_diva/Nsheets_diva*np.log2(Nblue_sheets_diva/Nsheets_diva)

is_red_filaments_diva=is_red[np.where(diva==2)]
Nfilaments_diva=float(is_red_filaments_diva.size)
Nred_filaments_diva=float(np.sum(is_red_filaments_diva==1))
Nblue_filaments_diva=Nfilaments_diva-Nred_filaments_diva
H_diva_filaments = -Nred_filaments_diva/Nfilaments_diva*np.log2(Nred_filaments_diva/Nfilaments_diva) -Nblue_filaments_diva/Nfilaments_diva*np.log2(Nblue_filaments_diva/Nfilaments_diva)

is_red_clusters_diva=is_red[np.where(diva==3)]
Nclusters_diva=float(is_red_clusters_diva.size)
Nred_clusters_diva=float(np.sum(is_red_clusters_diva==1))
Nblue_clusters_diva=Nclusters_diva-Nred_clusters_diva
H_diva_clusters = -Nred_clusters_diva/Nclusters_diva*np.log2(Nred_clusters_diva/Nclusters_diva) -Nblue_clusters_diva/Nclusters_diva*np.log2(Nblue_clusters_diva/Nclusters_diva)

# information gain, weighting using galaxies
H_diva = Nvoids_diva/Ntot*H_diva_voids + Nsheets_diva/Ntot*H_diva_sheets + Nfilaments_diva/Ntot*H_diva_filaments + Nclusters_diva/Ntot*H_diva_clusters
IG_diva = H_parent - H_diva

print("Information gain DIVA: %f" % IG_diva)

# ----------------------------------------------------------------------------------
# ------------------- INFORMATION GAIN (ORIGAMI) -----------------------------------
# ----------------------------------------------------------------------------------

is_red_voids_origami=is_red[np.where(origami==0)]
Nvoids_origami=float(is_red_voids_origami.size)
Nred_voids_origami=float(np.sum(is_red_voids_origami==1))
Nblue_voids_origami=Nvoids_origami-Nred_voids_origami
H_origami_voids = -Nred_voids_origami/Nvoids_origami*np.log2(Nred_voids_origami/Nvoids_origami) -Nblue_voids_origami/Nvoids_origami*np.log2(Nblue_voids_origami/Nvoids_origami)

is_red_sheets_origami=is_red[np.where(origami==1)]
Nsheets_origami=float(is_red_sheets_origami.size)
Nred_sheets_origami=float(np.sum(is_red_sheets_origami==1))
Nblue_sheets_origami=Nsheets_origami-Nred_sheets_origami
H_origami_sheets = -Nred_sheets_origami/Nsheets_origami*np.log2(Nred_sheets_origami/Nsheets_origami) -Nblue_sheets_origami/Nsheets_origami*np.log2(Nblue_sheets_origami/Nsheets_origami)

is_red_filaments_origami=is_red[np.where(origami==2)]
Nfilaments_origami=float(is_red_filaments_origami.size)
Nred_filaments_origami=float(np.sum(is_red_filaments_origami==1))
Nblue_filaments_origami=Nfilaments_origami-Nred_filaments_origami
H_origami_filaments = -Nred_filaments_origami/Nfilaments_origami*np.log2(Nred_filaments_origami/Nfilaments_origami) -Nblue_filaments_origami/Nfilaments_origami*np.log2(Nblue_filaments_origami/Nfilaments_origami)

is_red_clusters_origami=is_red[np.where(origami==3)]
Nclusters_origami=float(is_red_clusters_origami.size)
Nred_clusters_origami=float(np.sum(is_red_clusters_origami==1))
Nblue_clusters_origami=Nclusters_origami-Nred_clusters_origami
H_origami_clusters = -Nred_clusters_origami/Nclusters_origami*np.log2(Nred_clusters_origami/Nclusters_origami) -Nblue_clusters_origami/Nclusters_origami*np.log2(Nblue_clusters_origami/Nclusters_origami)

# information gain, weighting using galaxies
H_origami = Nvoids_origami/Ntot*H_origami_voids + Nsheets_origami/Ntot*H_origami_sheets + Nfilaments_origami/Ntot*H_origami_filaments + Nclusters_origami/Ntot*H_origami_clusters
IG_origami = H_parent - H_origami

print("Information gain ORIGAMI: %f" % IG_origami)
