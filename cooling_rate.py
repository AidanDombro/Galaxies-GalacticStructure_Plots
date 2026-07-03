#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:26:19 2025

@author: aidandombrosky
"""

import matplotlib.pyplot as plt
import numpy as np

T = np.arange(1, 1e4)
n = 8.99e-5

cool = (8e-27)*((n**2))*((100/T)**(1/2))*(np.e)**(-92/T)

plt.figure(figsize=(12, 8))

plt.plot(T, cool, color = 'r', lw = 3)

plt.xlabel('Temperature [K]', fontsize = 18)
plt.ylabel('Cooling Rate', fontsize = 18)
plt.title('Cooling of C II', fontsize = 20)



plt.show()
