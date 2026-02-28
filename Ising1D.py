import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# Start of with defining lattice positions in 1D and seperate array for spin states randomised to find total energy.

# Write function for general expression for hamiltonian H = -J sigma (s1.s2) - h sigma s. Assume a closed form, where the first and final spin states are neighbouring.

def config_energy(list_spins, h):
    edge_case = list_spins[0]*list_spins[-1]
    sum_list_interacting = [list_spins[i]*list_spins[i+1] for i in range(0, len(list_spins) - 1)]
    sum_list_ext = sum(list_spins)
    return ((-1*(edge_case + sum(sum_list_interacting))) - h*sum_list_ext)


if __name__ == "__main__":

    # Define spin states
    N = 100
    spin_states = np.random.choice([-1, 1], size=N)

    # Special Case 1 : All spin up

    spin_states_up = [1]*N

    # Special Case 2 : All spin down

    spin_states_down = [-1]*N

    # Special Case 1 : Alternating spin up and down

    spin_states_alt = [(-1)**n for n in range(N)]

    #plt.plot(['spin_states_up', 'spin_states_down', 'spin_states_alt'], [config_energy(spin_states_up,0), config_energy(spin_states_down,0), config_energy(spin_states_alt,0)])
    #plt.show()

    ## Introducing External Field.
    # 
    # h/J << 1 implise field is weak and spin-spin interactions dominate.
    # h/J ~ 1 implies field and interactions compete
    # h/J >> 1 implies field dominates forcing all spins to allign with it.

    # Scenario 1 (since J = 1, set h = 0.001)

    plt.figure()
    plt.plot(['spin_states_up', 'spin_states_down', 'spin_states_alt'], 
            [config_energy(spin_states_up, -0.001), config_energy(spin_states_down, -0.001), config_energy(spin_states_alt, -0.001)],
            label='h/J = 0.001')

    # Scenario 2 (since J = 1, set h = 1)

    plt.plot(['spin_states_up', 'spin_states_down', 'spin_states_alt'], 
            [config_energy(spin_states_up, -1), config_energy(spin_states_down, -1), config_energy(spin_states_alt, -1)],
            label='h/J = 1')

    # Scenario 3 (since J = 1, set h = 10)

    plt.plot(['spin_states_up', 'spin_states_down', 'spin_states_alt'], [config_energy(spin_states_up, -10), config_energy(spin_states_down, -10), config_energy(spin_states_alt, -10)], label='h/J = 10')

    plt.legend()
    plt.ylabel('Energy')
    plt.title('Energy of spin configurations under different external fields')
    plt.show()