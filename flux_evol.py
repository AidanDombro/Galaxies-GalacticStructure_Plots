#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 13:16:45 2026

@author: aidandombrosky
"""
##Worksheet 1: Introduction to Galaxies - Aidan Dombrosky

import numpy as np
import matplotlib.pyplot as plt

##Question 6
##(a)

#Defining the variables of L, d, and tau:
L_sun = 3.8e33              #luminosity of our Sun in erg/s
L = 2.6e10 * (L_sun)        #luminosity of any star in solar luminosities

d = 1000 * (3.086e21)        #distance to object in kpc converted to cm so we have nice and easy cgs units
                            #also made this begin at 1000 kpc for part (c)

tau = 0.68                  #optical depth
    
#Flux naught with the inverse square law:
F_0 = L/(4 * np.pi * d**2)

#Flux observed as the whole enchilada:
F_obs = F_0 * np.exp(- tau)

print(F_obs) #it works!

##(b)

# Stars that would dominate a galaxy's light would be those massive O and B type stars that come back again 
# and again from ASTR-220 and 320. We know from seeing these before, that their luminosities increase up until 
# a peak, afterward the stars explode, die, and begin to slowly dim over time. Since these are the dominant light
# in a galaxy, we would likely see this trend in star-rich regions of galaxies, as the galaxy dims with older age 
# and the more massive stars (and their messy remnants) eventually fizzle out. The optical depth would likely 
# decrease just as luminosity. After 10 million years, I imagine the dust, gas, and heavier matter like starstuff 
# would be cleared out in the ISM, making the galaxy optically thinner as it ages. 

##(c)

#Time array for the 10^8 yr (100 Myrs) by a step of 10^6 yr (1 Myr):
t = np.arange(0, 101, 1)

#Here's the luminosity evolution of a star modeled after our Sun with pretty crude numbers:
L_peak = 2.6e10                 #peak luminosity of L_sun
t_peak = 4.0                    #time of peak in Myr 

t_rise = 2.0                    #rise timescale in Myr
t_decay = 15.0                  #decay timescale in Myr

#I used a piecewise function to show the L's intial rise and then exponential decay as I put in part (b):
L_solar = np.where(t <= t_peak,
                   L_peak * np.exp(-((t - t_peak)**2) / (2 * t_rise**2)),
                   L_peak * np.exp(-(t - t_peak) / t_decay))

L = L_solar * L_sun             #converting from solar Ls to erg/s

#Now the optical depth evolution starting thick and thinning over time:
tau_initial = 2.0               #initial optical depth (highest)
tau_final = 0.1                 #final optical depth (lowest with some extra gunk)
t_clear = 20.0                  #clearing timescale in Myr

tau = tau_final + (tau_initial - tau_final) * np.exp(-t / t_clear)

#Using the naught/obs flux i used in part (a):
F_0 = L / (4 * np.pi * d**2)    #flux-naught

F_obs = F_0 * np.exp(-tau)      #flux-observed

#Plotting 'er up:
plt.figure(figsize=(10, 6))

plt.plot(t, F_obs, 'g-', linewidth=2, label='Observed Flux F$_{obs}$')

#"Pimping the plot" - Juan Merlo:
plt.xlabel('Time (Myr)', fontsize=12)
plt.ylabel('Flux (erg s$^{-1}$ cm$^{-2}$)', fontsize=12)

plt.title('Flux Evolution at 1 Mpc', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)

plt.grid(True, alpha=0.3)

plt.xlim(0, 100)
plt.yscale('log')

plt.tight_layout()
plt.show()