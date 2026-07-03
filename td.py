#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 16:19:36 2025

@author: aidandombrosky
"""

import yt
from yt.units import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import h5py


ds1 = yt.load("/scratch/ebuie/ISO_Turb/midway/1E23_S100_z03/ISM_hdf5_chk_0011")
ds2 = yt.load("/scratch/ebuie/ISO_Turb/midway/1E23_S60_z1/ISM_hdf5_chk_0011")

my_sphere1 = ds1.sphere("c", (100.0, "pc"))

plot1 = yt.PhasePlot(
    my_sphere1,
    ("gas", "density"),
    ("gas", "temperature"),
    ("gas", "mass"),
    weight_field=None,
)

plot1.set_unit(("gas", "mass"), "g")

my_sphere2 = ds2.sphere("c", (100.0, "pc"))

plot2 = yt.PhasePlot(
    my_sphere2,
    ("gas", "density"),
    ("gas", "temperature"),
    ("gas", "mass"),
    weight_field=None,
)

plot2.set_unit(("gas", "mass"), "g")

plot1.save("phase_0011m.png")
plot2.save("phase_0011.png")


def _ndens(field,data):
    return data['density'] / (1.67e-24*g )
yt.add_field("ndens", function=_ndens, units="cm**-3", sampling_type="cell")




