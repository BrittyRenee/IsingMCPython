# a script that will make a simulation of the ising model
# based off previous matlab script
# ultimate practice for python and getting physics experience

import ising_tools

L = 100 #This is the dimension of the LxL matrix
p = 0.5 # p == % of "spin ups" that are initializing our lattice
temp = 1.5 #value for the temperature
#Then the number of trials are determined
trials = 500 #number of loops for the Mote Carlo Portion

x = 0 #allocation of our average magnetization

# Then the lattice type: 'donut', 'positive', 'negative', or default
lat_type = 'donut'
bias = 'negative' # This variable indicates whether you want an almost negligable positive or negative bias to ensure results are either above or below the x-axis
animate_lattice = False # True if you want to animate lattice. False if you don't want an animation.

exp_runs = int(input("Please enter the number of experiments: "))

for i in list(range(exp_runs)):
    #Then the lattice is set up using the create_lattice function
    initial_lat = ising_tools.create_lattice(L,p)
    if animate_lattice == True:
        file_title = input("Please enter name for image files: ")
        final_lat, val = ising_tools.animate_lattice(trials, initial_lat, L, temp, lat_type, file_title, bias)
    else:
        final_lat, val = ising_tools.monte_lattice(trials, initial_lat, L, temp, lat_type, bias)
    x = x + val

avg_mag = x / exp_runs
print(avg_mag)
