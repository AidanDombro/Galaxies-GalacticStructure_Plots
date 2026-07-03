#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:21:15 2026

@author: aidandombrosky
"""
import numpy as np
import matplotlib.pyplot as plt

#Defining some things:
I_0 = 1
R_e = 2

r = np.linspace(0.01, 10, 2000)

#de Vaucouleurs (crazy French I'll abbreviate as deV) Law below:
n_deV = 4           #Sersic index of 4 for deV
b_deV = 2*n_deV - (1/3)

I_deV = np.exp((b_deV) * ((r/R_e)**(1/n_deV) - 1))
    
#Sersic formula (for the radial trend) below:
n_S = 1             #Sersic index of 1 for deV
b_S = 2*n_S - (1/3)

I_S = np.exp((b_S) * ((r/R_e)**(1/n_S) - 1))

#Plotting 'er up:
plt.plot(r, I_deV, 'r', linewidth=2, label='de Vaucouleurs Law')
plt.plot(r, I_S, 'g--', linewidth=2, label='Sersic Profile')

#"Pimping the plot" - Juan Merlo:
plt.xlabel('Radius (R/$R_e$)', fontsize=12)
plt.ylabel('I(R)', fontsize=12)

plt.title('Comparison of de Vaucouleurs Law & the Sersic Profile', fontsize=10, fontweight='bold')
plt.legend(fontsize=10) 

plt.grid(True, alpha=0.3)

plt.xlim(0,10)
plt.gca().invert_yaxis()
plt.yscale('log')

plt.tight_layout()
plt.show()