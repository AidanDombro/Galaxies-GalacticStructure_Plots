#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 18:48:34 2025

@author: aidandombrosky
"""

# q4_phaseplot.py
# (a) Temperature vs density phase plots with yt.PhasePlot
# (b) C II column density maps
# (c) C II cooling slice plots (unchanged)

import yt
import numpy as np
from astropy import constants as const
from astropy import units as u

# ---- USER PARAMETERS ----
file1 = "/scratch/ebuie/ISO Turb/midway/1E23 S100 z1/ISM_hdf5_chk_0012"
file2 = "/scratch/ebuie/ISO Turb/midway/1E25 S100 z1/ISM_hdf5_chk_0009"

C_abundance = 1e-4
electron_fraction = 1e-2
ion_frac_CII = 1.0

m_p = const.m_p.cgs.value
X_H = 0.70

save_prefix = "Q4_phaseplot"

# ---- Derived fields ----
def add_fields(ds, C_ab=C_abundance, e_frac=electron_fraction, f_CII=ion_frac_CII):
    # n_H
    if ('gas','n_H') not in ds.field_list:
        def _n_H(field, data):
            if ('gas','H_number_density') in ds.field_list:
                return data[('gas','H_number_density')].in_units('1/cm**3')
            rho = data[('gas','density')].in_units('g/cm**3')
            return (rho * X_H / m_p).in_units('1/cm**3')
        yt.add_field(('gas','n_H'), function=_n_H, units='1/cm**3', sampling_type='cell')

    # n_CII
    if ('gas','n_CII') not in ds.field_list:
        def _n_CII(field, data):
            nH = data[('gas','n_H')].in_units('1/cm**3')
            return (C_ab * f_CII * nH).in_units('1/cm**3')
        yt.add_field(('gas','n_CII'), function=_n_CII, units='1/cm**3', sampling_type='cell')

    # Lambda_CII
    if ('gas','Lambda_CII') not in ds.field_list:
        def _Lambda_CII(field, data):
            T = data[('gas','temperature')].in_units('K').value
            nH = data[('gas','n_H')].in_units('1/cm**3').value
            n_e = e_frac * nH
            n_C = C_ab * nH
            T_safe = np.clip(T,1e-2,None)
            lam = 8e-20*(1/T_safe)**0.5*np.exp(-92.0/T_safe)*n_e*n_C
            return (lam*u.erg/(u.cm**3*u.s)).to('erg/cm**3/s')
        yt.add_field(('gas','Lambda_CII'), function=_Lambda_CII,
                     units='erg/cm**3/s', sampling_type='cell')

# ---- Load datasets and add fields ----
ds1 = yt.load(file1)
ds2 = yt.load(file2)
add_fields(ds1)
add_fields(ds2)

# ---- (a) Phase plots with yt.PhasePlot ----
ad1 = ds1.all_data()
ad2 = ds2.all_data()

# x = n_H, y = temperature, colorbar = total mass per bin
pp1 = yt.PhasePlot(ad1, ('gas','n_H'), ('gas','temperature'), ('gas','cell_mass'),
                   weight_field=None)
pp2 = yt.PhasePlot(ad2, ('gas','n_H'), ('gas','temperature'), ('gas','cell_mass'),
                   weight_field=None)

# set same limits if desired:
pp1.set_log(('gas','n_H'), True)
pp1.set_log(('gas','temperature'), True)
pp1.set_unit(('gas','n_H'), 'cm**-3')
pp1.set_unit(('gas','temperature'), 'K')
pp1.set_xlabel(r'$n_\mathrm{H}$ (cm$^{-3}$)')
pp1.set_ylabel(r'T (K)')
pp1.annotate_title("Dataset 1")

pp2.set_log(('gas','n_H'), True)
pp2.set_log(('gas','temperature'), True)
pp2.set_unit(('gas','n_H'), 'cm**-3')
pp2.set_unit(('gas','temperature'), 'K')
pp2.set_xlabel(r'$n_\mathrm{H}$ (cm$^{-3}$)')
pp2.set_ylabel(r'T (K)')
pp2.annotate_title("Dataset 2")

# save figures
pp1.save(f"{save_prefix}_ds1")
pp2.save(f"{save_prefix}_ds2")
print("Saved yt PhasePlots for both datasets.")

# ---- (b) and (c): you can reuse the same CII column + slice code from before ----
# e.g., call your previously written make_CII_column() and save_map() functions
