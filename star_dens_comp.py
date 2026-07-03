#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 22:35:25 2026

@author: aidandombrosky
"""

import numpy as np
import matplotlib.pyplot as plt

#Problem statement stuff:
n0 = 0.1        #star pc^-3
h_R = 400       #pc
R = np.linspace(-1500, 1500, 1000)

#Exponential profile:
n_exp = n0 * np.exp(-np.abs(R) / h_R)

#Sech^2 profile:
n_sech2 = n0 * (1.0 / np.cosh(R / (2 * h_R)))**2

#Plotting 'er up:
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(R, n_exp,  color='#2196F3', linewidth=2.2, label=r'$n_0 \, e^{-|R|/h_R}$')
ax.plot(R, n_sech2, color='#E53935', linewidth=2.2, linestyle='--', label=r'$n_0 \, \mathrm{sech}^2\!\left(\frac{R}{2h_R}\right)$')

ax.set_xlabel('Height Above/Below Disk, R [pc]', fontsize=13)
ax.set_ylabel(r'Stellar Density, $n$ [stars pc$^{-3}$]', fontsize=13)

ax.set_title('Stellar Density Profile Comparison', fontsize=14, fontweight='bold')
ax.legend(fontsize=12, loc='upper right')

ax.set_xlim(-1500, 1500)
ax.set_ylim(0, 0.115)

ax.grid(True)
ax.tick_params(labelsize=11)

plt.tight_layout()