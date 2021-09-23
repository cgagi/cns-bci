"""
Created on Wed Apr 22 15:15:16 2015

@author: rkp

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from week2.compute_sta import compute_sta

import os


# FILENAME = 'c1p8.pickle'
FILENAME = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'week2', 'c1p8_3.4.pickle')

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']

# Fill in these values
sampling_period = 2*len(stim) # in ms
num_timesteps = len(stim)

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()