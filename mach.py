#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 21:43:50 2025

@author: aidandombrosky
"""

import yt
import numpy as np
from yt.utilities.physical_constants import kboltz, mp

gamma = 5.0/3.0
mu = 1.4 

ds = yt.load("/scratch/ebuie/ISO_Turb/midway/1E25_S100_z1/ISM_hdf5_chk_0009")

#Sound speed (c_s) in cm/s
def _sound_speed(field, data):
    T = data["gas", "temperature"]
    cs = np.sqrt(gamma * kboltz* T / (mu * mp))
    return cs

#Mach number
def _mach_number(field, data):
    vmag = data["gas", "velocity_magnitude"]
    cs = data["gas", "sound_speed"]
    return vmag / cs

yt.add_field(("gas", "sound_speed"), function=_sound_speed, units="cm/s", sampling_type="cell")
yt.add_field(("gas", "mach_number"), function=_mach_number, units="", sampling_type="cell")

#Slice plot of Mach number
slc = yt.SlicePlot(ds, "z", ("gas","mach_number"))
slc.set_log(("gas","mach_number"), True)
slc.set_zlim(("gas","mach_number"), 1e-2, 1e2)
slc.annotate_title("Mach Number Slice (z-plane)")
slc.save("mach_slice.png")

#Phase plot: Mach (x) vs Temperature (y)
ad = ds.all_data()
pp = yt.PhasePlot(ad, ("gas","mach_number"), ("gas","temperature"),
                  ("gas","cell_mass"), weight_field=None, fractional=True,
                  x_bins=256, y_bins=256)
pp.set_unit(("gas","temperature"), "K")
pp.set_xlim(1e-2, 1e2)
pp.set_ylim(1e1, 1e7)

pp.set_log(("gas","mach_number"), True)
pp.set_log(("gas","temperature"), True)

pp.save("mach_vs_T_phase.png")