#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:44:15 2026

@author: aidandombrosky
"""

import numpy as np
import matplotlib.pyplot as plt

#Constants and sucH:
G = 6.67e-8                 #cm^3/g^1/s^2
rho_0 = 1e-26               #g/cm^3

r_0 = 150                   #kpc
r_0_cm = r_0 * 3.086e21     #converting to cm

kpc_to_cm = 3.086e21        #converting to cm

#for 0 < r < r_0:
def phi_inner(r_kpc):

    r_cm = r_kpc * kpc_to_cm
    term1 = 3 * np.pi * G * rho_0 * r_0_cm**(5/3)
    term2 = 4 * r_0_cm**(1/3) - 3 * r_cm**(1/3)
    return -term1 * term2

#for r > r_0:
def phi_outer(r_kpc):

    r_cm = r_kpc * kpc_to_cm
    return -3 * np.pi * G * rho_0 * r_0_cm**3 / r_cm

#Now thwe potential with our modified density profile:
def phi_modified(r_kpc):

    if r_kpc <= r_0:
        return phi_inner(r_kpc)
    else:
        
        r_cm = r_kpc * kpc_to_cm

        M_r0 = 3 * np.pi * rho_0 * r_0_cm**3

        M_extra = 2 * np.pi * rho_0 * r_0_cm * (r_cm**2 - r_0_cm**2)
        
        return -(G * (M_r0 + M_extra)) / r_cm

#Effective potential:
def phi_effective(r_kpc, L):

    r_cm = r_kpc * kpc_to_cm
    if r_kpc <= r_0:
        phi = phi_inner(r_kpc)
    else:
        phi = phi_outer(r_kpc)
    
    return phi + L**2 / (2 * r_cm**2)

#"Plot pimping" for (a):
r_inner = np.linspace(1, r_0, 150)  
phi_inner_vals = [phi_inner(r) for r in r_inner]

plt.figure(figsize=(10, 6))
plt.plot(r_inner, phi_inner_vals, 'b-', linewidth=2)

plt.xlabel('Radius (kpc)', fontsize=12)
plt.ylabel('Gravitational Potential Φ(r) (erg/g)', fontsize=12)
plt.title('Gravitational Potential for 0 < r < r₀', fontsize=14)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('a.png', dpi=300, bbox_inches='tight')
plt.show()

#"Plot pimping" for (b):
r_outer = np.linspace(150, 300, 150)
phi_outer_vals = [phi_outer(r) for r in r_outer]

plt.figure(figsize=(10, 6))
plt.plot(r_outer, phi_outer_vals, 'r-', linewidth=2)
plt.xlabel('Radius (kpc)', fontsize=12)
plt.ylabel('Gravitational Potential Φ(r) (erg/g)', fontsize=12)
plt.title('Gravitational Potential for 150 < r < 300 kpc', fontsize=14)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('b.png', dpi=300, bbox_inches='tight')
plt.show()

#"Plot pimping" for (c):
r_full = np.linspace(1, 2*r_0, 300)
phi_modified_vals = []
for r in r_full:
    if r <= r_0:
        phi_modified_vals.append(phi_inner(r))
    else:

        r_cm = r * kpc_to_cm
        M_total_inner = 3 * np.pi * rho_0 * r_0_cm**3

        M_additional = 2 * np.pi * rho_0 * r_0_cm * (r_cm**2 - r_0_cm**2)

        phi_modified_vals.append(-(G * (M_total_inner + 0.5*M_additional)) / r_cm)

plt.figure(figsize=(10, 6))
plt.plot(r_full, phi_modified_vals, 'g-', linewidth=2, label='Modified (ρ ∝ 1/r for r>r₀)')
plt.plot(r_inner, phi_inner_vals, 'b--', linewidth=1.5, alpha=0.7, label='Original (r<r₀)')
plt.plot(r_outer[:150], phi_outer_vals[:150], 'r--', linewidth=1.5, alpha=0.7, label='Original (r>r₀)')
plt.xlabel('Radius (kpc)', fontsize=12)
plt.ylabel('Gravitational Potential Φ(r) (erg/g)', fontsize=12)
plt.title('Modified Density Profile', fontsize=14)
plt.legend()

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('c.png', dpi=300, bbox_inches='tight')
plt.show()

#"Plot pimping" for (d):

#Angular momentum:
r_circ = 70 * kpc_to_cm
v_circ_sq = r_circ * 3 * np.pi * G * rho_0 * r_0_cm**(5/3) * r_circ**(-2/3)
v_circ = np.sqrt(v_circ_sq)
L = r_circ * v_circ

phi_eff_vals = [phi_effective(r, L) for r in r_full]

plt.figure(figsize=(10, 6))
plt.plot(r_full, phi_modified_vals, 'g-', linewidth=2, label='Φ(r) - Modified')
plt.plot(r_full, phi_eff_vals, 'b-', linewidth=2, label='$Φ_{eff}$(r) - Effective')

#Also going to plot the centrifugal term:
centrifugal = [L**2 / (2 * (r * kpc_to_cm)**2) for r in r_full]
plt.plot(r_full, centrifugal, 'r--', linewidth=1.5, alpha=0.7, label='L²/(2r²) - Centrifugal')
plt.xlabel('Radius (kpc)', fontsize=12)
plt.ylabel('Potential (erg/g)', fontsize=12)
plt.title(f'Effective Potential', fontsize=14)

plt.legend()
plt.grid(True, alpha=0.3)
plt.axvline(x=70, color='k', linestyle=':', alpha=0.5, label='r = 70 kpc')
plt.tight_layout()
plt.savefig('d.png', dpi=300, bbox_inches='tight')
plt.show()