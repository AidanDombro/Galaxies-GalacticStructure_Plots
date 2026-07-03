#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 22:14:10 2025

@author: aidandombrosky
"""

import numpy as np
import matplotlib.pyplot as plt

Q_0 = 2e48
rh_0 = 9e-23
m_H = 1.67e-24
al_0 = 2.6e-13

n_0 = rh_0/m_H

t_ion = 1/(al_0 * n_0)

t = np.logspace(-2, 2, 500) * t_ion

v_i = (((Q_0 * n_0 * al_0**2)/(36 * np.pi))**(1/3) * (np.exp(-t/t_ion))/(1 - np.exp(-t/t_ion))**(2/3))/(1e5)

plt.loglog(t / (3.15e7), v_i) 

plt.axhline(13, linestyle = '--')

plt.xlabel("Time [yr]")
plt.ylabel("$v_i$ [km/s]")

plt.grid(True)
plt.show()


