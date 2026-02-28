# Generate a partition_function Z using 1D hamiltonian from Ising1D.py

from Ising1D import config_energy
import numpy as np
from numpy import random

N = 100
spin_states = [1]*N

print(config_energy(spin_states, h=0))
