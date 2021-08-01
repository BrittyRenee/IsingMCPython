# a script that will make a simulation of the ising model
# based off previous matlab script
# ultimate practice for python and getting physics experience
# improvements planned are adding a GUI that will allow manipulation of parameters without going into the script itself
# another imporvement will finding out how to plot or at least store the data gathered
# possibly display data and manually mark it down? Or use a different script to continuosly plot data

import ising_tools

L = 100 #This is the dimension of the LxL matrix
p = 0.5 # p == % of "spin ups" that are initializing our lattice
temp = 2 #value for the temperature
#Then the number of trials are determined
trials = 500

file_title = input("Please enter name for files: ")

#Then the lattice is set up using the create_lattice function
initial_lat = ising_tools.create_lattice(L,p)

# Then the lattice type: 'donut', 'positive', 'negative', or default
lat_type = 'donut'

final_lat = ising_tools.animate_lattice(trials, initial_lat, L, temp, lat_type, file_title)