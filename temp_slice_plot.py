#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:38:24 2025

@author: aidandombrosky
"""

import h5py
print(h5py.__version__)

import yt
from yt.units import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import h5py


ds1 = yt.load("/scratch/ebuie/ISO_Turb/midway/1E23_S60_z1/ISM_hdf5_chk_0011")
ds2 = yt.load("/scratch/ebuie/ISO_Turb/midway/1E23_S100_z1/ISM_hdf5_chk_0012")


slc1 = yt.SlicePlot(ds1, 'z', 'temperature')
slc2 = yt.SlicePlot(ds2, 'z', 'temperature')

slc1.save("ISM_0011_temp_slice.png")
slc2.save("ISM_0012_temp_slice.png")




