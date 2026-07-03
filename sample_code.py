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


ds = yt.load("/scratch/ebuie/ISO_Turb/midway/1E23_S100_z1/ISM_hdf5_chk_0012")


slc = yt.SlicePlot(ds, 'z', 'temperature')

slc.set_zlim("temperature", 5000.0, 1.0e5)

slc.save("ISM_012_temperature_slice.png")


