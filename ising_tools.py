# Contains the Monte Carlo function for ising and the different lattice parameters
# Also contains the animated plot for the changing ising lattice

import matplotlib.pyplot as plt
import numpy as np
import random
import math

def create_lattice(L,p):
    # creates the initial lattice
    lat_shape = (L,L)
    lattice = np.zeros(lat_shape)
    for i in np.arange(0,L):
        for j in np.arange(0,L):
            if random.random() < p:
                lattice[i, j] = 1
            else:
                lattice[i, j] = -1

    plt.ion()
    plt.show()

    lat_im = plt.imshow(lattice, cmap='cool', vmin=-1,vmax=1, interpolation='none')
    return lattice

def ising_eq(val,temp, S):
    E = (2*val)*S
    if E<0 or random.random() < math.exp((-1*E)/temp):
            val = val * -1
    else:
        val = val
    return val


def lattice_default(lattice, L, temp):
    #This is the default lattice where boundaries are present
    for i in np.arange(0, (L**2)):
        x = random.randint(0, L-1)
        y = random.randint(0, L-1)
        if x == 0 and y == 0:
            S = lattice[x+1, y] + lattice[x, y+1] #this prevents from going out of bounds in the matrix
        elif x == 0 and y < (L-1):
            S = lattice[x+1, y] + lattice[x, y+1] + lattice[x, y-1]
        elif x == 0 and y == (L-1):
            S = lattice[x+1, y] + lattice[x, y-1]
        elif y == 0 and x < (L-1):
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y+1]
        elif x == (L-1) and y == (L-1):
            S = lattice[x-1, y] + lattice[x, y-1]
        elif x == (L-1):
            S= lattice[x-1, y] + lattice[x, y+1] + lattice[x, y-1]
        elif y == (L-1):
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y-1]
        else:
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y+1] + lattice[x, y-1]

        lattice[x, y] = ising_eq(lattice[x, y], temp, S)

    return lattice


def lattice_donut(lattice, L, temp):
    # this is the lattice model to simulate no boundaries... or a pseudo-infinite lattice. This would create the shape of a donut.
    for i in np.arange(0,(L**2)):
        x = random.randint(0, L-1)
        y = random.randint(0, L-1)
        if x == 0 and y == 0:
            S = lattice[x+1, y] + lattice[x, y+1] + lattice[L-1, y] + lattice[x, L-1]
        elif x == 0 and y < (L-1):
            S = lattice[x+1, y] + lattice[x, y+1] + lattice[x, y-1] + lattice[L-1, y]
        elif x == 0 and y == (L-1):
            S = lattice[x+1, y] + lattice[x, y-1] + lattice[L-1, y] + lattice[x, 0]
        elif y == 0 and x < (L-1):
            S = lattice[x-1, y] + lattice[x, y+1] + lattice[x, L-1] + lattice[0, y]
        elif y == (L-1) and x == (L-1):
            S = lattice[x-1, y] + lattice[x, y-1] + lattice[0, y] + lattice[x, 0]
        elif x == (L-1):
            S = lattice[x-1, y] + lattice[x, y+1] + lattice[x, y-1] + lattice[0, y]
        elif y == (L-1):
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y-1] + lattice[x, 0]
        else:
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y-1] + lattice[x, y+1]
        
        lattice[x, y] = ising_eq(lattice[x, y], temp, S)
        
    return lattice

def neg_lattice(lattice, L, temp):
    #simulates a lattice located within an all negative field
    for i in np.arange(0,L**2):
        x = random.int(0, L-1)
        y = random.int(0, L-1)
        if x == 0 and y == 0:
            S = lattice[x+1, y] + lattice[x, y+1] - 1 - 1 #this prevents us from leaving matrix bounds
        elif x == 0 and y < (L-1):
            S = lattice[x+1, y] + lattice[x, y+1] + lattice[x, y-1] - 1
        elif x == 0 and y == (L-1):
            S = lattice[x+1, y] + lattice[x, y-1] - 1 - 1
        elif y == 0 and x < (L-1):
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y+1] - 1
        elif y == 0 and x == (L-1):
            S = lattice[x-1, y] + lattice[x, y+1] - 1 - 1
        elif x == (L-1):
            S = lattice[x-1, y] + lattice[x, y+1] + lattice[x, y-1] - 1
        elif y == (L-1):
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y-1] - 1
        else:
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y+1] + lattice[x, y-1]

        lattice[x,y] = ising_eq(lattice[x,y], temp, S)
    
    return lattice

def pos_lattice(lattice, L, temp):
    #simulates a lattice located within an all positive field
    for i in np.arange(0,L**2):
        x = random.int(0, L-1)
        y = random.int(0, L-1)
        if x == 0 and y == 0:
            S = lattice[x+1, y] + lattice[x, y+1] + 1 + 1 #this prevents us from leaving matrix bounds
        elif x == 0 and y < (L-1):
            S = lattice[x+1, y] + lattice[x, y+1] + lattice[x, y-1] + 1
        elif x == 0 and y == (L-1):
            S = lattice[x+1, y] + lattice[x, y-1] + 1 + 1
        elif y == 0 and x < (L-1):
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y+1] + 1
        elif y == 0 and x == (L-1):
            S = lattice[x-1, y] + lattice[x, y+1] + 1 + 1
        elif x == (L-1):
            S = lattice[x-1, y] + lattice[x, y+1] + lattice[x, y-1] + 1
        elif y == (L-1):
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y-1] + 1
        else:
            S = lattice[x+1, y] + lattice[x-1, y] + lattice[x, y+1] + lattice[x, y-1]

        lattice[x,y] = ising_eq(lattice[x,y], temp, S)
    
    return lattice

def animate_lattice(trials, lattice, L, temp, lat_type, file_title):
    plt.ion()
    plt.show()

    lat_im = plt.imshow(lattice, cmap='cool', vmin=-1,vmax=1, interpolation='none')
    t = 0
    for i in np.arange(0, trials+1):
        if t % 1 == 0:
            lat_im.set_data(lattice)
            plt.draw()
        if (t == 0) or (t % 25 == 0):
            plt.savefig(f"{file_title}-{t}")
        lattice = update_lat(lattice, L, temp, lat_type)
        plt.pause(.05)
        t += 1
    
    return lattice

def update_lat(lattice, L, temp, lat_type):
    if lat_type == 'donut':
        lattice = lattice_donut(lattice, L, temp)
    elif lat_type == 'ipositive':
        lattice == pos_lattice(lattice, L, temp)
    elif lat_type == 'negative':
        lattice == neg_lattice(lattice, L, temp)
    else:
        lattice == lattice_default(lattice, L, temp)

    return lattice
